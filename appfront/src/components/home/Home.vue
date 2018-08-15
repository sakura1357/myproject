<template>
	<div id="home">
    <h1>首页</h1>
		  <div class="row">
        <ul v-for="blog in blogList">
          <li>标题：{{ blog.fields.title }}</li>
          <li>作者：{{ blog.fields.author }}</li>
          <li>类型：{{ blog.fields.blog_type }}</li>
          <li>内容：{{ blog.fields.content }}</li>
          <li>创建时间：{{ blog.fields.created_time }}</li>
          <li>最后更新时间：{{ blog.fields.last_updated_time }}</li>
        </ul>
      </div><!-- /.row -->
	</div>
</template>
<script type="text/javascript">
	export default {
		name: 'home',
		data(){
      return {
        blogList: []
      }
    },
    created(){
      this.$ajax.get('blog/show_blogs/')
      .then(response=>{
        var res = response.data
          console.log(res)
          this.blogList = res['list']
        })
      .catch(error=>{

      })
    }
  }
</script>
<style scoped>
	

</style>