# BESTF
A framework for testing `Arduino` code.

`BESTF` stands for:
1. `BestF` -- Best Framework
2. `Begin`, `End`, `Start`, `True`, `False` -- command names

## Installation
1. Download `FOR_MACRO` from `Alex Gyver` on his github or use the ready-made one
2. Copy the `FOR_MACRO.h`, `bestf.h` and `test_custom_runner.py` to the `test` folder in the root of your `PlatformIO` project
3. Add the line `test_framework = custom` to the `platformio.ini` file
After completing these steps, you will be able to create your tests using this framework

## Macros
### Preparatory
* `TESTS_LIST` -- for listing tests and auto-generating main
* `START` -- for creating a start function
* `STOP` -- to create a stop function
* `NO_START` -- to disable the start function
* `NO_STOP` -- to disable the stop function
* `NO_OTHERS` -- to disable the start and stop functions

### Standard
* `TEST` -- to create a test
* `ASSUME` -- to check a condition
* `END` -- to indicate a successful test completion
* `ABORT` -- to indicate an unsuccessful test completion

### Internal
* `_INTERNAL_STR_` and `_INTERNAL_STR` -- together convert something to a string
* `_INTERNAL_RUN_TEST` -- runs a test

## Other
* `WAIT` -- to wait n seconds

## Examples
### `NO_OTHERS`
```cpp
#include "bestf.h"

NO_OTHERS

TEST(pass)
{
    WAIT(3);
    ASSUME(1 + 1 == 2);
    END;
}

TEST(fail)
{
    ASSUME(1 + 1 == 3);
    END;
}

TEST(fail)
{
    ABORT;
}

TESTS_LIST(pass, fail, abort)
```

### `NO_START`
```cpp
#include "bestf.h"

NO_START

STOP
{
    // Cleanup
}

TEST(pass)
{
    ASSUME(1 + 1 == 2);
    END;
}

TESTS_LIST(pass)
```

### `START' and `STOP`
```cpp
#include "bestf.h"

START
{
    // Init
}

STOP
{
    // Cleanup
}

TEST(pass)
{
    ASSUME(1 + 1 == 2);
    END;
}

TESTS_LIST(pass)
```

## Protocol
### Message format
Message format from `Arduino` to computer: `<First letter of command><Argument 1>;<Argument 2>;...;<Argument n>\n`

### Commands
* `Begin` -- start of testing
* `End` -- end of testing
* `Start` -- start of the test, arguments: test name, file name
* `True` -- the test was successful, passes the line number as an argument
* `False` -- the test was unsuccessful, passes the line number as an argument

## Supplement
### Macros
* `PRINT` -- displays text
* `WEAK_CONFIRM` -- asks for confirmation to continue
* `CONFIRM` -- asks for confirmation to continue
* `SKIP` -- marks the test as skipped
* `_INTERNAL_CONFIRM` -- internal auxiliary function for CONFIRM and WEAK_CONFIRM

### Commands
There is only one command that the supplement adds
* `Debug` -- command addition, passes the argument-subcommand and arguments for the subcommand

#### Sub-commands
* `Skip` -- test is skipped, passes the line number as an argument
* `Print` -- text output, passes the text itself and the line number
* `Confirm (Weak)` -- asks for confirmation to continue execution, passes the line number. After sending, waits for the character `y` or `n`. If `y` is received, continues execution. If `n` is received, sends `Skip`
* `Confirm` -- asks for confirmation to continue execution, passes the line number. After sending, waits for the character `y` or `n`. If `y` is received, continues execution. If `n` is received, sends `Abort`
