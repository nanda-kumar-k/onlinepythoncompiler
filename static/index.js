var textareas = document.getElementsByTagName('textarea');
        var count = textareas.length;
        for(var i=0;i<count;i++){
            textareas[i].onkeydown = function(e){
                if(e.keyCode==9 || e.which==9){
                    e.preventDefault();
                    var s = this.selectionStart;
                    this.value = this.value.substring(0,this.selectionStart) + "\t" + this.value.substring(this.selectionEnd);
                    this.selectionEnd = s+1; 
                }
            }
        }
        window.pressed = function(){
            var a = document.getElementById('aa');
            if(a.value == "")
            {
                fileLabel.innerHTML = "Choose file";
            }
            else
            {
                var theSplit = a.value.split('\\');
                fileLabel.innerHTML = theSplit[theSplit.length-1];
            }
        };

        window.outpressedfun = function(){
            var a = document.getElementById('outpressed');
            if(a.value == "")
            {
                fileLabe2.innerHTML = "Choose file";
            }
            else
            {
                var theSplit = a.value.split('\\');
                fileLabe2.innerHTML = theSplit[theSplit.length-1];
            }
        };

        function codeoptions(opt){
            if (opt == "editer"){
                document.getElementsByClassName("code-container")[0].style.display = "block";
                document.getElementsByClassName("upload-code-file")[0].style.display = "none";
            }
            else if (opt == "upload"){
                document.getElementsByClassName("code-container")[0].style.display = "none";
                document.getElementsByClassName("upload-code-file")[0].style.display = "flex";
            }
        }

        function inputoption(opt){
            if (opt == "upload"){
                document.getElementsByClassName("upload-input-file")[0].style.display = "flex";
                document.getElementsByClassName("take-input")[0].style.display = "none";
                document.getElementsByClassName("display-output")[0].style.display = "none";
            }
            else if (opt == "output"){
                document.getElementsByClassName("upload-input-file")[0].style.display = "none";
                document.getElementsByClassName("take-input")[0].style.display = "none";
                document.getElementsByClassName("display-output")[0].style.display = "block";
            }
            else if (opt == "enterinput"){
                document.getElementsByClassName("upload-input-file")[0].style.display = "none";
                document.getElementsByClassName("take-input")[0].style.display = "block";
                document.getElementsByClassName("display-output")[0].style.display = "none";
            }
        }
        function submitcode(){
            document.getElementById("codefile").action = "/compile";
            document.getElementById("codefile").submit();
        }
        function submitcodefile(){
            document.getElementById("codefile").action = "/uploadfile/code";
            document.getElementById("codefile").submit();
        }
        function submitinputfile(){
            document.getElementById("codefile").action = "/uploadfile/input";
            document.getElementById("codefile").submit();
        }

        function fontsize(){
            var fontsize = document.getElementById("select1").value;
            var textareas = document.getElementsByTagName('textarea');
            var count = textareas.length;
            for(var i=0;i<count;i++){
                textareas[i].style.fontSize = fontsize;
            }
        }

        function screendark(){
            document.getElementsByTagName("body")[0].style.backgroundColor = "rgb(10, 10, 10)";
            document.getElementsByTagName("body")[0].style.color = "white";
            document.getElementsByTagName("body")[0].style.transition = "all 0.5s";
            document.getElementsByTagName("body")[0].style.transitionTimingFunction = "ease-in-out";
            document.getElementsByClassName("navbar-container")[0].style.backgroundColor = "black";
            document.getElementsByTagName("textarea")[0].style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementsByTagName("textarea")[0].style.color = "white";
            document.getElementsByTagName("textarea")[1].style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementsByTagName("textarea")[1].style.color = "white";
            document.getElementById("mode1").style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementById("mode2").style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementById("mode3").style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementById("mode4").style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementById("mode5").style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementById("mode6").style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementById("mode7").style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementById("select1").style.backgroundColor = "rgb(32, 31, 31)";
            document.getElementById("select1").style.color = "white";
        }
        function screenlight(){
            document.getElementsByTagName("body")[0].style.backgroundColor = "white";
            document.getElementsByTagName("body")[0].style.color = "black";
            document.getElementsByTagName("body")[0].style.transition = "all 0.5s";
            document.getElementsByTagName("body")[0].style.transitionTimingFunction = "ease-in-out";
            document.getElementsByClassName("navbar-container")[0].style.backgroundColor = "#2f64ea";
            document.getElementsByTagName("textarea")[0].style.backgroundColor = "white";
            document.getElementsByTagName("textarea")[0].style.color = "black";
            document.getElementsByTagName("textarea")[1].style.backgroundColor = "white";
            document.getElementsByTagName("textarea")[1].style.color = "black";
            document.getElementById("mode1").style.backgroundColor = "white";
            document.getElementById("mode2").style.backgroundColor = "white";
            document.getElementById("mode3").style.backgroundColor = "white";
            document.getElementById("mode4").style.backgroundColor = "white";
            document.getElementById("mode5").style.backgroundColor = "white";
            document.getElementById("mode6").style.backgroundColor = "white";
            document.getElementById("mode7").style.backgroundColor = "white";
            document.getElementById("select1").style.backgroundColor = "white";
            document.getElementById("select1").style.color = "black";
        }