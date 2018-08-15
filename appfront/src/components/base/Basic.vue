<template>
	<div id="basic">
    	<div class="navbar navbar-default navbar-fixed-top" role="navigation">
		<div class="container-fluid">
			<div class="navbar-header">
				<a class="navbar-brand" href="">Logo</a>
				<button class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse">
					<span class="icon-bar"></span>
        			<span class="icon-bar"></span>
        			<span class="icon-bar"></span>
				</button>
			</div>
			<div id="navbar-collapse" class="collapse navbar-collapse">
				<ul class="nav navbar-nav">
					<li class="">
						<router-link to="/home">首页</router-link>
					</li>
					<li class="">
						<router-link to="/bloglist">博客</router-link>
					</li>					
					<li class="">
						<router-link to="/about">关于</router-link>
					</li>					
					<li class="">
						<a href="">联系</a>
					</li>
				</ul>
				<ul class="nav navbar-nav navbar-right">
					<li>
						<router-link to="/login">登录</router-link>
					</li>
					<li>
						<router-link to="/register">注册</router-link>
					</li>
					<li>
						<form class="navbar-form navbar-left">
							<div class="form-group">
								<input type="text" class="form-control" placeholder="Search">
							</div>
							<button type="submit" class="btn btn-default">搜索</button>
						</form>
					</li>
				</ul>
			</div>

		</div>	
	</div>

	<div class="container">
		<router-view/>
	</div><!-- /.container -->
	
    <footer class="blog-footer">
    	<p class="copyright">&copy 2018 - 采集自 <a href="https://v3.bootcss.com/examples/blog/"
    		target="_blank" title="模板之家">Boostrap</a>
    		- 由 Siar 修改
    	</p>
    </footer>
</div>
	</div>
</template>
<script type="text/javascript">
	export default {
		name: 'Basic',
		data(){
			return{
				msg: '我是basic组件'
			}
		},
		created(){

		},
		mounted(){

		}
	}
</script>
<style scoped>

/*
 * Globals
 */

body {
  font-family: Georgia, "Times New Roman", Times, serif;
  color: #555;
}

h1, .h1,
h2, .h2,
h3, .h3,
h4, .h4,
h5, .h5,
h6, .h6 {
  margin-top: 0;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: normal;
  color: #333;
}


/*
 * Override Bootstrap's default container.
 */

@media (min-width: 1200px) {
  .container {
    width: 970px;
  }
}


.container {
	margin-top: 6em;
}

/*
 * Footer
 */

.blog-footer {
  padding: 40px 0;
  color: #999;
  text-align: center;
  background-color: #f9f9f9;
  border-top: 1px solid #e5e5e5;
}
.blog-footer p:last-child {
  margin-bottom: 0;
}

</style>

