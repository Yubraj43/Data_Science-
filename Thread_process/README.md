# Threads vs Processes (Quick Guide)

## Overview
- **Program**: A static file containing instructions.
- **Process**: A running instance of a program (has its own memory and PID).
- **Thread**: A lightweight unit of execution inside a process (shares memory).

## Key Differences
- **Memory**: Processes have separate memory; threads share memory.
- **Speed**: Threads are lighter to create; processes are heavier.
- **Parallelism**: Processes run in true parallel on multi-core; threads in Python are limited by the GIL for CPU tasks.
- **Isolation**: A crash in one process usually does not affect others; threads can affect each other.

## When to Use
- **Use processes** for CPU-heavy tasks (data processing, ML, image/video work).
- **Use threads** for I/O-heavy tasks (network, file reads, web requests).

## This Folder
- `process.py`: Multiprocessing example.
- `Thread.py`: Threading example.
- `webscapping.py`: Threaded web scraping example.

## Run Examples
```powershell
cd c:\Users\mahat\Downloads\Data_Science\Thread_process
python process.py
python Thread.py
python webscapping.py
```

## Notes
- Use `if __name__ == "__main__":` for multiprocessing on Windows.
- Add `flush=True` to `print()` if output seems delayed.
