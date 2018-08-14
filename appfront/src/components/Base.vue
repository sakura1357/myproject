<template>
	<div id="base">
		<div class="navbar navbar-default navbar-fixed-top" role="navigation">
			<div class="container-fluid">
				<div class="navbar-header">
					<a class="navbar-brand" href="">我的网站</a>
					<button class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse">
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
				</div>
				<div id="navbar-collapse" class="collapse navbar-collapse">
					<ul class="nav navbar-nav">
						<li class="">
							<a href="">首页</a>
						</li>
						<li class="">
							<a href="">博客</a>
						</li>
					</ul>
					<ul class="nav navbar-nav navbar-right">
						<li>
							<a href="">登录</a>
						</li>
						<li>
							<a href="">注册</a>
						</li>
						<li class="dropdown">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">
								<span class="caret"></span>
							</a>
							<ul class="dropdown-menu">
								<li><a href="">个人资料</a></li>
								<li><a href="">修改密码</a></li>
								<li><a href="">后台管理</a></li>
								<li><a href="">退出</a></li>
							</ul>
						</li>

					</ul>
				</div>
			</div>
		</div>
		<div>
			<h1>这是base页面</h1>
		</div>
		<p>
            <router-link to="/base/home">主页</router-link>
        </p>	
        <router-view />
	</div>
</template>
<script type="text/javascript">
	export default {
		name: 'base',
		data(){

		},
		created(){

		},
		mounted(){

		}
	}
</script>
<style scoped>

</style>

