Vue.component('color-box', {
    template : `{% include 'wmp/color_box.html' %}`,

    created() {
        var self = this;
    },

    data: () => ({
        selected_deal_id: null,
        tweenedCSSColor : '',
        image_url: null,
    }),

    methods: {

        extract_color: function(){

            var self = this;
            // color_box img input 미리보기 코드...
            // var formData = new FormData();
            // formData.append('file', document.getElementById('upload_img').files[0]);

              axios.request({
                method: 'post',
                url: './extract_color',
                data: {
                        'deal_id': self.selected_deal_id
                    },
                headers: {
                    'Content-Type': 'application/json'
                },
              })

              .then((response) => {
                  var img_url = response.data.img_url
                  var dominant_color = response.data.color

                  document.getElementById('blah').src=img_url
                  document.getElementById('color_box').style.backgroundColor=dominant_color
                  document.getElementById('color_code').innerHTML = dominant_color
              })

              .catch((err) => {
                  alert('파일 전송에 실패했습니다.');
            })

        },

    }
});