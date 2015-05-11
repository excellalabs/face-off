$(document).ready(function () {
    showStars();
    $('#easyHeader').hide();
    $('#hardHeader').hide();

    if (round == 0) {
        $("#startGameModal").modal('show');
    }
    else if (gameMode != easyGame)
        startHardGame();
    else
        startEasyGame();

    //Add transition listeners
    cardTransitionListeners();

    //resets game round, selected value
    correct = 'False';
});

//Game Start Options
function startEasyGame() {
    gameMode = easyGame;
    $('#easyHeader').show()
}

function startHardGame() {
    startTimer();
    $('#hardHeader').show();
    $('.fa-share').hide()
}

function startTimer() {
    timer = $("#countdown").countdown360({
        radius: 40,
        seconds: 10,
        strokeWidth: 10,
        fillStyle: '#FFFFFF',
        strokeStyle: '#0099FF',
        fontSize: 30,
        fontColor: '#000000',
        autostart: false,
        onComplete: function () {
            disableCards(0, true);
        }
    });
    timer.start();
}

// Game Action Functions
function flip(id, choice) {
    if (choice == answer) {
        score += 1;
        updateCorrectStars(score - 1);
        correct = 'True';
    }
    else
        updateIncorrectStars(score - 1);

    $('#colleague' + id).addClass('clickFlip');

    //Interrupt countdown
    if (gameMode != easyGame)
        timer.stop(function () {
        });
    disableCards(id, false);
    resized = false;
}

function flipNoScore(id) {
    var card = $('#colleague' + id);
    if (card.hasClass('clickFlip')) {
        card.removeClass('clickFlip');
        card.trigger('stopRumble');


    }
    else
        card.addClass('clickFlip');

}

// disable onclick on other images, disable them & present next round button
function disableCards(id, disableALL) {
    for (var index = 0; index < maxRound; index++) {
        var card = $('#colleague' + index);
        if (gameMode != easyGame) {
            if (index != id || disableALL) {
                card.addClass('greyOut');
            }

            card.removeAttr('onclick');
            card.addClass('disabled');
        }
        else {
            shake();
            card.addClass('clickFlip');
            card.removeAttr('onclick');
            card.attr('onclick', 'flipNoScore(' + index + ')');
        }
    }
    if (gameMode != easyGame) {
        $("#countdown").hide();
        var nextRoundTimmer = $("#nextRoundCountdown").countdown360({
            radius: 40,
            seconds: 3,
            strokeWidth: 10,
            fillStyle: '#FFFFFF',
            strokeStyle: '#ff001a',
            fontSize: 30,
            fontColor: '#000000',
            autostart: false,
            onComplete: function () {
                if (round < maxRound) {
                    nextRound();
                }
                else {
                    setForm();
                }

            }
        });
        nextRoundTimmer.start();
    }
    else if (round == maxRound) {
        renderResultsLnk();
    }
    else if (round < maxRound) {
        $('#nextRound').removeClass('invisible');
    }
}

// Ajax related Functions
function setForm() {
    $('[name=score]').val(score);
    $('[name=answer_id]').val(answer);
    $('[name=results]').val(result_cards);
    $('[name=correct]').val(correct);
    if(gameMode != undefined)
        $('[name=mode]').val(gameMode);
    $('#resultsForm').submit();
}

function nextRound() {
    var cards = result_cards;
    formlessAjaxPostCSRFSetup();
    $.post('/rounds/', {
            matrix: cards,
            round: round,
            score: score,
            answer_id: answer,
            stars: stars,
            correct: correct
        },
        function (data) {
            $('#cards').html(data);
        });
}

//Display Functions
function shake() {
    for (var index = 0; index < maxRound; index++) {
        var card = $('#colleague' + index);
        card.jrumble({speed: 75, x: .5, y: .5, rotation: 0});
        card.hover(function () {
                $(this).trigger('startRumble');
            },
            function () {
                $(this).trigger('stopRumble');
            });
    }
}

function updateCorrectStars(starIndex) {
    $('#emptyStars').removeClass('fa fa-circle-o');
    $('#emptyStars').addClass('glyphicon glyphicon-ok-sign');
}
function updateIncorrectStars(starIndex) {
    $('#emptyStars').removeClass('fa fa-circle-o');
    $('#emptyStars').addClass('glyphicon glyphicon-remove-sign');
}

function renderResultsLnk() {
    $('#resultsSubmit').removeClass('invisible');
}

function showStars() {
    leftover_count = 5 - stars.length;
    html = "Round: ";
    for (var i = 0; i < stars.length; i++) {
        if (stars[i] == 'True') {
            html = html + "<i class='glyphicon glyphicon-ok-sign'></i>";
        }
        else if (stars[i] == 'False') {
            html = html + "<i class='glyphicon glyphicon-remove-sign'></i>";
        }
    }
    for (var j = 0; j < leftover_count; j++) {

        html = html + "<i id='emptyStars'class='fa fa-circle-o'></i>";
    }

    $('#stars').html(html);

}

function showGameMenu() {
    $('#gameMenu').removeClass('invisible');
    $('#noPicMenu').addClass('invisible');
    $('#noPicText').addClass('invisible');
    $('#addGameText').removeClass('invisible');
}

//--------  Text Resizing Methods -------
function cardTransitionListeners() {
    var cards = $('.flip-container');
    for (var x = 0; x < 4; x++) {
        cards[x].addEventListener('transitionend',
            function (event) {
                resizeText();
            }, false);
    }
}

function resizeText() {
    //Resize Card Text
    if (!resized) {
        $('.resizableText').textfill({
            minFontPixels: 12,
            maxFontPixels: 30
        });
        resized = true
    }
}
//-----------------X-------------