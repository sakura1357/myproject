<template>
	<div id="home">
		  <div class="row">
<!--         <ul v-for="blog in blogList">
          <li>标题：  blog.fields.title }}</li>
          <li>作者：{{ blog.fields.author }}</li>
          <li>类型：{{ blog.fields.blog_type }}</li>
          <li v-html='"摘要：" + blog.fields.excerpt'></li>
          <li>创建时间：{{ blog.fields.created_time }}</li>
          <li>最后更新时间：{{ blog.fields.last_updated_time }}</li>
        </ul> -->
        <div class="col-xs-12 col-sm-8 col-md-9 col-lg-11">
        <div class="panel panel-default">
          <div class="panel-heading">
            首页
          </div>
          <div class="panel-body">
            <div class="blog" v-for="blog in blogList">
                  <h3><a href="">{{ blog.fields.title }}</a></h3>
                 <span class="glyphicon glyphicon-tag" aria-hidden="true"></span>
                 <a href="">{{ blog.fields.blog_type }}</a>&nbsp;
                  <span class="glyphicon glyphicon-time" aria-hidden="true"></span>
                  {{ blog.fields.last_updated_time}}<br>
                  <p v-html='blog.fields.excerpt'></p>
            </div>
<!--             <div class="blog">
              <h3>--暂无博客，敬请期待--</h3>
            </div> -->
            <pagination :totalPage="parentTotalPage" :currentPage="parentCurrentpage" :changeCallback="parentCallback"></pagination>

          </div>
        </div>

      </div>
      </div><!-- /.row -->
	</div>
</template>
<script type="text/javascript">
  import pagination from '../base/pagination'
    export default {
      name: 'home',
      components: {
        pagination
      },
      data () {
        return {
          blogList : [],
          msg : "Update your data here.",
          //在data中初始化总页数totalPage，和当前页currentPage
          parentTotalPage: 20,
          parentCurrentpage: 1
        };
      },
      created(){
        // this.$ajax.get('http://127.0.0.1:8000/blog/show_blogs/?blog_mark=Tech')
        this.$ajax.get('http://127.0.0.1:8000/blog/show_blogs/')
        .then(response=>{
          var res = response.data;
          this.blogList = res['list'];
          // console.log(res);
          this.parentTotalPage = Math.ceil(res.total_count/5);
          console.log(this.parentTotalPage);
        })
        .catch(error=>{

        });
      },
      methods : {
        getBlogPageList(){
          this.$ajax.get('http://127.0.0.1:8000/blog/show_blogs/?')
          // this.$ajax.get('http://127.0.0.1:8000/blog/show_blogs/')
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
            this.msg = 'Update your data here. Page: ' + cPage;

          }
      },
      mounted() {

      } 
    }
</script>
<style scoped>
ul.blog-types {
  list-style-type: none;
}
/** div.blog:not(:last-child) 不是最后一个元素的其余元素使用如下的样式 **/
div.blog:not(:last-child) {
  margin-bottom: 2em;
  border-bottom: 1px solid #eee;
  padding-bottom: 1em;
}
div.blog h3{
  margin-top: 0.5em;
}
div.blog p.blog-info {
  margin-bottom: 0.5em;
}
</style>