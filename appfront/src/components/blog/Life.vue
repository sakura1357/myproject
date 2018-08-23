<template>
	<div id="life">
		   <div class="row">
        <div class="col-xs-12 col-sm-8 col-md-9 col-lg-11">
        <div class="panel panel-default">
          <div class="panel-heading">
            随心而记
          </div>
          <div class="panel-body">
            <div class="blog" v-for="blog in blogList">
                  <h3><a href="">{{ blog.fields.blog_title }}</a></h3>
                 <span class="glyphicon glyphicon-tag" aria-hidden="true"></span>
                 <a href="">{{ blog.fields.blog_type }}</a>&nbsp;
                  <span class="glyphicon glyphicon-time" aria-hidden="true"></span>
                  {{ blog.fields.last_updated_time}}<br>
                  <p v-html='blog.fields.excerpt'></p>
            </div>
<!--             <div class="blog">
              <h3>--暂无博客，敬请期待--</h3>
            </div> -->
            <pagination 
              :totalPage="parentTotalPage" 
              :parentCurrentpage="parentCurrentpage" 
              :changeCallback="parentCallback">
            </pagination>
          </div>
        </div>
      </div>
      </div>
	</div>
</template>
<script type="text/javascript">
import pagination from '../base/pagination'
    export default {
      name: 'Life',
      components: {
        pagination
      },
      data () {
        return {
          blogList : [],
          //在data中初始化总页数totalPage，和当前页currentPage
          parentTotalPage: 20,
          parentCurrentpage: 1
        };
      },
      created(){
        this.$ajax.get('http://127.0.0.1:8000/blog/show_blogs_pages/?blog_mark=Life')
        .then(response=>{
          var res = response.data;
          this.blogList = res['list'];
          this.parentTotalPage = res['blog_pages'];
        })
        .catch(error=>{

        });
      },
      methods : {
        getBlogPageList(cPage){
          this.$ajax.get('http://127.0.0.1:8000/blog/show_blogs_pages/?cPage=' + cPage)
          .then(response=>{
            var res = response.data;
            this.blogList = res['list'];
          })
          .catch(error=>{

          });
        },
        //在这里传入pagination的跳转页码回调方法
        //cPage参数是已跳转的当前页码
        parentCallback( cPage )  {
            //这里是页码变化后要做的事
            this.getBlogPageList(cPage);
            //显示的是上一次加载的数据，点击下一页，输出的是上一页的数据，而不是你点击的下一页的数据
            // console.log(this.blogList);
          }
      },
      mounted() {

      } 
    }
</script>
<style scoped>
	

</style>