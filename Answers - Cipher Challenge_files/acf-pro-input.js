!function(i){var t=acf.Field.extend({type:"repeater",wait:"",events:{'click a[data-event="add-row"]':"onClickAdd",'click a[data-event="remove-row"]':"onClickRemove",'click a[data-event="collapse-row"]':"onClickCollapse",showField:"onShow",unloadField:"onUnload",mouseover:"onHover",unloadField:"onUnload"},$control:function(){return this.$(".acf-repeater:first")},$table:function(){return this.$("table:first")},$tbody:function(){return this.$("tbody:first")},$rows:function(){return this.$("tbody:first > tr").not(".acf-clone")},$row:function(t){return this.$("tbody:first > tr:eq("+t+")")},$clone:function(){return this.$("tbody:first > tr.acf-clone")},$actions:function(){return this.$(".acf-actions:last")},$button:function(){return this.$(".acf-actions:last .button")},getValue:function(){return this.$rows().length},allowRemove:function(){var t=parseInt(this.get("min"));return!t||t<this.val()},allowAdd:function(){var t=parseInt(this.get("max"));return!t||t>this.val()},addSortable:function(a){1!=this.get("max")&&this.$tbody().sortable({items:"> tr",handle:"> td.order",forceHelperSize:!0,forcePlaceholderSize:!0,scroll:!0,stop:function(t,e){a.render()},update:function(t,e){a.$input().trigger("change")}})},addCollapsed:function(){var e=a.load(this.get("key"));if(!e)return!1;this.$rows().each(function(t){-1<e.indexOf(t)&&i(this).addClass("-collapsed")})},addUnscopedEvents:function(a){this.on("invalidField",".acf-row",function(t){var e=i(this);a.isCollapsed(e)&&a.expand(e)})},initialize:function(){this.addUnscopedEvents(this),this.addCollapsed(),acf.disable(this.$clone(),this.cid),this.render()},render:function(){this.$rows().each(function(t){i(this).find("> .order > span").html(t+1)}),0==this.val()?this.$control().addClass("-empty"):this.$control().removeClass("-empty"),this.allowAdd()?this.$button().removeClass("disabled"):this.$button().addClass("disabled")},validateAdd:function(){if(this.allowAdd())return!0;var t=this.get("max"),e=acf.__("Maximum rows reached ({max} rows)");return e=e.replace("{max}",t),this.showNotice({text:e,type:"warning"}),!1},onClickAdd:function(t,e){if(!this.validateAdd())return!1;e.hasClass("acf-icon")?this.add({before:e.closest(".acf-row")}):this.add()},add:function(a){if(!this.allowAdd())return!1;a=acf.parseArgs(a,{before:!1});var t=acf.duplicate({target:this.$clone(),append:this.proxy(function(t,e){a.before?a.before.before(e):t.before(e),e.removeClass("acf-clone"),acf.enable(e,this.cid),this.render()})});return this.$input().trigger("change"),t},validateRemove:function(){if(this.allowRemove())return!0;var t=this.get("min"),e=acf.__("Minimum rows reached ({min} rows)");return e=e.replace("{min}",t),this.showNotice({text:e,type:"warning"}),!1},onClickRemove:function(t,e){var a=e.closest(".acf-row");a.addClass("-hover");var i=acf.newTooltip({confirmRemove:!0,target:e,context:this,confirm:function(){this.remove(a)},cancel:function(){a.removeClass("-hover")}})},remove:function(t){var e=this;acf.remove({target:t,endHeight:0,complete:function(){e.$input().trigger("change"),e.render()}})},isCollapsed:function(t){return t.hasClass("-collapsed")},collapse:function(t){t.addClass("-collapsed"),acf.doAction("hide",t,"collapse")},expand:function(t){t.removeClass("-collapsed"),acf.doAction("show",t,"collapse")},onClickCollapse:function(t,e){var a=e.closest(".acf-row"),i=this.isCollapsed(a);t.shiftKey&&(a=this.$rows()),i?this.expand(a):this.collapse(a)},onShow:function(t,e,a){var i=acf.getFields({is:":visible",parent:this.$el});acf.doAction("show_fields",i)},onUnload:function(){var e=[];this.$rows().each(function(t){i(this).hasClass("-collapsed")&&e.push(t)}),e=e.length?e:null,a.save(this.get("key"),e)},onHover:function(){this.addSortable(this),this.off("mouseover")}});acf.registerFieldType(t),acf.registerConditionForFieldType("hasValue","repeater"),acf.registerConditionForFieldType("hasNoValue","repeater"),acf.registerConditionForFieldType("lessThan","repeater"),acf.registerConditionForFieldType("greaterThan","repeater");var a=new acf.Model({name:"this.collapsedRows",key:function(t,e){var a=this.get(t+e)||0;return a++,this.set(t+e,a,!0),1<a&&(t+="-"+a),t},load:function(t){var t=this.key(t,"load"),e=acf.getPreference(this.name);return!(!e||!e[t])&&e[t]},save:function(t,e){var t=this.key(t,"save"),a=acf.getPreference(this.name)||{};null===e?delete a[t]:a[t]=e,i.isEmptyObject(a)&&(a=null),acf.setPreference(this.name,a)}})}(jQuery),function(c){var t=acf.Field.extend({type:"flexible_content",wait:"",events:{'click [data-name="add-layout"]':"onClickAdd",'click [data-name="remove-layout"]':"onClickRemove",'click [data-name="collapse-layout"]':"onClickCollapse",showField:"onShow",unloadField:"onUnload",mouseover:"onHover"},$control:function(){return this.$(".acf-flexible-content:first")},$layoutsWrap:function(){return this.$(".acf-flexible-content:first > .values")},$layouts:function(){return this.$(".acf-flexible-content:first > .values > .layout")},$layout:function(t){return this.$(".acf-flexible-content:first > .values > .layout:eq("+t+")")},$clonesWrap:function(){return this.$(".acf-flexible-content:first > .clones")},$clones:function(){return this.$(".acf-flexible-content:first > .clones  > .layout")},$clone:function(t){return this.$('.acf-flexible-content:first > .clones  > .layout[data-layout="'+t+'"]')},$actions:function(){return this.$(".acf-actions:last")},$button:function(){return this.$(".acf-actions:last .button")},$popup:function(){return this.$(".tmpl-popup:last")},getPopupHTML:function(){var t=this.$popup().html(),e=c(t),a=this.$layouts(),r=function(t){return a.filter(function(){return c(this).data("layout")===t}).length};return e.find("[data-layout]").each(function(){var t=c(this),e=t.data("min")||0,a=t.data("max")||0,i=t.data("layout")||"",n=r(i);if(a&&a<=n)t.addClass("disabled");else if(e&&n<e){var o=e-n,s=acf.__("{required} {label} {identifier} required (min {min})"),l=acf._n("layout","layouts",o);s=(s=(s=(s=s.replace("{required}",o)).replace("{label}",i)).replace("{identifier}",l)).replace("{min}",e),t.append('<span class="badge" title="'+s+'">'+o+"</span>")}}),t=e.outerHTML()},getValue:function(){return this.$layouts().length},allowRemove:function(){var t=parseInt(this.get("min"));return!t||t<this.val()},allowAdd:function(){var t=parseInt(this.get("max"));return!t||t>this.val()},isFull:function(){var t=parseInt(this.get("max"));return t&&this.val()>=t},addSortable:function(a){1!=this.get("max")&&this.$layoutsWrap().sortable({items:"> .layout",handle:"> .acf-fc-layout-handle",forceHelperSize:!0,forcePlaceholderSize:!0,scroll:!0,stop:function(t,e){a.render()},update:function(t,e){a.$input().trigger("change")}})},addCollapsed:function(){var e=a.load(this.get("key"));if(!e)return!1;this.$layouts().each(function(t){-1<e.indexOf(t)&&c(this).addClass("-collapsed")})},addUnscopedEvents:function(e){this.on("invalidField",".layout",function(t){e.onInvalidField(t,c(this))})},initialize:function(){this.addUnscopedEvents(this),this.addCollapsed(),acf.disable(this.$clonesWrap(),this.cid),this.render()},render:function(){this.$layouts().each(function(t){c(this).find(".acf-fc-layout-order:first").html(t+1)}),0==this.val()?this.$control().addClass("-empty"):this.$control().removeClass("-empty"),this.isFull()?this.$button().addClass("disabled"):this.$button().removeClass("disabled")},onShow:function(t,e,a){var i=acf.getFields({is:":visible",parent:this.$el});acf.doAction("show_fields",i)},validateAdd:function(){if(this.allowAdd())return!0;var t=this.get("max"),e=acf.__("This field has a limit of {max} {label} {identifier}"),a=acf._n("layout","layouts",t);return e=(e=(e=e.replace("{max}",t)).replace("{label}","")).replace("{identifier}",a),this.showNotice({text:e,type:"warning"}),!1},onClickAdd:function(t,e){if(!this.validateAdd())return!1;var a=null,i;e.hasClass("acf-icon")&&(a=e.closest(".layout")).addClass("-hover"),new n({target:e,targetConfirm:!1,text:this.getPopupHTML(),context:this,confirm:function(t,e){e.hasClass("disabled")||this.add({layout:e.data("layout"),before:a})},cancel:function(){a&&a.removeClass("-hover")}}).on("click","[data-layout]","onConfirm")},add:function(a){if(a=acf.parseArgs(a,{layout:"",before:!1}),!this.allowAdd())return!1;var t=acf.duplicate({target:this.$clone(a.layout),append:this.proxy(function(t,e){a.before?a.before.before(e):this.$layoutsWrap().append(e),acf.enable(e,this.cid),this.render()})});return this.$input().trigger("change"),t},validateRemove:function(){if(this.allowRemove())return!0;var t=this.get("min"),e=acf.__("This field requires at least {min} {label} {identifier}"),a=acf._n("layout","layouts",t);return e=(e=(e=e.replace("{min}",t)).replace("{label}","")).replace("{identifier}",a),this.showNotice({text:e,type:"warning"}),!1},onClickRemove:function(t,e){var a=e.closest(".layout");a.addClass("-hover");var i=acf.newTooltip({confirmRemove:!0,target:e,context:this,confirm:function(){this.removeLayout(a)},cancel:function(){a.removeClass("-hover")}})},removeLayout:function(t){var e=this,a=1==this.getValue()?60:0;acf.remove({target:t,endHeight:a,complete:function(){e.$input().trigger("change"),e.render()}})},onClickCollapse:function(t,e){var a=e.closest(".layout");this.isLayoutClosed(a)?this.openLayout(a):this.closeLayout(a)},isLayoutClosed:function(t){return t.hasClass("-collapsed")},openLayout:function(t){t.removeClass("-collapsed"),acf.doAction("show",t,"collapse")},closeLayout:function(t){t.addClass("-collapsed"),acf.doAction("hide",t,"collapse"),this.renderLayout(t)},renderLayout:function(e){var t,a=e.children("input").attr("name").replace("[acf_fc_layout]",""),i={action:"acf/fields/flexible_content/layout_title",field_key:this.get("key"),i:e.index(),layout:e.data("layout"),value:acf.serialize(e,a)};c.ajax({url:acf.get("ajaxurl"),data:acf.prepareForAjax(i),dataType:"html",type:"post",success:function(t){t&&e.children(".acf-fc-layout-handle").html(t)}})},onUnload:function(){var e=[];this.$layouts().each(function(t){c(this).hasClass("-collapsed")&&e.push(t)}),e=e.length?e:null,a.save(this.get("key"),e)},onInvalidField:function(t,e){this.isLayoutClosed(e)&&this.openLayout(e)},onHover:function(){this.addSortable(this),this.off("mouseover")}});acf.registerFieldType(t);var n=acf.models.TooltipConfirm.extend({events:{"click [data-layout]":"onConfirm",'click [data-event="cancel"]':"onCancel"},render:function(){this.html(this.get("text")),this.$el.addClass("acf-fc-popup")}});acf.registerConditionForFieldType("hasValue","flexible_content"),acf.registerConditionForFieldType("hasNoValue","flexible_content"),acf.registerConditionForFieldType("lessThan","flexible_content"),acf.registerConditionForFieldType("greaterThan","flexible_content");var a=new acf.Model({name:"this.collapsedLayouts",key:function(t,e){var a=this.get(t+e)||0;return a++,this.set(t+e,a,!0),1<a&&(t+="-"+a),t},load:function(t){var t=this.key(t,"load"),e=acf.getPreference(this.name);return!(!e||!e[t])&&e[t]},save:function(t,e){var t=this.key(t,"save"),a=acf.getPreference(this.name)||{};null===e?delete a[t]:a[t]=e,c.isEmptyObject(a)&&(a=null),acf.setPreference(this.name,a)}})}(jQuery),function(s){var t=acf.Field.extend({type:"gallery",events:{"click .acf-gallery-add":"onClickAdd","click .acf-gallery-edit":"onClickEdit","click .acf-gallery-remove":"onClickRemove","click .acf-gallery-attachment":"onClickSelect","click .acf-gallery-close":"onClickClose","change .acf-gallery-sort":"onChangeSort","click .acf-gallery-update":"onUpdate",mouseover:"onHover",showField:"render"},actions:{validation_begin:"onValidationBegin",validation_failure:"onValidationFailure",resize:"onResize"},onValidationBegin:function(){acf.disable(this.$sideData(),this.cid)},onValidationFailure:function(){acf.enable(this.$sideData(),this.cid)},$control:function(){return this.$(".acf-gallery")},$collection:function(){return this.$(".acf-gallery-attachments")},$attachments:function(){return this.$(".acf-gallery-attachment")},$attachment:function(t){return this.$('.acf-gallery-attachment[data-id="'+t+'"]')},$active:function(){return this.$(".acf-gallery-attachment.active")},$main:function(){return this.$(".acf-gallery-main")},$side:function(){return this.$(".acf-gallery-side")},$sideData:function(){return this.$(".acf-gallery-side-data")},isFull:function(){var t=parseInt(this.get("max")),e=this.$attachments().length;return t&&t<=e},getValue:function(){var t=[];return this.$attachments().each(function(){t.push(s(this).data("id"))}),!!t.length&&t},addUnscopedEvents:function(e){this.on("change",".acf-gallery-side",function(t){e.onUpdate(t,s(this))})},addSortable:function(t){this.$collection().sortable({items:".acf-gallery-attachment",forceHelperSize:!0,forcePlaceholderSize:!0,scroll:!0,start:function(t,e){e.placeholder.html(e.item.html()),e.placeholder.removeAttr("style")}}),this.$control().resizable({handles:"s",minHeight:200,stop:function(t,e){acf.update_user_setting("gallery_height",e.size.height)}})},initialize:function(){this.addUnscopedEvents(this),this.render()},render:function(){var t=this.$(".acf-gallery-sort"),e=this.$(".acf-gallery-add"),a=this.$attachments().length;this.isFull()?e.addClass("disabled"):e.removeClass("disabled"),a?t.removeClass("disabled"):t.addClass("disabled"),this.resize()},resize:function(){var t=this.$control().width(),e=150,a=Math.round(t/e);a=Math.min(a,8),this.$control().attr("data-columns",a)},onResize:function(){this.resize()},openSidebar:function(){this.$control().addClass("-open");var t=this.$control().width()/3;t=parseInt(t),t=Math.max(t,350),this.$(".acf-gallery-side-inner").css({width:t-1}),this.$side().animate({width:t-1},250),this.$main().animate({right:t},250)},closeSidebar:function(){this.$control().removeClass("-open"),this.$active().removeClass("active"),acf.disable(this.$side());var t=this.$(".acf-gallery-side-data");this.$main().animate({right:0},250),this.$side().animate({width:0},250,function(){t.html("")})},onClickAdd:function(t,e){if(this.isFull())this.showNotice({text:acf.__("Maximum selection reached"),type:"warning"});else var a=acf.newMediaPopup({mode:"select",title:acf.__("Add Image to Gallery"),field:this.get("key"),multiple:"add",library:this.get("library"),allowedTypes:this.get("mime_types"),selected:this.val(),select:s.proxy(function(t,e){this.appendAttachment(t,e)},this)})},appendAttachment:function(t,e){if(t=this.validateAttachment(t),!this.isFull()&&!this.$attachment(t.id).length){var a=['<div class="acf-gallery-attachment" data-id="'+t.id+'">','<input type="hidden" value="'+t.id+'" name="'+this.getInputName()+'[]">','<div class="margin" title="">','<div class="thumbnail">','<img src="" alt="">',"</div>",'<div class="filename"></div>',"</div>",'<div class="actions">','<a href="#" class="acf-icon -cancel dark acf-gallery-remove" data-id="'+t.id+'"></a>',"</div>","</div>"].join(""),i=s(a);if(this.$collection().append(i),"prepend"===this.get("insert")){var n=this.$attachments().eq(e);n.length&&n.before(i)}this.renderAttachment(t),this.render(),this.$input().trigger("change")}},validateAttachment:function(t){if((t=acf.parseArgs(t,{id:"",url:"",alt:"",title:"",filename:"",type:"image"})).attributes){t=t.attributes;var e=acf.isget(t,"sizes","medium","url");null!==e&&(t.url=e)}return t},renderAttachment:function(t){t=this.validateAttachment(t);var e=this.$attachment(t.id);"image"==t.type?e.find(".filename").remove():(t.url=acf.isget(t,"thumb","src"),e.find(".filename").text(t.filename)),t.url||(t.url=acf.get("mimeTypeIcon"),e.addClass("-icon")),e.find("img").attr({src:t.url,alt:t.alt,title:t.title}),acf.val(e.find("input"),t.id)},editAttachment:function(t){var e=acf.newMediaPopup({mode:"edit",title:acf.__("Edit Image"),button:acf.__("Update Image"),attachment:t,field:this.get("key"),select:s.proxy(function(t,e){this.renderAttachment(t)},this)})},onClickEdit:function(t,e){var a=e.data("id");a&&this.editAttachment(a)},removeAttachment:function(t){this.closeSidebar(),this.$attachment(t).remove(),this.render(),this.$input().trigger("change")},onClickRemove:function(t,e){t.preventDefault(),t.stopPropagation();var a=e.data("id");a&&this.removeAttachment(a)},selectAttachment:function(a){var t=this.$attachment(a);if(!t.hasClass("active")){var e=this.proxy(function(){this.$side().find(":focus").trigger("blur"),this.$active().removeClass("active"),t.addClass("active"),this.openSidebar(),i()}),i=this.proxy(function(){var t={action:"acf/fields/gallery/get_attachment",field_key:this.get("key"),id:a};this.has("xhr")&&this.get("xhr").abort(),acf.showLoading(this.$sideData());var e=s.ajax({url:acf.get("ajaxurl"),data:acf.prepareForAjax(t),type:"post",dataType:"html",cache:!1,success:n});this.set("xhr",e)}),n=this.proxy(function(t){if(t){var e=this.$sideData();e.html(t),e.find(".compat-field-acf-form-data").remove(),e.find("> table.form-table > tbody").append(e.find("> .compat-attachment-fields > tbody > tr")),acf.doAction("append",e)}});e()}},onClickSelect:function(t,e){var a=e.data("id");a&&this.selectAttachment(a)},onClickClose:function(t,e){this.closeSidebar()},onChangeSort:function(t,e){var a=e.val();if(a){var i=[];this.$attachments().each(function(){i.push(s(this).data("id"))});var n=this.proxy(function(){var t={action:"acf/fields/gallery/get_sort_order",field_key:this.get("key"),ids:i,sort:a},e=s.ajax({url:acf.get("ajaxurl"),dataType:"json",type:"post",cache:!1,data:acf.prepareForAjax(t),success:o})}),o=this.proxy(function(t){acf.isAjaxSuccess(t)&&(t.data.reverse(),t.data.map(function(t){this.$collection().prepend(this.$attachment(t))},this))});n()}},onUpdate:function(t,e){var a=this.$(".acf-gallery-update");if(!a.hasClass("disabled")){var i=acf.serialize(this.$sideData());a.addClass("disabled"),a.before('<i class="acf-loading"></i> '),i.action="acf/fields/gallery/update_attachment",s.ajax({url:acf.get("ajaxurl"),data:acf.prepareForAjax(i),type:"post",dataType:"json",complete:function(){a.removeClass("disabled"),a.prev(".acf-loading").remove()}})}},onHover:function(){this.addSortable(this),this.off("mouseover")}});acf.registerFieldType(t),acf.registerConditionForFieldType("hasValue","gallery"),acf.registerConditionForFieldType("hasNoValue","gallery"),acf.registerConditionForFieldType("selectionLessThan","gallery"),acf.registerConditionForFieldType("selectionGreaterThan","gallery")}(jQuery);