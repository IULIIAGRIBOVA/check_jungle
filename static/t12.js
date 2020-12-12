$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				AuthorName : $('#AuthorName').val(),
				SearchPage : $('#SearchPage').val(),
				TrackName : $('#TrackName').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {


			$('#PageText').text(data.PageText).show();
			$('#PageURL').attr('href', data.PageURL)
			$('#PageURL').text(data.PageURL).show();
			$('#Loader').hide();



		});

		event.preventDefault();

	});

});
