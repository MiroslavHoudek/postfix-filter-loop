postfix-filter-loop
===================

This is a very simple Python code to achieve Advanced Content Filtering in Postfix ( http://www.postfix.org/FILTER_README.html ) . This Python code listens on one port to get emails from Postfix, then you can do the magic (remove email, change contents) and then re-inject the mail into Postfix. I needed a Python code to do just that, using only standard modules, and absolutely straightforward. So there, get it, configure Postfix, start it, and do whatever you want with headers or body.
