## Systems Bibliography

This repository contains an annotated bibliography that I've built from my readings in computer systems research.

### Contents

At the top-level, I partition papers among the following categories:

- [Cloud Computing](./cloud-computing/)
- [Database Systems](./database-systems/)
- [Programming Languages](./programming-languages/)
- [Storage Systems](./storage-systems/)

For a particular paper, the line between some of these categories can be blurry. In such cases I make my best effort to categorize the paper in its logical section.

### Schema

The current schema I use for recording notes about a particular paper is described below.

**Metadata**

This is general metadata about the paper, including:
- Title
- Publication year
- Author(s)

**Big Idea**

This is a short (typically one sentence description) of the primary takeaway from the paper.

**Summary**

This is a summary of the main points of the paper. When I find particular technical details interesting, they will also appear in this section. I try to ensure that the information in this section is a relatively-objective summary of the paper's contents (i.e. it does not contain too much of my own commentary).

**Commentary**

These are my personal thoughts on particular aspects of the paper, recorded as I am reading it. The ideas in this section tend to be much more subjective than those in the _Summary_ section. Furthermore, the contents of this section also tend to be written more hastily and therefore may lack relevant context.

**Questions**

These are questions that I am left with upon completing the paper.

**Further Reading**

These are papers that I make note of while scanning the paper's references. Many times I use the contents of the _Further Reading_ section to inform my decisions on the papers I will read next.

### Staying Organized

Maintaining this bibliography in Markdown has its benefits and drawbacks. I find authoring in Markdown extremely satisfying - it is quick to write, and it renders in a clean, readable format with support for code blocks with syntax highlighting. However, it also means that many features are missing, like built-in support for a table of contents.

In order to stay organized, I wrote a little script ([`src/update.py`](./_src/update.py)) that regenerates the index page for each top-level section of the bibliography. To simplify things further, I provide a `Makefile` target to regenerate the index for each section:

```bash
make regen
```

Run this after the addition of any page to keep all indexes up-to-date.
