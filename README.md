# event-management-app

This application was adapted from a fork of the application outlined in this tutorial written by [Michael Herman](https://github.com/mjhea0): Check out the [post](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs).

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

## Measuring and Driving Adoption

- To measure adoption of the application, `vue-gtag` can be leveraged by sending event data to Google Analytics using a tracking ID. The North Star metric for this simple application could be number of events created. This would be measured via an event handler on the "Add Event" Button. Other useful metrisc relating to click-through rate and site usage can be gained from `vue-gtag` if this application were integrated into a larger set of applications. To drive adoption of this application, I would work closely with the product team to understand the personas/use cases, and then iteratively integrate those needs into the application. A/B testing could be used to determine layout decisions. Based on the analytics data and results of testing, improvements can be made to drive adoption and improve utility.

### Future Improvements
- Update dependencies to resolve security vulnerabilities
- Add sort using b-table
- Add identity and access layer for supporting multiple users
- Add homepage which serves as Map of Concepts (relating to Events) for drill through
- Add Attending/RSVP, event description, event tags, truncated description
- Add Database layer
- Add file browse for images
- Add recurring of events for future scheduling
- Test "Naughty strings" to improve validation
