## Updates for the AI era!

You can now intelligently mansnip into your context window by setting an environment variable like this:

```bash
$ MANSNIP_LLM=1 mansnip ...
```

This will do a variety of things (try it yourself) that optimize for minimal token-length when using an llm. 

Compare various approaches for finding the documentation for bash's complete command: 

```bash
$ man bash | token-count                            # whole page
73392
$ man bash | grep -C 3 complete | token-count       # naive approach with a bunch of garbage input
8833
$ mansnip bash complete | token-count               # mansnip without llm feature
2908
$ MANSNIP_LLM=1 mansnip bash complete | token-count # with new llm compaction!
1624
```
That's a 98% reduction! Sweet.

Just `pip install mansnip-kristopolous`

## My classic 2020 pitch below!

<p align="center">
  
[![Video](https://9ol.es/vid.jpg)](http://www.youtube.com/watch?v=3GT1J-ejM3Q)

> "As seen on YouTube!" (click image, it's only 1min 45sec)
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

You'll also get to install it easily [through pypi](https://pypi.org/project/mansnip-kristopolous/). 

Here's how do it 

`$ pip3 install mansnip-kristopolous` 

Act now, servers are standing by.

![mansnip](https://9ol.es/man1.jpg)

ＦＡＤＥ ＴＯ  ＢＬＡＣＫ

ＥＮＤ ＳＣＥＮＥ

---

Want more? Here's some [background](background.md) 
