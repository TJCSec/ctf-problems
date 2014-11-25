The goal of this problem is to see the comment about asking for help on the internet, and search for the post, Steve Katz is mentioned, and sure enough Steve Katz posted on Stack Overflow about an issue with this very application, and accidentally included the app's secret key. Since the decision whether to show the flag or not depends on if `session['loggedin'] == True`, the user can then fake the session variable to say so.

The /login route is a red herring.
