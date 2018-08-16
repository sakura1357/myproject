<template>
	<div id="life">
    <h1>随心而记</h1>
		  <div class="row">
        <ul v-for="blog in blogList">
          <li>标题：{{ blog.fields.title }}</li>
          <li>作者：{{ blog.fields.author }}</li>
          <li>类型：{{ blog.fields.blog_type }}</li>
          <li v-html='"摘要：" + blog.fields.excerpt'></li>
          <li>创建时间：{{ blog.fields.created_time }}</li>
          <li>最后更新时间：{{ blog.fields.last_updated_time }}</li>
        </ul>
      </div><!-- /.row -->
	</div>
</template>
<script type="text/javascript">
	export default {
		name: 'Life',
		data(){
      return {
        blogList: []
      }
    },
    created(){
      this.$ajax.get('http://127.0.0.1:8000/blog/show_blogs/?blog_mark=Life')
      .then(response=>{
        var res = response.data
        this.blogList = res['list']
        })
      .catch(error=>{

      })
    }
  }
</script>
<style scoped>
	

</style>