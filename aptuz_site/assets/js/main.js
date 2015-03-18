$(document).ready(function(e){
	$(window).scroll(function(){
		if($(this).scrollTop() > 500){
			$(".info-In .iC").addClass("active");
		}
		if($(this).scrollTop() > 600){
			$(".mW-2").find(".iC").addClass("active");
		}
	});

	$(".mobi-nav").click(function(e){
		$(".mob-main-nav").toggleClass("active").delay(300).queue(function(){
			$(".mobi-nav").toggleClass("active");
			$(".mobi-nav").find("span").toggleClass("active");
			$(this).dequeue();
		});
	});

	$(window).bind('load',function(){
		var pathname = $(location)[0].pathname ;
		$("#main-menu ul li").each(function(index,el){
			if(pathname === $(el).find("a").attr("href")){
				$(el).find("a").addClass("active");
			}
		});
	});

	$(".lmore").click(function(){
		$("html,body").animate({
			scrollTop : 583
		},1000);
	});

	$(".mail_send").click(function(e){
		e.preventDefault();
		$(this).attr('disabled','disabled');
		var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		if(re.test($("input[name='email']").val())){
			$.ajax({
				url : '/mail_request/',
				data: $(".mail_form").serialize(),
				type: 'GET',
				success: function(data){
					if (data === "success") {
						alert("Mail Sent Successfully");
						$(".mail_send").removeAttr("disabled");
					}
					else {
						$(".mail_send").removeAttr("disabled");
						alert("Invaild Request");
					}
				}
			});
		}
		else{
			$(".mail_send").removeAttr("disabled");
			alert("Enter Vaild Email");
		}
	});
});