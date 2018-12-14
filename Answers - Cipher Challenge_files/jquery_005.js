$(document).ready(function(){var e=$(".js-accordion");e.length&&(e.each(function(e){var a=$(this);$options=a.data(),$accordions_headers=a.find(".js-accordion__header"),$accordions_prefix_classes=$options.accordionPrefixClasses||"",$accordions_multiselectable=$options.accordionMultiselectable||"",$index_accordion=e+1,a.attr({role:"tablist","aria-multiselectable":"true","class":$accordions_prefix_classes}),"none"===$accordions_multiselectable&&a.attr("aria-multiselectable","false"),$accordions_headers.each(function(e){var a=$(this),t=a.text(),r=a.next(".js-accordion__panel"),o=e+1;r.prepend(a.removeClass("js-accordion__header").addClass($accordions_prefix_classes+"__title").attr("tabindex","0")),$accordion_header=$('<button class="js-accordion__header '+$accordions_prefix_classes+'__header">'+t+"</button>"),r.before($accordion_header),$accordion_header.attr({"aria-controls":"accordion"+$index_accordion+"_panel"+o,"aria-expanded":"false",role:"tab",id:"accordion"+$index_accordion+"_tab"+o,tabindex:"-1","aria-selected":"false"}),r.attr({"aria-labelledby":"accordion"+$index_accordion+"_tab"+o,role:"tabpanel",id:"accordion"+$index_accordion+"_panel"+o,"aria-hidden":"true"}).addClass($accordions_prefix_classes+"__panel"),"true"==a.attr("data-accordion-opened")&&($accordion_header.attr("aria-expanded","true").removeAttr("data-accordion-opened"),r.attr("aria-hidden","false")),1===o&&$accordion_header.removeAttr("tabindex")})}),$("body").on("focus",".js-accordion__header",function(e){var a=$(this),t=a.parent(),r=t.find(".js-accordion__header");r.attr({tabindex:"-1","aria-selected":"false"}),a.attr("aria-selected","true").removeAttr("tabindex")}).on("click",".js-accordion__header",function(e){var a=$(this),t=$("#"+a.attr("aria-controls")),r=a.parent(),o=r.attr("aria-multiselectable"),i=r.find(".js-accordion__header"),n=r.find(".js-accordion__panel");i.attr("aria-selected","false"),a.attr("aria-selected","true"),"false"==a.attr("aria-expanded")?(a.attr("aria-expanded","true"),t.attr("aria-hidden","false")):(a.attr("aria-expanded","false"),t.attr("aria-hidden","true")),"false"==o&&(n.not(t).attr("aria-hidden","true"),i.not(a).attr("aria-expanded","false")),setTimeout(function(){a.focus()},0),e.preventDefault()}).on("keydown",".js-accordion__header",function(e){var a=$(this),t=a.parent(),r=t.find(".js-accordion__header"),o=t.find(".js-accordion__header").first(),i=t.find(".js-accordion__header").last(),n=a.prevAll(".js-accordion__header").first(),c=a.nextAll(".js-accordion__header").first();37!=e.keyCode&&38!=e.keyCode||e.ctrlKey?40!=e.keyCode&&39!=e.keyCode||e.ctrlKey?36==e.keyCode?(r.attr({tabindex:"-1","aria-selected":"false"}),o.attr("aria-selected","true").removeAttr("tabindex"),setTimeout(function(){o.focus()},0),e.preventDefault()):35==e.keyCode&&(r.attr({tabindex:"-1","aria-selected":"false"}),i.attr("aria-selected","true").removeAttr("tabindex"),setTimeout(function(){i.focus()},0),e.preventDefault()):(r.attr({tabindex:"-1","aria-selected":"false"}),a.is(i)?(o.attr("aria-selected","true").removeAttr("tabindex"),setTimeout(function(){o.focus()},0)):(c.attr("aria-selected","true").removeAttr("tabindex"),setTimeout(function(){c.focus()},0)),e.preventDefault()):(r.attr({tabindex:"-1","aria-selected":"false"}),a.is(o)?(i.attr("aria-selected","true").removeAttr("tabindex"),setTimeout(function(){i.focus()},0)):(n.attr("aria-selected","true").removeAttr("tabindex"),setTimeout(function(){n.focus()},0)),e.preventDefault())}).on("keydown",".js-accordion__panel",function(e){var a=$(this),t=$("#"+a.attr("aria-labelledby")),r=a.parent(),o=r.find(".js-accordion__header").first(),i=t.prevAll(".js-accordion__header").first(),n=t.nextAll(".js-accordion__header").first(),c=r.find(".js-accordion__header").last();38==e.keyCode&&e.ctrlKey?(setTimeout(function(){t.focus()},0),e.preventDefault()):33==e.keyCode&&e.ctrlKey?t.is(o)?(setTimeout(function(){c.focus()},0),e.preventDefault()):(setTimeout(function(){i.focus()},0),e.preventDefault()):34==e.keyCode&&e.ctrlKey&&(t.is(c)?(setTimeout(function(){o.focus()},0),e.preventDefault()):(setTimeout(function(){n.focus()},0),e.preventDefault()))}))});
//# sourceMappingURL=./jquery.accordion.min.js.map