<p align="center">
<img width="750" alt="logo_750" src="https://github.com/user-attachments/assets/ad687a4d-8abe-4c60-bf89-6a24a04f447c" />
<br/>
<a href=https://pypi.org/project/mansnip><img src=https://badge.fury.io/py/mansnip.svg/></a>  
</p>

When LLMs use the Internet instead of the local documentation on the computer its running on, they make all kinds of mistakes: compatibility and deprecated usage, missing obvious things. 

context7 fixes this only for things in context7. What about everything else? 

Get your models to use the right documentation, locally, for the software you actually have, effeciently.

**Mansnip**, part of the [DAY50](https://day50.dev) suite of open-source tools for AI workflows, solves the problem of irrelevant documentation going to the context window.

You can intelligently put only the parts of manpages you care about into your context window:

```bash
$ uvx mansnip --llm bash bind
```

And your terminal window:

```bash
$ uvx mansnip bash bind
```

Compare the token cost of various approaches for finding the documentation for bash's complete command: 

```bash
$ man bash | token-count                            # whole page
73392
$ man bash | grep -C 3 complete | token-count       # naive approach with a bunch of garbage input
8833
$ mansnip bash complete | token-count               # mansnip without llm feature
2908
$ mansnip --llm bash complete | token-count         # with llm compaction!
1624
```
That's a 98% reduction! Sweet.

There's also a ready-to-go MCP server for it in `mcp-server.py`. 

Just `pip/pipx/uv tool install mansnip`

## My classic 2020 pitch below!

<p align="center">



https://github.com/user-attachments/assets/1fb76ac3-54e7-48dd-b349-4c7fa89016c6


["As seen on YouTube!"](https://www.youtube.com/watch?v=3GT1J-ejM3Q)
</p>

----

**Don't you hate** wasting time navigating through manpages with the leading pager's clunky search tools?

Ever try to find things like the "declare" built-in in `bash(1)` only to slodge through the results using the 'n' key going 'nope, nope, nope'? 

![the old way](https://9ol.es/animate.gif)

Stop wasting time with the old way of manually stumbling through manuals. Say goodbye to these problems once and for all!

**Finally there's a better way!**

## Introducting Mansnip! 

Mansnip is a revolutionary way to navigate through manpages, a tool that no terminal should be without!

It intelligently searches through manpages and outputs the snippets relevant to your query as self-contained browsable sections. 
Simply use it the way you use man, at the command line, followed by your search term(s).

Watch how mansnip can immediately find `bash(1)'s` declare without any extra effort:

![mansnip is amazing](https://9ol.es/msfade.png)

Mansnip works on any manpage.

**With mansnip** you'll just zip through documentation, saving precious time so you can write GitHub readmes like you're trying to sell Ginsu steak knives.

See how mansnip obediently shows everything with a "-z" option in the 25,888 lines of the [zshall manpage](http://gsp.com/cgi-bin/man.cgi?section=1&topic=zshall) on a single screen, all at once, in an easy-to-read manner.

![zshall for all](https://9ol.es/mansnip.png)

But wait, there's more! You'll also get the line number and hierarchical context totally free!

*We're still not finished yet!*

You'll also get to install it easily [through pypi](https://pypi.org/project/mansnip/). 

Here's how do it 

`$ pip3 install mansnip` 

Act now, servers are standing by.

![mansnip](https://9ol.es/man1.jpg)

ＦＡＤＥ ＴＯ  ＢＬＡＣＫ

ＥＮＤ ＳＣＥＮＥ

---

Want more? Here's some [background](background.md) 
