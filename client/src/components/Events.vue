<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Events</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.event-modal>
          Add Event
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Date</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(event, index) in events" :key="index">
              <td>{{ event.title }}</td>
              <td>{{ event.author }}</td>
              <td>{{ event.date }}</td>
              <td>
                <span v-if="event.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.event-update-modal
                          @click="editEvent(event)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteEvent(event)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- EVENT ENTRY MODAL -->
    <b-modal ref="addEventModal"
            id="event-modal"
            title="Add a new event"
            hide-footer>
      <!-- EVENT ENTRY FORM START -->
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">

      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addEventForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>

        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addEventForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-date-group"
                      label="Date:"
                      label-for="form-date-input">
          <b-form-input id="form-date-input"
                          type="date"
                          v-model="addEventForm.date"
                          required
                          placeholder="Enter date">
            </b-form-input>
          </b-form-group>

        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addEventForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>

      </b-form>

    </b-modal>
    <b-modal ref="editEventModal"
            id="event-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      events: [],
      addEventForm: {
        title: '',
        author: '',
        date: '',
        read: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        author: '',
        date: '',
        read: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getEvents() {
      const path = 'http://localhost:5000/events';
      axios.get(path)
        .then((res) => {
          this.events = res.data.events;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addEvent(payload) {
      const path = 'http://localhost:5000/events';
      axios.post(path, payload)
        .then(() => {
          this.getEvents();
          this.message = 'Event added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getEvents();
        });
    },
    initForm() {
      this.addEventForm.title = '';
      this.addEventForm.author = '';
      this.addEventForm.date = '';
      this.addEventForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.date = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addEventModal.hide();
      let read = false;
      if (this.addEventForm.read[0]) read = true;
      const payload = {
        title: this.addEventForm.title,
        author: this.addEventForm.author,
        date: this.addEventForm.date,
        read, // property shorthand
      };
      this.addEvent(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addEventModal.hide();
      this.initForm();
    },
    editEvent(event) {
      this.editForm = event;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editEventModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        date: this.editForm.date,
        read,
      };
      this.updateEvent(payload, this.editForm.id);
    },
    updateEvent(payload, eventID) {
      const path = `http://localhost:5000/events/${eventID}`;
      axios.put(path, payload)
        .then(() => {
          this.getEvents();
          this.message = 'event updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getEvents();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editEventModal.hide();
      this.initForm();
      this.getEvents(); // why?
    },
    removeEvent(eventID) {
      const path = `http://localhost:5000/events/${eventID}`;
      axios.delete(path)
        .then(() => {
          this.getEvents();
          this.message = 'Event removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getEvents();
        });
    },
    onDeleteEvent(event) {
      this.removeEvent(event.id);
    },
  },
  created() {
    this.getEvents();
  },
};
</script>
