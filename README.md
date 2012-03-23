Picture-Hanging
===============

[![Build Status](https://secure.travis-ci.org/dvberkel/picture-hanging.png?branch=master)](http://travis-ci.org/dvberkel/picture-hanging)

In [Picture-Hanging Puzzles](http://arxiv.org/abs/1203.3602 "ArXiv page for 'Picture-Hanging Puzzles'")
a famous puzzle, and some of its generalisations are solved using a
words over a free group.

This project offers primitives which enable a developer to express
words over free groups and operate on these words in similiar ways as
expressed in the article.

Free Group
----------

Wikipedia has a nice [article](http://en.wikipedia.org/wiki/Free_group "Wikipedia on Free Groups")
on free groups.

> In mathematics, a group *G* is called **free** if there is a subset *S* of *G*
> such that any element of *G* can be written in one and only one way as
> a product of finitely many elements of *S* and their inverses
> (disregarding trivial variations). Apart from the existence of
> inverses no other relation exists between the generators of a free
> group.

Environment
-----------

Python is used in this project. Make sure that python is able to find
the project. I usually add the current directory to the `PYTHONPATH`
with the following command.

    > export PYTHONPATH=.

### Tests

Execute the following command to run all tests in the project

    > python picture/test/test_all.py

### Executables

To solve a picture hanging puzzle with *n* pins run

    > bin/picture-hanging n