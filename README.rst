Scrapy website
==============

This is the website that runs on https://scrapy.org.

Requirements
============

This website is made with `Jekyll`_. The most universal way to install it is::

    gem install jekyll

Usage
=====

To start the web server locally auto-reloading when files change use::

    jekyll serve --watch

The website is updated via the `Travis build`_ when merging to the gh-pages branch.

.. _Travis build: https://travis-ci.org/scrapy/scrapy.org

Adding your company to the website
==================================

Are you a company or individual using Scrapy for your product or project? Add
yourself to the "Companies using Scrapy" list in ``companies.html`` and send a
pull request!


Are you providing Scrapy consulting?
------------------------------------
If you are a company providing Scrapy consulting or spider development, you 
can submit a pull request to add your company to the "Scrapy Pros" list in
``companies.html``.

The companies are sorted by their overall contribution to the Scrapy project
and ecosystem. There's a small process to manage that::

1. In order to appear in the list, a company must score at least five points
   in the table below.
2. The company must submit an issue to 
   `scrapy.org repo <https://github.com/scrapy/scrapy.org/>`_ whenever they want
   to update their contributions and ranking.
3. This issue must contain references to all the contributions that the company
   made since the last time their rank has been updated.

This is the criteria that will be used:

+----------------------------------------------------------------------+--------+
| Contribution                                                         | Points |
+======================================================================+========+
| Pull request accepted in scrapy repo                                 |   50   |
+----------------------------------------------------------------------+--------+
| Creation or contribution to public Scrapy plugins                    |   20   |
+----------------------------------------------------------------------+--------+
| Instructional materials such as screencasts, tutorials or blog posts |   10   |
+----------------------------------------------------------------------+--------+
| Blog posts that spread the word about Scrapy                         |    5   |
+----------------------------------------------------------------------+--------+
| Landing page in the company website describing the Scrapy services   |    2   |
+----------------------------------------------------------------------+--------+
| Scrapy listed in the company's technologies stack (if any)           |    2   |
+----------------------------------------------------------------------+--------+
| Answer to StackOverflow question regarding Scrapy                    |    1   |
+----------------------------------------------------------------------+--------+

.. _Jekyll: http://jekyllrb.com/
