    Vue.component('select-menu', {
        template : `{% include 'wmp/select_menu.html' %}`,

        created() {
                var self = this;
            },

        data: () => ({
          items : [[combo_items|tojson]], // items: ['a','b','c'],
          selected_item: null,
        }),

        methods : {

           test_function: function() {

            var self = this;

               axios.request({
                   method: 'post',
                   url: '/main',
                   data: {
                       'item': self.selected_item,
                   },
                   headers: {
                       'Content-Type': 'application/json'
                   },
                   responseType: 'json'
               })

               .then((response) => {
                   console.log('get success!!');
               })

               .catch(() => {
                    console.log('get err!!');
               })
           },
        }
    });