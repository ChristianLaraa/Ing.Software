class WeekDays{
    diaEsp = ["Lunes","Martes","Miércoles","Jueves","Viernes"];
    diaEng =["Monday","Tuesday","Wednesday","Thursday","Friday"];
    /* Singleton constructor para evaluar si existe o no un determinado objeto
    Si existe lo llama, en caso de No existir se crea
    */
    constructor(lang){
    this.lang = lang;
    if(WeekDays.instance){
    return WeekDays.instance;
    }
    WeekDays.instance=this;
    }
    //Método para obtener los días
    getDays(){
    return this.lang === "es" ?
    this.diaEsp:
    this.diaEng;
    }
    }
    
    // Probar método Singleton fuera de la Class
    const weekDays1 = new WeekDays ("en");
    const weekDays2 = new WeekDays();
    //const weekDays2 = new WeekDays("es"); /* si se agrega valor diferente en segundo objeto, la salida no cambia salida */
    
    console.log(weekDays1.getDays()); /* vistas en consola */
    console.log(weekDays2.getDays());