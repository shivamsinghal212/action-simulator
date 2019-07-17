import asyncio
import time
import functools

"""
get_running_loop

Return the running event loop in the current OS thread.

If there is no running event loop a RuntimeError is raised. This function can only be called from a coroutine or a 
callback.
"""
# loop = asyncio.get_running_loop()  # only in python 3.6



def function_to_run_async():
    print('Started sleeping...')
    time.sleep(5)
    print('done sleeping...')


def to_do():
    loop = asyncio.get_event_loop()
    print('I am doing something quick!!')
    loop.run_in_executor(None, function_to_run_async)
    print('I am done!!!')
    print(loop)
    loop.call_soon(functools.partial(print, "Hello", flush=False))


to_do()