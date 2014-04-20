(function($){
  
  /**
   * Tractatus quotation object
   * 
   * @type @exp;Backbone@pro;Model@call;extend
   */
  var BookPassage = Backbone.Model.extend({
    url: 'http://api.wittgenste.in/random',
    //Default attributes
    defaults: function() {
      return {
        index: "0.000",
        text: "..."
      };
    }    
  });
  
  /**
   * Should only ever be a single one for now...
   * 
   * @type @exp;Backbone@pro;Collection@call;extend
   */
  var BookPassageCollection = Backbone.Collection.extend({
    model: BookPassage,
    url: 'http://api.wittgenste.in/random',
    
    /**
     * Parse the request
     * 
     * @param {type} res
     * @returns {unresolved}
     */
    parse : function(res) {
      console.log("Inside the parse");
      
      alert('response' + res);
      return res.BookPassage;
    }
  });
  
  /**
   * The current tractatus passage (which will be rendered to the screen)
   * 
   * @type _L1.Bookpassage
   */
  var CurrentPassage = new BookPassageCollection;
  
  /**
   * Application view (UI)
   * 
   * @type @exp;Backbone@pro;View@call;extend
   */
  var WittgensteinView = Backbone.View.extend({
    el: $('body'),
//    template: _.template($('#passage-template').html()),
    
    // Can change
    initialize: function() {
      _.bindAll(this, 'render');
      console.log("Setting model");
//      this.listenTo(this.model, 'change', this.render);
      this.model = new BookPassage();
      this.model.fetch();
      console.log("Done setting");
      
      this.listenTo(this.model, 'change', this.render);
      
      // Render self
      this.render();
    },
    
    render: function() {
      console.log("Rendering");
      $(this.el).html(
              '<p>'+ this.model.get('index') + '</p><p>' +
              this.model.get("text") + "</p>");
      console.log("Rendering done");
//      $(this.el).append(this.template(this.model.toJSON()));
      return this;
    },
    
  });  
  
  // Start the app
  var App = new WittgensteinView;
})(jQuery);