//Patrón Singleton
class Singleton{
    constructor(){
    //evaluar si esta creado el objeto, en caso de que no se crea
    console.log("Entra al Constructor");
    this.random = Math.random();
    if(Singleton.instance){
    console.log("ya existe");
    return Singleton.instance;
    }
    //crear instancia si no existe
    console.log("No existe y se crea");
    Singleton.instance=this;
    }
    }
    
    //Fuera de Class Crear Objeto
    //primer ejecución
    const singleton1 = new Singleton();
    //segunda ejecución
    const singleton2 = new Singleton();
    //Verificación de números random almacenados
    console.log(singleton1.random);
    console.log(singleton2.random);
    console.log(singleton1 === singleton2);