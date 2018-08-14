<template>
	<div id="library">
		<!-- <button @click="showBooks()">点击显示所有数据</button> -->
		<h1>library</h1>
		<ul v-for="book in books">
			<li>书名：{{ book.fields.book_name }}</li>
			<li>作者：{{ book.fields.author }}</li>
		</ul>
	</div>
</template>
<script type="text/javascript">
	export default{
		name: 'library',
		data () {
			return {
				book_name: '',
				author: '',
				books: []
			}
		},
		created(){
			this.$ajax.get('http://127.0.0.1:8000/library/show_books/')
				.then(response=>{
					var res = response.data
					// console.log(res)
					this.books = res['list']
				})
				.catch(error=>{

				})
		},
		methods:{

		}
}
</script>
