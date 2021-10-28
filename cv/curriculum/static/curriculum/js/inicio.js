document.body.onload=()=>{
    console.log('dynamic loading inicio')
    
    let m_ofs_x = -1
    let m_ofs_y = -1
    
    window.addEventListener("mousemove", (e) => {
        let step = 5
        //if (m_ofs_x > e.offsetX)
        document.body.style.backgroundPositionX = -e.pageX/step + "px";
        document.body.style.backgroundPositionY = -e.pageY/step + "px";
        /*
        document.body.style.backgroundPositionX += (m_ofs_x > e.pageX)?step:-step+"px";
        document.body.style.backgroundPositionY += (m_ofs_y > document.body.offsetY)?step:-step+"px";
        m_ofs_x = e.pageX
        m_ofs_y = e.offsetY
        //console.log(document.body.offsetY)
        console.log(e.pageX)
        console.dir(e)
        */
        //document.body.style.backgroundPositionX = -e.offsetX/50 + "px";
        //document.body.style.backgroundPositionY = -e.offsetY/50 + "px";
    })            
                
    let up_btn = $('#up')
    up_btn.hide().click(()=>{
        $('html, body').animate({scrollTop: 0, duration: 2000})
    })
    function check_up_btn(){
        if (window.scrollY > 200) {
            up_btn.show()
        } else {
            up_btn.hide()
        }
    }
    check_up_btn()
    window.addEventListener('scroll',(e)=>{
        check_up_btn()
    })
    
    $('body').scrollspy({ target: '#navbar-header' })
    
    let now = new Date()
    let was = new Date('1979-09-20T12:34:56')
    //let was = new Date('2020-12-21T12:34:56')
    let y = now.getFullYear()-was.getFullYear();y=was.getMonth()<now.getMonth()?y:y-1
    let m = now.getMonth()-was.getMonth();m=m<0?12+m:m
    let d = now.getDate()-was.getDate();
    $("#edad").text(y+" años "+m+" meses "+d+" dias")            
    
    let navs = $("#navbarCollapse a")
    navs.click((e)=>{
        e.preventDefault();
        console.log($(e.target.hash+" h2").text())
        $('html, body').animate({
            scrollTop: $(e.target.hash).offset().top,
            duration: 2500
        })
        /*
        let tl = gsap.timeline()
        let st = new SplitText(e.target.hash+" h2", {type:"words,chars"}) 
        let chars = st.chars
        gsap.set(e.target.hash+" h2", {perspective: 400})
        tl.from(chars, {
            duration: 0.2, opacity:0, scale:0, y:-80, rotationX:180, 
            transformOrigin:"0% 50% -50",  ease:"back", stagger: 0.01
        }, "+=1")
        */
    })
    console.log('dynamic loading finish')
}
console.log('static loading finish')
