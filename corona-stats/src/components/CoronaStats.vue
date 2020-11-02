<template>
  <div class="mx-9">
    <v-data-table
      dense
      fixed-header
      v-model="selected"
      item-key="dataset"
      loading-text="Loading US Corona Virus Statistics..."
      :headers="headers"
      :items="results"
      :options.sync="options"
      :loading="loading"
      :items-per-page="defaultPageSize"
      show-select
      multi-sort
      class="mt-2 elevation-5"
      :footer-props="footerProps"
      >
    <template v-slot:top="{ pagination, options, updateOptions }">
        <v-data-footer
          :pagination="pagination"
          :options="options"
          @update:options="updateOptions"
          firstIcon="mdi-arrow-collapse-left"
          lastIcon="mdi-arrow-collapse-right"
          prevIcon="mdi-chevron-left"
          nextIcon="mdi-chevron-right"
          :items-per-page-options="pageSizeOptions"
          items-per-page-text="$vuetify.dataTable.itemsPerPageText"/>
      </template>
    </v-data-table>
  </div>
</template>

<script>
  import axios from 'axios'
  import moment from 'moment'
  export default {
    name: 'CoronaStats',
    props: {
      pageSizeOptions: {
        type: Array,
        default: () => [50, 100, 200, 500, 1000, 5000]
      },
      defaultPageSize: {
        type: Number,
        default: 500
      }
    },
    data () {
      return {

        /* Grid stuff */
        selected: [],
        totalResults: 0,
        results: [],
        loading: true,
        options: {},
        footerProps: {
          firstIcon: 'mdi-arrow-collapse-left',
          lastIcon: 'mdi-arrow-collapse-right',
          prevIcon: 'mdi-chevron-left',
          nextIcon: 'mdi-chevron-right',
          'items-per-page-options': this.pageSizeOptions
        },
        headers: [
          {
            text: 'Dataset',
            align: 'start',
            sortable: true,
            value: 'data_set_name'
          },
          { text: 'State Name', value: 'state' },
          { text: 'Updated', value: 'updated' },
          { text: 'Total Cases', value: 'cases' },
          { text: 'Cases Today', value: 'casesToday' },
          { text: 'Total Deaths', value: 'deaths' },
          { text: 'Deaths Today', value: 'deathsToday' },
          { text: 'Recovered Cases', value: 'recovered' },
          { text: 'Active Cases', value: 'active' },
          { text: 'Cases Per Million', value: 'Cases Per Million' },
          { text: 'Deaths Per Million', value: 'deathsPerMillion' },
          { text: 'Total Tests', value: 'tests' },
          { text: 'Tests Per Million', value: 'testsPerMillion' },
          { text: 'Total Population', value: 'pop' },
        ]
      }
    },
    mounted () {
      this.getDataFromApi()
        .then(data => {
          this.results = data.items
          this.totalResults = data.total
        })
    },
    methods: {
      formatDate (value) {
        return moment(value).format('YYYY-MM-DD HH:mm:ss')
      },
      getDataFromApi () {
        this.loading = true
        return new Promise((resolve) => {

        let items
        let total

        axios
          .get('http://127.0.0.1:8000/all_states', {
            params: {
            }
          })
          .then(response => {
            total = response.data.length
            items = response.data
          })
          .catch(error => {
            console.log(error)
          })
          .finally(() => {
            this.loading = false
            resolve({
              items,
              total
            })
          })
        })
      }
    }
  }


</script>
