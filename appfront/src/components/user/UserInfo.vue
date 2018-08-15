<template>
	<div id="user-info">
		<p>{{ msg }}</p>
	</div>
</template>
<script>
	export default {
		name: 'UserInfo',
		data(){
			return {
				msg: '这是用户个人信息页面'
			}
		}
	}
</script>