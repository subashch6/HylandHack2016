
var jsonObj_Agg = null;

function generateGraph(data, type, bindDiv)
{
	var chart = c3.generate({
				bindto: bindDiv,
				data: {
					columns: data,
					type: type
					}
				});
	return chart;
}

function sendQueryEmit()
{
	var val = document.getElementById('input').value;
	val = val.trim();
	var val2 = document.getElementById('input2').value;
	socket.emit('QuerySent', {'query':[val2,val]});
	
}


function setAggregate(jsonObj)
{
	jsonObj_Agg = jsonObj;
}


function processPolitical()
{
	aggregate_pol = jsonObj_Agg.org_tweet[0].aggregate_political_scores;
	pol = jsonObj_Agg.org_tweet[0].political_scores;
	aggregate_pol.unshift('Followers Political');
	pol.unshift('Tweet Political');
	pol_json = [pol, aggregate_pol];
	return pol_json;
}


function processPersonality()
{
	aggregate_per = jsonObj_Agg.org_tweet[0].aggregate_personality_scores;
	per  = jsonObj_Agg.org_tweet[0].personality_scores;
	aggregate_per.unshift('Followers Personality');
	per.unshift('Tweet Personality');
	per_json = [per, aggregate_per];
	return per_json;
}

function processEmotion()
{
	aggregate_emo = jsonObj_Agg.org_tweet[0].aggregate_emotion_scores;
	var anger = ['Anger',aggregate_emo[0]];
	var joy = ['Joy',aggregate_emo[1]];
	var fear = ['Fear',aggregate_emo[2]];
	var sadness = ['Sadness',aggregate_emo[3]];
	var surprise = ['Surprise',aggregate_emo[4]];

	var values = [anger, joy, fear, sadness, surprise];
	return values;
}

function processEngagement()
{
	val = jsonObj_Agg.org_tweet[0].twitter_engagement;
	val *= 100;
	val2 = ['Twitter Engagement', val];
	return val2;
}



