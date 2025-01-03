import subprocess
import os

# Shittiest testing framework?
class Test:
    def __init__(self, path, name, success_on_failure=False):
        self.SUCCESS = 0
        self.FAILURE = 1
        self.test_name = name
        self.executable_path = path
        self.success_on_failure = success_on_failure
        print("[*] Test " + self.test_name + ": Created. Command: " + self.executable_path + ". Success on failure: " + str(self.success_on_failure))
    def start(self, args=None, env=None):
        print("[*] Test " + self.test_name + ": starting process")
        self.process = subprocess.Popen([self.executable_path] + (args if args is not None else []), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=(env if env else os.environ))
    def input(self, input, success_on_failure=None):
        buffer = self.success_on_failure
        if success_on_failure:
            self.success_on_failure = success_on_failure
        stdout, stderr = self.process.communicate(input=input)
        if stderr:
            if not self.success_on_failure:
                print("[-] Test " + self.test_name + ": Error upon sending input: " + stderr)
                self.success_on_failure = buffer
                return self.FAILURE, stderr, stdout
            else:
                print("[+] Test " + self.test_name + ": Input successfully errored: " + stderr)
                self.success_on_failure = buffer
                return self.SUCCESS, stderr, stdout
        else:
            if not self.success_on_failure:
                print("[+] Test " + self.test_name + ": Input successful: " + stdout)
                self.success_on_failure = buffer
                return self.SUCCESS, stderr, stdout
            else:
                print("[+] Test " + self.test_name + ": Error upon sending input: " + stdout)
                self.success_on_failure = buffer
                return self.FAILURE, stderr, stdout
    def close(self):
        return_code = self.process.returncode
        if return_code == 0:
            print("[*] Test " + self.test_name + ": Info: Process ended. Status: success")
            return self.SUCCESS, return_code
        else:
            print("[*] Test " + self.test_name + ": Info: Process ended. Status: failure. Code: " + str(return_code))
            return self.FAILURE, return_code

math = Test("./math", "math.cpp")

print("Test 1 - calculation")
math.start()
status, _stderr, stdout = math.input("4\n")
if not status == math.SUCCESS:
    print("Error: input attempt returned failure condition")
    exit(1)
if "50.24" not in stdout:
    print("Error: calculation was incorrect")
    exit(1)
math.close()

print("Test 2 - invalid input")
math.start()
status, _stderr, _stdout = math.input("text\n", success_on_failure=True)
if not status == math.SUCCESS:
    print("Error: input attempt returned failure condition")
    exit(1)
math.close()

ctof = Test("./ctof/ctof", "ctof.cpp")

print("Test 1 - C to F calculation")
ctof.start(env=dict(os.environ, **{"LD_LIBRARY_PATH":"./ctof"}), args=["-cf"])

status, _stderr, stdout = ctof.input("20\n")
if not status == ctof.SUCCESS:
    print("Error: input attempt returned failure condition")
    exit(1)
if "68" not in stdout:
    print("Error: calculation was incorrect")
    exit(1)
ctof.close()

print("Test 2 - invalid input")
ctof.start(env=dict(os.environ, **{"LD_LIBRARY_PATH":"./ctof"}), args=["-cf"])
status, _stderr, _stdout = ctof.input("text\n", success_on_failure=True)
if not status == ctof.SUCCESS:
    print("Error: input attempt returned failure condition")
    exit(1)
ctof.close()

print("Test 3 - F to C calculation")
ctof.start(env=dict(os.environ, **{"LD_LIBRARY_PATH":"./ctof"}), args=["-fc"])

status, _stderr, stdout = ctof.input("68\n")
if not status == ctof.SUCCESS:
    print("Error: input attempt returned failure condition")
    exit(1)
if "20" not in stdout:
    print("Error: calculation was incorrect")
    exit(1)
ctof.close()
