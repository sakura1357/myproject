<template>
  <div id="blog">
    <div class="row">
    <div class="col-xs-10 col-xs-offset-1">
      <h3>{{ blog.blog_title }}</h3>
      <ul class="blog-info-description">
        <li>作者： {{ blog.author }}</li>
        <li>分类：<a href="">{{ blog.blog_type }}</a></li>
        <li>发表日期： {{ blog.created_time}}</li>
        <li>阅读()</li>
        <li>评论()</li>
        <li>点赞()</li>
      </ul>
      <div v-html='blog.blog_content' class="blog-content"></div>
      <div class="blog-more">
        <p>上一篇：
            <a 
            :href="'#/blog/'+previous_blog.id" 
            @click="get_previous_blog()" 
            v-if="previous_blog.blog_title">
            {{ previous_blog.blog_title }}
          </a>
            <span v-else>{{ previous_blog }}</span>
          &nbsp;下一篇：
            <a 
              :href="'#/blog/'+next_blog.id" 
              @click="get_next_blog()" 
              v-if="next_blog.blog_title">
            {{ next_blog.blog_title }}
            </a>
            <span v-else>{{ next_blog }}</span>
        </p>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
  export default {
      name: 'Blog',
      data(){
        return {
          blog: [],
          previous_blog: [],
          next_blog: []
        }
      },
      created(){
        this.$ajax.get('http://127.0.0.1:8000/blog/show_blog_detail/?id=' + this.$route.params.id)
        .then(response=>{
          var res = response.data;
          this.blog = res['blog'];
          this.previous_blog = res['previous_blog'];
          this.next_blog = res['next_blog'];
          console.log(res);
        })
        .catch(error=>{

        });
      },
      methods : {
        get_previous_blog(){
        this.$ajax.get('http://127.0.0.1:8000/blog/show_blog_detail/?id=' + this.previous_blog.id)
        .then(response=>{
          var res = response.data;
          this.blog = res['blog'];
          this.previous_blog = res['previous_blog'];
          this.next_blog = res['next_blog'];
          console.log(res);
        })
        .catch(error=>{

        });

        },
        get_next_blog(){
        this.$ajax.get('http://127.0.0.1:8000/blog/show_blog_detail/?id=' + this.next_blog.id)
        .then(response=>{
          var res = response.data;
          this.blog = res['blog'];
          this.previous_blog = res['previous_blog'];
          this.next_blog = res['next_blog'];
          console.log(res);
        })
        .catch(error=>{

        });

        }
      }
  }
</script>
<style scoped>

ul.blog-info-description {
  list-style-type: none;
  margin-bottom: 1em;
}
ul.blog-info-description li{
  display: inline-block;
  margin-right: 1em;
}

/**首行缩进2个字符**/
div.blog-content {
  /*text-indent: 2em;*/
  margin-bottom: 2em;

}

div.blog-more {
  display: inline-block;
}


</style>