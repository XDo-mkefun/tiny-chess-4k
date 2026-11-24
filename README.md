# tiny-chess-4k

Strongest chess engine in 4 KB of Python — make.fun tiny-chess-01 entry.

0x88 alpha-beta with quiescence, transposition table and MVV move ordering.
Fixed 40,000-node budget per move, no clock, fully deterministic.
Talks to the env over HTTP (POST /game, /move).
