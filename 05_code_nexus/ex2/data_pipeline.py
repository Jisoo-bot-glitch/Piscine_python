import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank = 0
        self.total = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        item = self.storage.pop(0)
        current_rank = self.rank
        self.rank += 1
        return (current_rank, item)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for row in data:
                if not isinstance(row, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(str(item))
            self.total += len(data)
        else:
            self.storage.append(str(data))
            self.total += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(item)
            self.total += len(data)
        else:
            self.storage.append(data)
            self.total += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not (isinstance(key, str) and isinstance(value, str)):
                    return False
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                for key, value in item.items():
                    if not (isinstance(key, str) and isinstance(value, str)):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                combined = ": ".join(item.values())
                self.storage.append(combined)
            self.total += len(data)
        else:
            combined = ": ".join(data.values())
            self.storage.append(combined)
            self.total += 1


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for e in stream:
            for proc in self.processors:
                if proc.validate(e):
                    proc.ingest(e)
                    break
            else:
                print(
                    f"DataStream error - Can't process element in stream: {e}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                name = type(proc).__name__.replace("Processor", " Processor")
                print(f"{name}: total {proc.total} items processed, "
                      f"remaining {len(proc.storage)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            results = []
            for _ in range(nb):
                if not proc.storage:
                    break
                results.append(proc.output())
            plugin.process_output(results)


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = []
        for rank, value in data:
            values.append(value)
        csv_line = ",".join(values)
        print(csv_line)


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = []
        for rank, value in data:
            pairs.append(f'"item_{rank}": "{value}"')
        json_line = "{" + ", ".join(pairs) + "}"
        print(json_line)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors\n")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    data_stream.register_processor(num_proc)
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)
    print("Send first batch of data on stream:,[’Hello world’, "
          "[3.14, -1,2.71], [{’log_level’: ’WARNING’, ’log_message’: "
          "’Telnet access! Use ssh instead’}, {’log_level’: ’INFO’, "
          "’log_message’: ’User wil is connected’}], 42, [’Hi’, ’five’]]")
    stream_data = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected',
            },
        ],
        42,
        ['Hi', 'five'],
    ]
    print()
    data_stream.process_stream(stream_data)
    data_stream.print_processors_stats()

    plugin = CSVPlugin()
    plujin = JSONPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(1, plugin)
    print()
    data_stream.output_pipeline(2, plujin)
    data_stream.print_processors_stats()
