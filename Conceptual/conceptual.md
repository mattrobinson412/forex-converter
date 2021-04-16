### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

      Some important differences between Python and JavaScript are:  
      * Python is used for web applications and a variety of other apps, including science projects
      * Python has a large standard library to import from
      * Python uses indentation to separate code, not curly braces ({})
      * Python names using snake_case
      * Python has immutable lists called tuples

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  

      1. name_of_dict['c']: 3,
      2. name_of_dict.update({'c': 3})

- What is a unit test?  

      A unit test checks that a single component operates in the right way.

- What is an integration test?

      An integration test checks multiple components to see if they work together.

- What is the role of web application framework, like Flask?

      Web application frameworks allow developers to write Web applications (see WebApplications) or services without having to handle such low-level details as protocols, sockets or process/thread management.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

      URL parameters feel more like “subject of page” scenarios, where URL query parameters feel more like “extra info about page” and are often used when coming from a form.

- How do you collect data from a URL placeholder parameter using Flask?

      You collect data from a URL placeholder param in Flask by storing it as a variable under the same var_name in the app route.

- How do you collect data from the query string using Flask?

      You collect data from the query string in Flask using 'flask.request.args.get()'.

- How do you collect data from the body of the request using Flask?

      By using request.form.

- What is a cookie and what kinds of things are they commonly used for?

      It is a small piece of data stored on the user's computer by the web browser while browsing a website. They're commonly used for storing usernames, passwords, and carts on e-commerce sites.

- What is the session object in Flask?

      Session is a way to store information (in variables) to be used across multiple pages.

- What does Flask's `jsonify()` do?

      jsonify() creates a Response with the JSON representation of the given arguments with an application/json mimetype. 