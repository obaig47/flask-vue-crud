<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <alert
          v-if="showMessage"
          :message="message"
        />
        <button
          v-b-modal.event-modal
          type="button"
          class="btn btn-success btn-sm"
        >
          Add Event
        </button>
        <br><br>
        <b-table-simple
          striped
          hover
          :items="events"
          :fields="fields"
        >
          <template #cell(read)="{ event }">
            <span>
              <div
                class="btn-group"
                role="group"
              >
                <b-btn
                  v-b-modal.event-update-modal
                  type="button"
                  class="btn btn-warning btn-sm"
                  @click="editEvent(event)"
                >
                  Update
                </b-btn>
              </div></span>
          </template>
        </b-table-simple>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">
                Title
              </th>
              <th scope="col">
                Image
              </th>
              <th scope="col">
                Date
              </th>
              <th scope="col">
                Read?
              </th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(event, index) in events"
              :key="index"
            >
              <td>{{ event.title }}</td>
              <td>{{ event.image }}</td>
              <td>{{ event.date }}</td>
              <td>
                <span v-if="event.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div
                  class="btn-group"
                  role="group"
                >
                  <button
                    v-b-modal.event-update-modal
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="editEvent(event)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteEvent(event)"
                  >
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
    <b-modal
      id="event-modal"
      ref="addEventModal"
      title="Add a new event"
      hide-footer
    >
      <!-- EVENT ENTRY FORM START -->
      <b-form
        class="w-100"
        @submit="onSubmit"
        @reset="onReset"
      >
        <b-form-group
          id="form-title-group"
          label="Title:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="addEventForm.title"
            type="text"
            required
            placeholder="Enter title"
          />
        </b-form-group>

        <b-form-group
          id="form-image-group"
          label="Image:"
          label-for="form-image-input"
        >
          <b-form-input
            id="form-image-input"
            v-model="addEventForm.image"
            type="text"
            required
            placeholder="Enter image"
          />
        </b-form-group>

        <b-form-group
          id="form-date-group"
          label="Date:"
          label-for="form-date-input"
        >
          <b-form-input
            id="form-date-input"
            v-model="addEventForm.date"
            type="date"
            required
            placeholder="Enter date"
          />
        </b-form-group>

        <b-form-group id="form-read-group">
          <b-form-checkbox-group
            id="form-checks"
            v-model="addEventForm.read"
          >
            <b-form-checkbox value="true">
              Read?
            </b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-button-group>
          <b-button
            type="submit"
            variant="primary"
          >
            Submit
          </b-button>
          <b-button
            type="reset"
            variant="danger"
          >
            Reset
          </b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal
      id="event-update-modal"
      ref="editEventModal"
      title="Update"
      hide-footer
    >
      <b-form
        class="w-100"
        @submit="onSubmitUpdate"
        @reset="onResetUpdate"
      >
        <b-form-group
          id="form-title-edit-group"
          label="Title:"
          label-for="form-title-edit-input"
        >
          <b-form-input
            id="form-title-edit-input"
            v-model="editForm.title"
            type="text"
            required
            placeholder="Enter title"
          />
        </b-form-group>
        <b-form-group
          id="form-image-edit-group"
          label="Image:"
          label-for="form-image-edit-input"
        >
          <b-form-input
            id="form-image-edit-input"
            v-model="editForm.image"
            type="text"
            required
            placeholder="Enter image"
          />
        </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group
            id="form-checks"
            v-model="editForm.read"
          >
            <b-form-checkbox value="true">
              Read?
            </b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button
            type="submit"
            variant="primary"
          >
            Update
          </b-button>
          <b-button
            type="reset"
            variant="danger"
          >
            Cancel
          </b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  components: {
    alert: Alert,
  },
  data() {
    return {
      // Note 'isActive' is left out and will not appear in the rendered table
      fields: [
        {
          key: 'title',
          sortable: false,
        },
        {
          key: 'image',
          sortable: false,
        },
        {
          key: 'date',
          sortable: true,
          // Variant applies to the whole column, including the header
          // and footer
        },
        {
          key: 'read',
          sortable: false,
          // Variant applies to the whole column, including the header
          // and footer
        },
      ],
      events: [],
      addEventForm: {
        title: '',
        image: '',
        date: '',
        read: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        image: '',
        date: '',
        read: [],
      },
    };
  },
  created() {
    this.getEvents();
  },
  methods: {
    getEvents() {
      const path = 'http://localhost:5000/events';
      axios
          .get(path)
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
      axios
          .post(path, payload)
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
      this.addEventForm.image = '';
      this.addEventForm.date = '';
      this.addEventForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.image = '';
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
        image: this.addEventForm.image,
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
        image: this.editForm.image,
        date: this.editForm.date,
        read,
      };
      this.updateEvent(payload, this.editForm.id);
    },
    updateEvent(payload, eventID) {
      const path = `http://localhost:5000/events/${eventID}`;
      axios
          .put(path, payload)
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
      axios
          .delete(path)
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
};
</script>
