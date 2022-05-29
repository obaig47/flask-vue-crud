# event-management-app

This application was made with a clone of the application outlined in this tutorial: Check out the [post](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs).

## How to run

1. Run the server-side Flask app in one terminal window:

   ```sh
   $ cd server
   $ python3.9 -m venv env
   $ source env/bin/activate
   (env)$ pip install -r requirements.txt
   (env)$ python app.py
   ```

   Navigate to [http://localhost:5000](http://localhost:5000)

2. Run the client-side Vue app in a different terminal window:

   ```sh
   $ cd client
   $ npm install
   $ npm run serve
   ```

   Navigate to [http://localhost:8080](http://localhost:8080)

- Readme that addresses:

  - [ ] Any relevant instructions on how to run the app
  - [ ] Improvements you’d make if you had additional time
  - [ ] Brief description (no more than a paragraph) on how you’d measure and drive adoption of your app

- To measure and measure adoption of the application, I would attach the Vue app to Google Analytics using `vue-gtag` by the tracking ID. The North Star metric for this simple application, if deployed and containing an Identity and Access management layer, would be number of attendees as well as number of events created. This would be measured via an event handler on the Create Event Button as well as an event handler on the Attended checknox. To drive adoption of this application, I would work closely with product managers to understand the personas and use cases, and then integrate those needs into the application so that the application is clear and easily accessible to the user. A/B testing could be relevant to determine best layout for driving users towards this application.

### Future Features

- Fix dependency issues to remove security issues
- Account login
- Database for persisting data and storing images
- Drill through into an event to more detailed description
- Abbreviated description in table view
- Tagging system
- Naughty strings from mockaroo to test validation
- Move image field to being stored under the title
- Enable recurrance of events for future scheduling
