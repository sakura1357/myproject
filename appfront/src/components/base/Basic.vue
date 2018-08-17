<template>
	<div id="basic">
    	<!-- <div class="navbar navbar-default navbar-fixed-top" role="navigation"> -->
    	<nav class="navbar navbar-default navbar-fixed-top">
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
						<router-link to="/tech">技术杂谈</router-link>
					</li>					
					<li class="">
						<router-link to="/life">随心而记</router-link>
					</li>					
					<li class="">
						<router-link to="/about">关于</router-link>

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
	</nav>
	<!-- </div> -->

	<div class="container">
		<router-view/>
	</div><!-- /.container -->
	
    <footer class="blog-footer navbar-fixed-bottom">
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

.container {
	margin-top: 6em;
	margin-bottom: 3em;
}

/*
 * Footer
 */

.blog-footer {
  padding: 25px 0;
  color: #999;
  text-align: center;
  background-color: #f9f9f9;
  border-top: 1px solid #e5e5e5;
}
.blog-footer p:last-child {
  margin-bottom: 0;
}

</style>

