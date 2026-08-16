/* MAXESS 10.10 cross-domain Result Contract bridge.
 * Reads the assessment's signed-by-contract URL payload. Never reads rendered scores.
 */
(function(){
  'use strict';
  if(window.MAXESS_RESULT&&Array.isArray(window.MAXESS_RESULT.dimensions))return;
  var params=new URLSearchParams(window.location.search);
  var encoded=params.get('result');
  if(!encoded)return;
  try{
    var b64=encoded.replace(/-/g,'+').replace(/_/g,'/');
    while(b64.length%4)b64+='=';
    var binary=atob(b64),bytes=new Uint8Array(binary.length);
    for(var i=0;i<binary.length;i++)bytes[i]=binary.charCodeAt(i);
    var json=new TextDecoder('utf-8').decode(bytes),payload=JSON.parse(json);
    if(!payload||payload.version!=='MAXESS-RESULTS-CONTRACT-1'||payload.completed!==true)return;
    var names={direction:'Direction',communication:'Communication',evaluation:'Evaluation',iteration:'Iteration','systems-thinking':'Systems Thinking'};
    var dimensions=Object.keys(names).map(function(id){return {id:id,name:names[id],score:Number(payload.dimensions&&payload.dimensions[id])||0};});
    if(dimensions.length!==5)return;
    var overall=Math.max(0,Math.min(100,Number(payload.overall)||0));
    var band=overall<=50?'Foundation':overall<=75?'Developing':overall<=90?'Advancing':'Mastering';
    window.MAXESS_RESULT={schema:'MAXESS-RESULT-1',mode:'assessment-handoff',overallScore:overall,band:band,dimensions:dimensions,selectedInterests:Array.isArray(payload.selectedInterests)?payload.selectedInterests:[],responses:Array.isArray(payload.responses)?payload.responses:[]};
  }catch(error){
    window.MAXESS_RESULT_ERROR='Invalid MAXESS Result Contract';
  }
})();
