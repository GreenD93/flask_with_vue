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
                  var color_1st = response.data.color_1st
                  var color_2nd = response.data.color_2nd

                  document.getElementById('blah').src=img_url
                  document.getElementById('color_box_1st').style.backgroundColor=color_1st
                  document.getElementById('color_box_2nd').style.backgroundColor=color_2nd

                  document.getElementById('color_code_1st').innerHTML = color_1st
                  document.getElementById('color_code_2nd').innerHTML = color_2nd
              })

              .catch((err) => {
                  alert('파일 전송에 실패했습니다.');
            })

        },

    }
});