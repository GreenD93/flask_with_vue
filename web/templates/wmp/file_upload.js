Vue.component('file-upload', {
    template : `{% include 'wmp/file_upload.html' %}`,

    created() {
        var self = this;
    },

   methods: {

        upload: function(){
            alert('working');
            var data = new FormData();
              data.append('file', document.getElementById('file').files[0]);

              axios.request({
                  method: 'post',
                  url: './upload',
                  data: data
              })

              .then((response) => {
                  alert('파일 전송에 선공했습니다.');
                  console.log(response);
              })

              .catch((err) => {
                  alert('파일 전송에 실패했습니다.');
            })
        }
    }

});