Scrapy website
==============

This is the website that runs on https://scrapy.org.

Basic Requirements
============

This website is made with `Jekyll`_. The most universal way to install it is::

    bundle install

Usage
=====

To start the web server locally auto-reloading when files change use::

    jekyll serve --watch

The website is updated via the `Travis build`_ when merging to the ``master`` branch.

.. _Travis build: https://travis-ci.org/scrapy/scrapy.org

Adding your company to the website
==================================

Are you a company or individual using Scrapy for your product or project? Add
yourself to the "Companies using Scrapy" list by sending a pull request:

- add a "company card" in ``_data/companies/list/<companyslug>.yml`` as a YAML file;
  you need to set a few fields: a name, a "logouser" for your logo filename,
  a homepage and a blurb in markdown syntax on how you're using Scrapy.
  Do add links to any article or tweet spreading your love of Scrapy
- add your logo to ``img/``
- add the slug of your company card to the list in ``_data/companies/users.yml``.


Are you providing Scrapy consulting?
------------------------------------
If you are a company providing Scrapy consulting or spider development, you
can submit a pull request to add your company to the "Scrapy Pros" list.

The companies are sorted by their overall contribution to the Scrapy project
and ecosystem. There's a small process to manage that:

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

In practice, to be listed, you'll need to:

- add/update your "company card" in ``_data/companies/list/<companyslug>.yml``
  as a YAML file;
  it needs a ``url`` field (e.g. the landing page of your consulting services offer),
  a ``description`` field describing your services (use markdown),
  and a ``logo`` filename
- add your logo to ``img/``
- add/update your contributions in ``_data/companies/pros/contributions.csv``
- re-run ``update_ranking.py`` inside ``_data/companies/pros/``

and send a pull request with these changes.

.. _Jekyll: http://jekyllrb.com/
