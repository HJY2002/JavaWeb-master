let data={
    banks:[]
};
let vm =new Vue({
    el:'#bank-app',
    data,
    mounted(){
        fetch('http://locallhost:5000/bank')
            .then(res=>res.json())
            .then(data=>{
               for ( i in data.data){
                   this.banks.push(data.data[i]);
               }
            })
    }
})