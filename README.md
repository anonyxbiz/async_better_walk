# async_better_walk

Welcome to `async_better_walk`, the library that offers you a better way to walk through directories without the risk of crashing your app. If you've ever used `os.walk()` and felt your application trembling at the thought of handling large directories, then this is the solution you've been waiting for! 

## Features

- **Asynchronous**: Finally, a library that lets you browse files like you’re strolling through a park — non-blocking and leisurely!
- **Super Fast**: Files appear as quickly as your brain can process them. No more waiting for eternity just to find that one file you know is hiding somewhere!
- **No Dependencies**: Built entirely with Python’s inbuilt libraries, so you can save the install time for something more important.

## Installation

You can install the package using pip or clone the repository.

```bash
pip install git+https://github.com/anonyxbiz/async_better_walk.git
```

## Usage

Here’s a quick example of how to use `async_better_walk`:

```python
from async_better_walk import Os
from asyncio import run

async def main():
    dir = "/path/to/directory"  # Point this to the directory you want to explore
    app = await Os.init(dir=dir)  # Asynchronously initialize the class instance.
    
    # Stream chunks of files without causing your app to break!
    async for file in app.walk(1024):
        print(file)

if __name__ == "__main__":
    run(main())
```

## API Reference

### `Os.init(dir: str)`
Asynchronously sets up the class instance and the directory to be walked upon, then returns the class instance. (P.S. Yes, it’s still alive and kicking!)

### `Os.walk(bytes: int)`

Asynchronously walks through the specified directory, with a maximum chunksize as specified, yielding file paths as they are found.

- **Parameters**:
  - `bytes`: The maximum chunksize to use (because we’re not about to choke on data).
- **Returns**: An asynchronous generator that yields file paths (think of it as a file buffet!)

### `Os.bash(cmd: str)`

Executes a shell command asynchronously and yields output as it becomes available.

- **Parameters**:
  - `cmd`: The shell command to asynchronously execute (you say "bash," we say "yes, please!").
- **Returns**: An asynchronous generator that yields command output.

## Logging

This library uses logging to keep you informed about what’s happening under the hood. You can configure the logger as needed, because who doesn’t love a little drama in their logs?

## Contributing

We welcome contributions! If you find a bug, have a suggestion, or just want to say hi, please open an issue or submit a pull request. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was born out of a desire to create an efficient asynchronous file walking solution. Let’s face it, we all want to avoid crashing our apps like they’re made of glass!