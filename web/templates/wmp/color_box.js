Vue.component('color-box', {
    template : `{% include 'wmp/color_box.html' %}`,

    created() {
        var self = this;
    },

    data: () => ({
        tweenedCSSColor : '#37B400'
    }),

    methods: {

    }
});