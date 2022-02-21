# Overview

<b>safe_cracker</b> provides basic dictionary and brute force attacks on password-protected files

The following file types are supported:<br>
* ZIP
* Excel workbooks

<b>DISCLAIMER: This software is for educational purposes only. This software should not be used for illegal activity. The author is not responsible for its use.</b>

# Quickstart

See the examples directory for more details. For instance, you can crack a really easy ZIP with the following:<br>
<code>python -m examples.example_01_mask_xt</code>

# Installation

Install the required dependencies with the following:<br>
<code>python -m pip install -r requirements.txt</code>

# Why?

I liked the idea of a safecracker, given a specific toolset, can attempt to crack any safe. I coded all of the like-classes similarly so that we can flexibly swap them in and out.

Beyond that, I mostly just wanted a fun little project to play with:
* dictionary and mask attacks
* threading, generators, and tqdm
* chunking large generators

I also sleep better knowing I can recover passwords for long-forgotten files!

# Resources
* <b>Attacks</b>
	* Dictionary Attack Example<br>
	[https://www.thepythoncode.com/article/crack-zip-file-password-in-python](https://www.thepythoncode.com/article/crack-zip-file-password-in-python)
		* rockyou Dictionary<br>
		[https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
	* Mask (Brute-Force) Attack Example<br>
	[https://github.com/kamil1marczak/ZIP-file-Dynamic-Multi-Threads-Bruteforce-Password-Cracker-in-Python/blob/master/zip_cracker.py](https://github.com/kamil1marczak/ZIP-file-Dynamic-Multi-Threads-Bruteforce-Password-Cracker-in-Python/blob/master/zip_cracker.py)
* <b>Threading</b>
	* Threading with Keyboard Interrupt<br>
	[https://gist.github.com/clchiou/f2608cbe54403edb0b13](https://gist.github.com/clchiou/f2608cbe54403edb0b13)
	* Threading with Stop Condition<br>
	[https://stackoverflow.com/questions/59764657/python-concurrency-threadpoolexecutor-stop-execution-if-condition-is-met](https://stackoverflow.com/questions/59764657/python-concurrency-threadpoolexecutor-stop-execution-if-condition-is-met)
	* Cancelling Unnecessary Futures<br>
	[https://stackoverflow.com/questions/29177490/how-do-you-kill-futures-once-they-have-started](https://stackoverflow.com/questions/29177490/how-do-you-kill-futures-once-they-have-started)
* <b>tqdm</b>
	* tqdm with concurrent.futures<br>
	[https://gist.github.com/alexeygrigorev/79c97c1e9dd854562df9bbeea76fc5de](https://gist.github.com/alexeygrigorev/79c97c1e9dd854562df9bbeea76fc5de)
* <b>Other</b>
	* Strong Password Generator<br>
	[https://passwordsgenerator.net/](https://passwordsgenerator.net/)
	* Chunking a Generator<br>
	[https://stackoverflow.com/questions/24527006/split-a-generator-into-chunks-without-pre-walking-it](https://stackoverflow.com/questions/24527006/split-a-generator-into-chunks-without-pre-walking-it)

# Warranty

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Roadmap

* add support for multithreading using pythoncom for Excel safes<br>
[https://stackoverflow.com/questions/26764978/using-win32com-with-multithreading](https://stackoverflow.com/questions/26764978/using-win32com-with-multithreading)