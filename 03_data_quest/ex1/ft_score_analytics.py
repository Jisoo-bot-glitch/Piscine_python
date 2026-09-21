#!usr/bin/python3
import sys

print('=== Player Score Analytics ===')
scores: list[int] = []
for arg in sys.argv[1:]:
    try:
        scores.append(int(arg))
    except ValueError:
        print(f'Invalid parameter: ’{arg}’')

if (scores == []):

    print('No scores provided. ', end="")
    print(f'Usage: python3 {sys.argv[0]} <score1> <score2> ...')
    sys.exit(1)

print(f'Scores processed: {scores}')
print(f'Total players: {len(scores)}')
print(f'Total score: {sum(scores)}')
print(f'Average score: {sum(scores)/(len(scores))}')
print(f'High score: {max(scores)}')
print(f'Low score: {min(scores)}')
print(f'Score range: {max(scores) - min(scores)}')
