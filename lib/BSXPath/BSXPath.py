

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <title>
  vpetro / bsxpath / source &mdash; Bitbucket
</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="description" content="" />
  <meta name="keywords" content="" />
  <!--[if lt IE 9]>
  <script src="https://dwz7u9t8u8usb.cloudfront.net/m/957a2f59c221/js/lib/html5.js"></script>
  <![endif]-->

  <script>
    (function (window) {
      // prevent stray occurrences of `console.log` from causing errors in IE
      var console = window.console || (window.console = {});
      console.log || (console.log = function () {});

      var BB = window.BB || (window.BB = {});
      BB.debug = false;
      BB.cname = false;
      BB.CANON_URL = 'https://bitbucket.org';
      BB.MEDIA_URL = 'https://dwz7u9t8u8usb.cloudfront.net/m/957a2f59c221/';
      BB.images = {
        noAvatar: 'https://dwz7u9t8u8usb.cloudfront.net/m/957a2f59c221/img/no_avatar.gif'
      };
      BB.user || (BB.user = {});
      BB.user.has = (function () {
        var betaFeatures = [];
        
        return function (feature) {
          return _.contains(betaFeatures, feature);
        };
      }());
      BB.repo || (BB.repo = {});
  
  
      BB.user.isAdmin = false
      BB.repo.id = 85076;
    
    
      BB.repo.slug = 'bsxpath';
    
    
      BB.repo.owner = {
        username: 'vpetro'
      };
    
      // Coerce `BB.repo` to a string to get
      // "davidchambers/mango" or whatever.
      BB.repo.toString = function () {
        return this.owner.username + '/' + this.slug;
      }
    
      BB.changeset = 'b8565098c1e4'
    
    
  
    }(this));
  </script>

  


  <link rel="stylesheet" href="https://dwz7u9t8u8usb.cloudfront.net/m/957a2f59c221/bun/css/bundle.css"/>



  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Bitbucket" />
  <link rel="icon" href="https://dwz7u9t8u8usb.cloudfront.net/m/957a2f59c221/img/logo_new.png" type="image/png" />
  <link type="text/plain" rel="author" href="/humans.txt" />


  
    <script src="https://dwz7u9t8u8usb.cloudfront.net/m/957a2f59c221/bun/js/bundle.js"></script>
  



</head>

<body class="">
  <script type="text/javascript">
    if (!RegExp(" AppleWebKit/").test(navigator.userAgent)) {
    $('body').addClass('non-webkit');
    }
  </script>
  <!--[if IE 8]>
  <script>jQuery(document.body).addClass('ie8')</script>
  <![endif]-->
  <!--[if IE 9]>
  <script>jQuery(document.body).addClass('ie9')</script>
  <![endif]-->

  <div id="wrapper">


  <div class="site-message"><p>Bitbucket will be unavailable for a few moments <time datetime="2011-09-30T21:00+00:00">11:00pm, 26 September 2011 (UTC)</time> for maintenance.</p></div>


  <div id="header-wrap">
    <div id="header">
    <ul id="global-nav">
      <li><a class="home" href="http://www.atlassian.com">Atlassian Home</a></li>
      <li><a class="docs" href="http://confluence.atlassian.com/display/BITBUCKET">Documentation</a></li>
      <li><a class="support" href="/support">Support</a></li>
      <li><a class="blog" href="http://blog.bitbucket.org">Blog</a></li>
      <li><a class="forums" href="http://groups.google.com/group/bitbucket-users">Forums</a></li>
    </ul>
    <a href="/" id="logo">Bitbucket by Atlassian</a>

    <div id="main-nav">
    
      <ul class="clearfix">
        <li><a href="/features">Features</a></li>
        <li><a href="/plans">Pricing &amp; signup</a></li>
        <li><a href="/explore">Explore Bitbucket</a></li>
        <li><a href="/account/signin/?next=/vpetro/bsxpath/src/b8565098c1e4/BSXPath.py">Log in</a></li>
        

<li class="search-box">
  
    <form action="/repo/all">
      <input type="search" results="5" autosave="bitbucket-explore-search"
             name="name" id="searchbox"
             placeholder="Find a project" />
  
  </form>
</li>

      </ul>
    
    </div>
    </div>
  </div>

    <div id="header-messages">
  
  
    
    
    
    
  

    
   </div>



    <div id="content">
      <div id="unnamed">
      
  
  





  <script>
    jQuery(function ($) {
        var cookie = $.cookie,
            cookieOptions, date,
            $content = $('#content'),
            $pane = $('#what-is-bitbucket'),
            $hide = $pane.find('[href="#hide"]').css('display', 'block').hide();

        date = new Date();
        date.setTime(date.getTime() + 365 * 24 * 60 * 60 * 1000);
        cookieOptions = { path: '/', expires: date };

        if (cookie('toggle_status') == 'hide') $content.addClass('repo-desc-hidden');

        $('#toggle-repo-content').click(function (event) {
            event.preventDefault();
            $content.toggleClass('repo-desc-hidden');
            cookie('toggle_status', cookie('toggle_status') == 'show' ? 'hide' : 'show', cookieOptions);
        });

        if (!cookie('hide_intro_message')) $pane.show();

        $hide.click(function (event) {
            event.preventDefault();
            cookie('hide_intro_message', true, cookieOptions);
            $pane.slideUp('slow');
        });

        $pane.hover(
            function () { $hide.fadeIn('fast'); },
            function () { $hide.fadeOut('fast'); });

      (function () {
        // Update "recently-viewed-repos" cookie for
        // the "repositories" drop-down.
        var
          id = BB.repo.id,
          cookieName = 'recently-viewed-repos_' + BB.user.id,
          rvr = cookie(cookieName),
          ids = rvr? rvr.split(','): [],
          idx = _.indexOf(ids, '' + id);

        // Remove `id` from `ids` if present.
        if (~idx) ids.splice(idx, 1);

        cookie(
          cookieName,
          // Insert `id` as the first item, then call
          // `join` on the resulting array to produce
          // something like "114694,27542,89002,84570".
          [id].concat(ids.slice(0, 4)).join(),
          {path: '/', expires: 1e6} // "never" expires
        );
      }());
    });
  </script>



  
  
  
  
  
    <div id="what-is-bitbucket" class="new-to-bitbucket">
      <h2>Petro Verkhogliad <span id="slogan">is sharing code with you</span></h2>
      <img src="https://bitbucket-assetroot.s3.amazonaws.com:443/c/photos/2008/Jul/20/petro_avatar.png" alt="" class="avatar" />
      <p>Bitbucket is a code hosting site. Unlimited public and private repositories. Free for small teams.</p>
      <div class="primary-action-link signup"><a href="/account/signup/?utm_source=internal&utm_medium=banner&utm_campaign=what_is_bitbucket">Try Bitbucket free</a></div>
      <a href="#hide" title="Don't show this again">Don't show this again</a>
    </div>
  


<div id="tabs">
  <ul class="tabs">
    <li>
      <a href="/vpetro/bsxpath/overview">Overview</a>
    </li>

    <li>
      <a href="/vpetro/bsxpath/downloads">Downloads (<span id="downloads-count">0</span>)</a>
    </li>

    

    <li>
      <a href="/vpetro/bsxpath/pull-requests">Pull requests (0)</a>
    </li>

    <li class="selected">
      
        <a href="/vpetro/bsxpath/src">Source</a>
      
    </li>

    <li>
      <a href="/vpetro/bsxpath/changesets">Commits</a>
    </li>

    <li id="wiki-tab" class="dropdown"
      style="display:
                        none  
        
      ">
      <a href="/vpetro/bsxpath/wiki">Wiki</a>
    </li>

    <li id="issues-tab" class="dropdown inertial-hover"
      style="display:
        block 
        
      ">
      <a href="/vpetro/bsxpath/issues?status=new&amp;status=open">Issues (0) &raquo;</a>
      <ul>
        <li><a href="/vpetro/bsxpath/issues/new">Create new issue</a></li>
        <li><a href="/vpetro/bsxpath/issues?status=new">New issues</a></li>
        <li><a href="/vpetro/bsxpath/issues?status=new&amp;status=open">Open issues</a></li>
        <li><a href="/vpetro/bsxpath/issues?status=duplicate&amp;status=invalid&amp;status=resolved&amp;status=wontfix">Closed issues</a></li>
        
        <li><a href="/vpetro/bsxpath/issues">All issues</a></li>
        <li><a href="/vpetro/bsxpath/issues/query">Advanced query</a></li>
      </ul>
    </li>

    

    <li class="secondary">
      <a href="/vpetro/bsxpath/descendants">Forks/queues (0)</a>
    </li>

    <li class="secondary">
      <a href="/vpetro/bsxpath/zealots">Followers (<span id="followers-count">1</span>)</a>
    </li>
  </ul>
</div>



 

  <div class="repo-menu" id="repo-menu">
    <ul id="repo-menu-links">
    
      <li>
        <a href="/vpetro/bsxpath/rss" class="rss" title="RSS feed for bsxpath">RSS</a>
      </li>

      <li><a href="/vpetro/bsxpath/fork" class="fork">fork</a></li>
      
        
          <li><a href="/vpetro/bsxpath/hack" class="patch-queue">patch queue</a></li>
        
      
      <li>
        <a rel="nofollow" href="/vpetro/bsxpath/follow" class="follow">follow</a>
      </li>
      
          
      
      
        <li class="get-source inertial-hover">
          <a class="source">get source</a>
          <ul class="downloads">
            
              
              <li><a rel="nofollow" href="/vpetro/bsxpath/get/b8565098c1e4.zip">zip</a></li>
              <li><a rel="nofollow" href="/vpetro/bsxpath/get/b8565098c1e4.tar.gz">gz</a></li>
              <li><a rel="nofollow" href="/vpetro/bsxpath/get/b8565098c1e4.tar.bz2">bz2</a></li>
            
          </ul>
        </li>
      
    </ul>

  
    <ul class="metadata">
      
      
        <li class="branches inertial-hover">branches
          <ul>
            <li><a href="/vpetro/bsxpath/src/b8565098c1e4">default</a>
              
              
            </li>
          </ul>
        </li>
      
      
      <li class="tags inertial-hover">tags
        <ul>
          <li><a href="/vpetro/bsxpath/src/b8565098c1e4">tip</a>
            
            </li>
        </ul>
      </li>
     
     
    </ul>
  
</div>

<div class="repo-menu" id="repo-desc">
  
    <ul id="repo-menu-links-mini">
      <li><a rel="nofollow" class="compare-link"
             href="/vpetro/bsxpath/compare/../"
             title="Show changes between bsxpath and "
             ></a></li>
      
  

      
      <li>
        <a href="/vpetro/bsxpath/rss" class="rss" title="RSS feed for bsxpath"></a>
      </li>

      <li><a href="/vpetro/bsxpath/fork" class="fork" title="Fork"></a></li>
      
        
          <li><a href="/vpetro/bsxpath/hack" class="patch-queue" title="Patch queue"></a></li>
        
      
      <li>
        <a rel="nofollow" href="/vpetro/bsxpath/follow" class="follow">follow</a>
      </li>
      
          
      
    
      
        <li>
          <a class="source" title="Get source"></a>
          <ul class="downloads">
            
              
                <li><a rel="nofollow" href="/vpetro/bsxpath/get/b8565098c1e4.zip">zip</a></li>
                <li><a rel="nofollow" href="/vpetro/bsxpath/get/b8565098c1e4.tar.gz">gz</a></li>
                <li><a rel="nofollow" href="/vpetro/bsxpath/get/b8565098c1e4.tar.bz2">bz2</a></li>
              
            
          </ul>
        </li>
      
    
    </ul>

    <h3 id="repo-heading" class="public">
      <a class="owner-username" href="/vpetro">vpetro</a> /
      <a class="repo-name" href="/vpetro/bsxpath">bsxpath</a>
    

    
    </h3>

        
        <p class="repo-desc-description">A plugin for BeautifulSoup developed by <a href="http://d.hatena.ne.jp/furyu-tei" rel="nofollow">http://d.hatena.ne.jp/furyu-tei</a> that enables the use of XPath.</p>
        

  <div id="repo-desc-cloneinfo">Clone this repository (size: 31.4 KB):
    <a href="https://bitbucket.org/vpetro/bsxpath" class="https">HTTPS</a> /
    <a href="ssh://hg@bitbucket.org/vpetro/bsxpath" class="ssh">SSH</a>
    <pre id="clone-url-https">hg clone https://bitbucket.org/vpetro/bsxpath</pre>
    <pre id="clone-url-ssh">hg clone ssh://hg@bitbucket.org/vpetro/bsxpath</pre>
    
  </div>

        <a href="#" id="toggle-repo-content"></a>

        

</div>




      

  <div id="source-path">
    <h1>
      <a href="/vpetro/bsxpath/src">bsxpath</a> /

  
    
      BSXPath.py
    
  

    </h1>
  </div>


  
  <div id="source-view">
    <div class="header">
      <ul class="metadata">
        <li><code>b8565098c1e4</code></li>
        <li>2691 loc</li>
        <li>75.9 KB</li>
      </ul>
      <ul class="source-view-links">
        
        <li><a id="embed-link" href="https://bitbucket.org/vpetro/bsxpath/src/b8565098c1e4/BSXPath.py?embed=t">embed</a></li>
        
        <li><a href="/vpetro/bsxpath/history/BSXPath.py">history</a></li>
        
        <li><a href="/vpetro/bsxpath/annotate/b8565098c1e4/BSXPath.py">annotate</a></li>
        
        <li><a href="/vpetro/bsxpath/raw/b8565098c1e4/BSXPath.py">raw</a></li>
        <li>
          <form action="/vpetro/bsxpath/diff/BSXPath.py" class="source-view-form">
          
            <input type="hidden" name="diff2" value="b8565098c1e4" />
            <select name="diff1">
            
              
            
            </select>
            <input type="submit" value="diff" />
          
          </form>
        </li>
      </ul>
    </div>
  
    <div>
    <table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#cl-1">   1</a>
<a href="#cl-2">   2</a>
<a href="#cl-3">   3</a>
<a href="#cl-4">   4</a>
<a href="#cl-5">   5</a>
<a href="#cl-6">   6</a>
<a href="#cl-7">   7</a>
<a href="#cl-8">   8</a>
<a href="#cl-9">   9</a>
<a href="#cl-10">  10</a>
<a href="#cl-11">  11</a>
<a href="#cl-12">  12</a>
<a href="#cl-13">  13</a>
<a href="#cl-14">  14</a>
<a href="#cl-15">  15</a>
<a href="#cl-16">  16</a>
<a href="#cl-17">  17</a>
<a href="#cl-18">  18</a>
<a href="#cl-19">  19</a>
<a href="#cl-20">  20</a>
<a href="#cl-21">  21</a>
<a href="#cl-22">  22</a>
<a href="#cl-23">  23</a>
<a href="#cl-24">  24</a>
<a href="#cl-25">  25</a>
<a href="#cl-26">  26</a>
<a href="#cl-27">  27</a>
<a href="#cl-28">  28</a>
<a href="#cl-29">  29</a>
<a href="#cl-30">  30</a>
<a href="#cl-31">  31</a>
<a href="#cl-32">  32</a>
<a href="#cl-33">  33</a>
<a href="#cl-34">  34</a>
<a href="#cl-35">  35</a>
<a href="#cl-36">  36</a>
<a href="#cl-37">  37</a>
<a href="#cl-38">  38</a>
<a href="#cl-39">  39</a>
<a href="#cl-40">  40</a>
<a href="#cl-41">  41</a>
<a href="#cl-42">  42</a>
<a href="#cl-43">  43</a>
<a href="#cl-44">  44</a>
<a href="#cl-45">  45</a>
<a href="#cl-46">  46</a>
<a href="#cl-47">  47</a>
<a href="#cl-48">  48</a>
<a href="#cl-49">  49</a>
<a href="#cl-50">  50</a>
<a href="#cl-51">  51</a>
<a href="#cl-52">  52</a>
<a href="#cl-53">  53</a>
<a href="#cl-54">  54</a>
<a href="#cl-55">  55</a>
<a href="#cl-56">  56</a>
<a href="#cl-57">  57</a>
<a href="#cl-58">  58</a>
<a href="#cl-59">  59</a>
<a href="#cl-60">  60</a>
<a href="#cl-61">  61</a>
<a href="#cl-62">  62</a>
<a href="#cl-63">  63</a>
<a href="#cl-64">  64</a>
<a href="#cl-65">  65</a>
<a href="#cl-66">  66</a>
<a href="#cl-67">  67</a>
<a href="#cl-68">  68</a>
<a href="#cl-69">  69</a>
<a href="#cl-70">  70</a>
<a href="#cl-71">  71</a>
<a href="#cl-72">  72</a>
<a href="#cl-73">  73</a>
<a href="#cl-74">  74</a>
<a href="#cl-75">  75</a>
<a href="#cl-76">  76</a>
<a href="#cl-77">  77</a>
<a href="#cl-78">  78</a>
<a href="#cl-79">  79</a>
<a href="#cl-80">  80</a>
<a href="#cl-81">  81</a>
<a href="#cl-82">  82</a>
<a href="#cl-83">  83</a>
<a href="#cl-84">  84</a>
<a href="#cl-85">  85</a>
<a href="#cl-86">  86</a>
<a href="#cl-87">  87</a>
<a href="#cl-88">  88</a>
<a href="#cl-89">  89</a>
<a href="#cl-90">  90</a>
<a href="#cl-91">  91</a>
<a href="#cl-92">  92</a>
<a href="#cl-93">  93</a>
<a href="#cl-94">  94</a>
<a href="#cl-95">  95</a>
<a href="#cl-96">  96</a>
<a href="#cl-97">  97</a>
<a href="#cl-98">  98</a>
<a href="#cl-99">  99</a>
<a href="#cl-100"> 100</a>
<a href="#cl-101"> 101</a>
<a href="#cl-102"> 102</a>
<a href="#cl-103"> 103</a>
<a href="#cl-104"> 104</a>
<a href="#cl-105"> 105</a>
<a href="#cl-106"> 106</a>
<a href="#cl-107"> 107</a>
<a href="#cl-108"> 108</a>
<a href="#cl-109"> 109</a>
<a href="#cl-110"> 110</a>
<a href="#cl-111"> 111</a>
<a href="#cl-112"> 112</a>
<a href="#cl-113"> 113</a>
<a href="#cl-114"> 114</a>
<a href="#cl-115"> 115</a>
<a href="#cl-116"> 116</a>
<a href="#cl-117"> 117</a>
<a href="#cl-118"> 118</a>
<a href="#cl-119"> 119</a>
<a href="#cl-120"> 120</a>
<a href="#cl-121"> 121</a>
<a href="#cl-122"> 122</a>
<a href="#cl-123"> 123</a>
<a href="#cl-124"> 124</a>
<a href="#cl-125"> 125</a>
<a href="#cl-126"> 126</a>
<a href="#cl-127"> 127</a>
<a href="#cl-128"> 128</a>
<a href="#cl-129"> 129</a>
<a href="#cl-130"> 130</a>
<a href="#cl-131"> 131</a>
<a href="#cl-132"> 132</a>
<a href="#cl-133"> 133</a>
<a href="#cl-134"> 134</a>
<a href="#cl-135"> 135</a>
<a href="#cl-136"> 136</a>
<a href="#cl-137"> 137</a>
<a href="#cl-138"> 138</a>
<a href="#cl-139"> 139</a>
<a href="#cl-140"> 140</a>
<a href="#cl-141"> 141</a>
<a href="#cl-142"> 142</a>
<a href="#cl-143"> 143</a>
<a href="#cl-144"> 144</a>
<a href="#cl-145"> 145</a>
<a href="#cl-146"> 146</a>
<a href="#cl-147"> 147</a>
<a href="#cl-148"> 148</a>
<a href="#cl-149"> 149</a>
<a href="#cl-150"> 150</a>
<a href="#cl-151"> 151</a>
<a href="#cl-152"> 152</a>
<a href="#cl-153"> 153</a>
<a href="#cl-154"> 154</a>
<a href="#cl-155"> 155</a>
<a href="#cl-156"> 156</a>
<a href="#cl-157"> 157</a>
<a href="#cl-158"> 158</a>
<a href="#cl-159"> 159</a>
<a href="#cl-160"> 160</a>
<a href="#cl-161"> 161</a>
<a href="#cl-162"> 162</a>
<a href="#cl-163"> 163</a>
<a href="#cl-164"> 164</a>
<a href="#cl-165"> 165</a>
<a href="#cl-166"> 166</a>
<a href="#cl-167"> 167</a>
<a href="#cl-168"> 168</a>
<a href="#cl-169"> 169</a>
<a href="#cl-170"> 170</a>
<a href="#cl-171"> 171</a>
<a href="#cl-172"> 172</a>
<a href="#cl-173"> 173</a>
<a href="#cl-174"> 174</a>
<a href="#cl-175"> 175</a>
<a href="#cl-176"> 176</a>
<a href="#cl-177"> 177</a>
<a href="#cl-178"> 178</a>
<a href="#cl-179"> 179</a>
<a href="#cl-180"> 180</a>
<a href="#cl-181"> 181</a>
<a href="#cl-182"> 182</a>
<a href="#cl-183"> 183</a>
<a href="#cl-184"> 184</a>
<a href="#cl-185"> 185</a>
<a href="#cl-186"> 186</a>
<a href="#cl-187"> 187</a>
<a href="#cl-188"> 188</a>
<a href="#cl-189"> 189</a>
<a href="#cl-190"> 190</a>
<a href="#cl-191"> 191</a>
<a href="#cl-192"> 192</a>
<a href="#cl-193"> 193</a>
<a href="#cl-194"> 194</a>
<a href="#cl-195"> 195</a>
<a href="#cl-196"> 196</a>
<a href="#cl-197"> 197</a>
<a href="#cl-198"> 198</a>
<a href="#cl-199"> 199</a>
<a href="#cl-200"> 200</a>
<a href="#cl-201"> 201</a>
<a href="#cl-202"> 202</a>
<a href="#cl-203"> 203</a>
<a href="#cl-204"> 204</a>
<a href="#cl-205"> 205</a>
<a href="#cl-206"> 206</a>
<a href="#cl-207"> 207</a>
<a href="#cl-208"> 208</a>
<a href="#cl-209"> 209</a>
<a href="#cl-210"> 210</a>
<a href="#cl-211"> 211</a>
<a href="#cl-212"> 212</a>
<a href="#cl-213"> 213</a>
<a href="#cl-214"> 214</a>
<a href="#cl-215"> 215</a>
<a href="#cl-216"> 216</a>
<a href="#cl-217"> 217</a>
<a href="#cl-218"> 218</a>
<a href="#cl-219"> 219</a>
<a href="#cl-220"> 220</a>
<a href="#cl-221"> 221</a>
<a href="#cl-222"> 222</a>
<a href="#cl-223"> 223</a>
<a href="#cl-224"> 224</a>
<a href="#cl-225"> 225</a>
<a href="#cl-226"> 226</a>
<a href="#cl-227"> 227</a>
<a href="#cl-228"> 228</a>
<a href="#cl-229"> 229</a>
<a href="#cl-230"> 230</a>
<a href="#cl-231"> 231</a>
<a href="#cl-232"> 232</a>
<a href="#cl-233"> 233</a>
<a href="#cl-234"> 234</a>
<a href="#cl-235"> 235</a>
<a href="#cl-236"> 236</a>
<a href="#cl-237"> 237</a>
<a href="#cl-238"> 238</a>
<a href="#cl-239"> 239</a>
<a href="#cl-240"> 240</a>
<a href="#cl-241"> 241</a>
<a href="#cl-242"> 242</a>
<a href="#cl-243"> 243</a>
<a href="#cl-244"> 244</a>
<a href="#cl-245"> 245</a>
<a href="#cl-246"> 246</a>
<a href="#cl-247"> 247</a>
<a href="#cl-248"> 248</a>
<a href="#cl-249"> 249</a>
<a href="#cl-250"> 250</a>
<a href="#cl-251"> 251</a>
<a href="#cl-252"> 252</a>
<a href="#cl-253"> 253</a>
<a href="#cl-254"> 254</a>
<a href="#cl-255"> 255</a>
<a href="#cl-256"> 256</a>
<a href="#cl-257"> 257</a>
<a href="#cl-258"> 258</a>
<a href="#cl-259"> 259</a>
<a href="#cl-260"> 260</a>
<a href="#cl-261"> 261</a>
<a href="#cl-262"> 262</a>
<a href="#cl-263"> 263</a>
<a href="#cl-264"> 264</a>
<a href="#cl-265"> 265</a>
<a href="#cl-266"> 266</a>
<a href="#cl-267"> 267</a>
<a href="#cl-268"> 268</a>
<a href="#cl-269"> 269</a>
<a href="#cl-270"> 270</a>
<a href="#cl-271"> 271</a>
<a href="#cl-272"> 272</a>
<a href="#cl-273"> 273</a>
<a href="#cl-274"> 274</a>
<a href="#cl-275"> 275</a>
<a href="#cl-276"> 276</a>
<a href="#cl-277"> 277</a>
<a href="#cl-278"> 278</a>
<a href="#cl-279"> 279</a>
<a href="#cl-280"> 280</a>
<a href="#cl-281"> 281</a>
<a href="#cl-282"> 282</a>
<a href="#cl-283"> 283</a>
<a href="#cl-284"> 284</a>
<a href="#cl-285"> 285</a>
<a href="#cl-286"> 286</a>
<a href="#cl-287"> 287</a>
<a href="#cl-288"> 288</a>
<a href="#cl-289"> 289</a>
<a href="#cl-290"> 290</a>
<a href="#cl-291"> 291</a>
<a href="#cl-292"> 292</a>
<a href="#cl-293"> 293</a>
<a href="#cl-294"> 294</a>
<a href="#cl-295"> 295</a>
<a href="#cl-296"> 296</a>
<a href="#cl-297"> 297</a>
<a href="#cl-298"> 298</a>
<a href="#cl-299"> 299</a>
<a href="#cl-300"> 300</a>
<a href="#cl-301"> 301</a>
<a href="#cl-302"> 302</a>
<a href="#cl-303"> 303</a>
<a href="#cl-304"> 304</a>
<a href="#cl-305"> 305</a>
<a href="#cl-306"> 306</a>
<a href="#cl-307"> 307</a>
<a href="#cl-308"> 308</a>
<a href="#cl-309"> 309</a>
<a href="#cl-310"> 310</a>
<a href="#cl-311"> 311</a>
<a href="#cl-312"> 312</a>
<a href="#cl-313"> 313</a>
<a href="#cl-314"> 314</a>
<a href="#cl-315"> 315</a>
<a href="#cl-316"> 316</a>
<a href="#cl-317"> 317</a>
<a href="#cl-318"> 318</a>
<a href="#cl-319"> 319</a>
<a href="#cl-320"> 320</a>
<a href="#cl-321"> 321</a>
<a href="#cl-322"> 322</a>
<a href="#cl-323"> 323</a>
<a href="#cl-324"> 324</a>
<a href="#cl-325"> 325</a>
<a href="#cl-326"> 326</a>
<a href="#cl-327"> 327</a>
<a href="#cl-328"> 328</a>
<a href="#cl-329"> 329</a>
<a href="#cl-330"> 330</a>
<a href="#cl-331"> 331</a>
<a href="#cl-332"> 332</a>
<a href="#cl-333"> 333</a>
<a href="#cl-334"> 334</a>
<a href="#cl-335"> 335</a>
<a href="#cl-336"> 336</a>
<a href="#cl-337"> 337</a>
<a href="#cl-338"> 338</a>
<a href="#cl-339"> 339</a>
<a href="#cl-340"> 340</a>
<a href="#cl-341"> 341</a>
<a href="#cl-342"> 342</a>
<a href="#cl-343"> 343</a>
<a href="#cl-344"> 344</a>
<a href="#cl-345"> 345</a>
<a href="#cl-346"> 346</a>
<a href="#cl-347"> 347</a>
<a href="#cl-348"> 348</a>
<a href="#cl-349"> 349</a>
<a href="#cl-350"> 350</a>
<a href="#cl-351"> 351</a>
<a href="#cl-352"> 352</a>
<a href="#cl-353"> 353</a>
<a href="#cl-354"> 354</a>
<a href="#cl-355"> 355</a>
<a href="#cl-356"> 356</a>
<a href="#cl-357"> 357</a>
<a href="#cl-358"> 358</a>
<a href="#cl-359"> 359</a>
<a href="#cl-360"> 360</a>
<a href="#cl-361"> 361</a>
<a href="#cl-362"> 362</a>
<a href="#cl-363"> 363</a>
<a href="#cl-364"> 364</a>
<a href="#cl-365"> 365</a>
<a href="#cl-366"> 366</a>
<a href="#cl-367"> 367</a>
<a href="#cl-368"> 368</a>
<a href="#cl-369"> 369</a>
<a href="#cl-370"> 370</a>
<a href="#cl-371"> 371</a>
<a href="#cl-372"> 372</a>
<a href="#cl-373"> 373</a>
<a href="#cl-374"> 374</a>
<a href="#cl-375"> 375</a>
<a href="#cl-376"> 376</a>
<a href="#cl-377"> 377</a>
<a href="#cl-378"> 378</a>
<a href="#cl-379"> 379</a>
<a href="#cl-380"> 380</a>
<a href="#cl-381"> 381</a>
<a href="#cl-382"> 382</a>
<a href="#cl-383"> 383</a>
<a href="#cl-384"> 384</a>
<a href="#cl-385"> 385</a>
<a href="#cl-386"> 386</a>
<a href="#cl-387"> 387</a>
<a href="#cl-388"> 388</a>
<a href="#cl-389"> 389</a>
<a href="#cl-390"> 390</a>
<a href="#cl-391"> 391</a>
<a href="#cl-392"> 392</a>
<a href="#cl-393"> 393</a>
<a href="#cl-394"> 394</a>
<a href="#cl-395"> 395</a>
<a href="#cl-396"> 396</a>
<a href="#cl-397"> 397</a>
<a href="#cl-398"> 398</a>
<a href="#cl-399"> 399</a>
<a href="#cl-400"> 400</a>
<a href="#cl-401"> 401</a>
<a href="#cl-402"> 402</a>
<a href="#cl-403"> 403</a>
<a href="#cl-404"> 404</a>
<a href="#cl-405"> 405</a>
<a href="#cl-406"> 406</a>
<a href="#cl-407"> 407</a>
<a href="#cl-408"> 408</a>
<a href="#cl-409"> 409</a>
<a href="#cl-410"> 410</a>
<a href="#cl-411"> 411</a>
<a href="#cl-412"> 412</a>
<a href="#cl-413"> 413</a>
<a href="#cl-414"> 414</a>
<a href="#cl-415"> 415</a>
<a href="#cl-416"> 416</a>
<a href="#cl-417"> 417</a>
<a href="#cl-418"> 418</a>
<a href="#cl-419"> 419</a>
<a href="#cl-420"> 420</a>
<a href="#cl-421"> 421</a>
<a href="#cl-422"> 422</a>
<a href="#cl-423"> 423</a>
<a href="#cl-424"> 424</a>
<a href="#cl-425"> 425</a>
<a href="#cl-426"> 426</a>
<a href="#cl-427"> 427</a>
<a href="#cl-428"> 428</a>
<a href="#cl-429"> 429</a>
<a href="#cl-430"> 430</a>
<a href="#cl-431"> 431</a>
<a href="#cl-432"> 432</a>
<a href="#cl-433"> 433</a>
<a href="#cl-434"> 434</a>
<a href="#cl-435"> 435</a>
<a href="#cl-436"> 436</a>
<a href="#cl-437"> 437</a>
<a href="#cl-438"> 438</a>
<a href="#cl-439"> 439</a>
<a href="#cl-440"> 440</a>
<a href="#cl-441"> 441</a>
<a href="#cl-442"> 442</a>
<a href="#cl-443"> 443</a>
<a href="#cl-444"> 444</a>
<a href="#cl-445"> 445</a>
<a href="#cl-446"> 446</a>
<a href="#cl-447"> 447</a>
<a href="#cl-448"> 448</a>
<a href="#cl-449"> 449</a>
<a href="#cl-450"> 450</a>
<a href="#cl-451"> 451</a>
<a href="#cl-452"> 452</a>
<a href="#cl-453"> 453</a>
<a href="#cl-454"> 454</a>
<a href="#cl-455"> 455</a>
<a href="#cl-456"> 456</a>
<a href="#cl-457"> 457</a>
<a href="#cl-458"> 458</a>
<a href="#cl-459"> 459</a>
<a href="#cl-460"> 460</a>
<a href="#cl-461"> 461</a>
<a href="#cl-462"> 462</a>
<a href="#cl-463"> 463</a>
<a href="#cl-464"> 464</a>
<a href="#cl-465"> 465</a>
<a href="#cl-466"> 466</a>
<a href="#cl-467"> 467</a>
<a href="#cl-468"> 468</a>
<a href="#cl-469"> 469</a>
<a href="#cl-470"> 470</a>
<a href="#cl-471"> 471</a>
<a href="#cl-472"> 472</a>
<a href="#cl-473"> 473</a>
<a href="#cl-474"> 474</a>
<a href="#cl-475"> 475</a>
<a href="#cl-476"> 476</a>
<a href="#cl-477"> 477</a>
<a href="#cl-478"> 478</a>
<a href="#cl-479"> 479</a>
<a href="#cl-480"> 480</a>
<a href="#cl-481"> 481</a>
<a href="#cl-482"> 482</a>
<a href="#cl-483"> 483</a>
<a href="#cl-484"> 484</a>
<a href="#cl-485"> 485</a>
<a href="#cl-486"> 486</a>
<a href="#cl-487"> 487</a>
<a href="#cl-488"> 488</a>
<a href="#cl-489"> 489</a>
<a href="#cl-490"> 490</a>
<a href="#cl-491"> 491</a>
<a href="#cl-492"> 492</a>
<a href="#cl-493"> 493</a>
<a href="#cl-494"> 494</a>
<a href="#cl-495"> 495</a>
<a href="#cl-496"> 496</a>
<a href="#cl-497"> 497</a>
<a href="#cl-498"> 498</a>
<a href="#cl-499"> 499</a>
<a href="#cl-500"> 500</a>
<a href="#cl-501"> 501</a>
<a href="#cl-502"> 502</a>
<a href="#cl-503"> 503</a>
<a href="#cl-504"> 504</a>
<a href="#cl-505"> 505</a>
<a href="#cl-506"> 506</a>
<a href="#cl-507"> 507</a>
<a href="#cl-508"> 508</a>
<a href="#cl-509"> 509</a>
<a href="#cl-510"> 510</a>
<a href="#cl-511"> 511</a>
<a href="#cl-512"> 512</a>
<a href="#cl-513"> 513</a>
<a href="#cl-514"> 514</a>
<a href="#cl-515"> 515</a>
<a href="#cl-516"> 516</a>
<a href="#cl-517"> 517</a>
<a href="#cl-518"> 518</a>
<a href="#cl-519"> 519</a>
<a href="#cl-520"> 520</a>
<a href="#cl-521"> 521</a>
<a href="#cl-522"> 522</a>
<a href="#cl-523"> 523</a>
<a href="#cl-524"> 524</a>
<a href="#cl-525"> 525</a>
<a href="#cl-526"> 526</a>
<a href="#cl-527"> 527</a>
<a href="#cl-528"> 528</a>
<a href="#cl-529"> 529</a>
<a href="#cl-530"> 530</a>
<a href="#cl-531"> 531</a>
<a href="#cl-532"> 532</a>
<a href="#cl-533"> 533</a>
<a href="#cl-534"> 534</a>
<a href="#cl-535"> 535</a>
<a href="#cl-536"> 536</a>
<a href="#cl-537"> 537</a>
<a href="#cl-538"> 538</a>
<a href="#cl-539"> 539</a>
<a href="#cl-540"> 540</a>
<a href="#cl-541"> 541</a>
<a href="#cl-542"> 542</a>
<a href="#cl-543"> 543</a>
<a href="#cl-544"> 544</a>
<a href="#cl-545"> 545</a>
<a href="#cl-546"> 546</a>
<a href="#cl-547"> 547</a>
<a href="#cl-548"> 548</a>
<a href="#cl-549"> 549</a>
<a href="#cl-550"> 550</a>
<a href="#cl-551"> 551</a>
<a href="#cl-552"> 552</a>
<a href="#cl-553"> 553</a>
<a href="#cl-554"> 554</a>
<a href="#cl-555"> 555</a>
<a href="#cl-556"> 556</a>
<a href="#cl-557"> 557</a>
<a href="#cl-558"> 558</a>
<a href="#cl-559"> 559</a>
<a href="#cl-560"> 560</a>
<a href="#cl-561"> 561</a>
<a href="#cl-562"> 562</a>
<a href="#cl-563"> 563</a>
<a href="#cl-564"> 564</a>
<a href="#cl-565"> 565</a>
<a href="#cl-566"> 566</a>
<a href="#cl-567"> 567</a>
<a href="#cl-568"> 568</a>
<a href="#cl-569"> 569</a>
<a href="#cl-570"> 570</a>
<a href="#cl-571"> 571</a>
<a href="#cl-572"> 572</a>
<a href="#cl-573"> 573</a>
<a href="#cl-574"> 574</a>
<a href="#cl-575"> 575</a>
<a href="#cl-576"> 576</a>
<a href="#cl-577"> 577</a>
<a href="#cl-578"> 578</a>
<a href="#cl-579"> 579</a>
<a href="#cl-580"> 580</a>
<a href="#cl-581"> 581</a>
<a href="#cl-582"> 582</a>
<a href="#cl-583"> 583</a>
<a href="#cl-584"> 584</a>
<a href="#cl-585"> 585</a>
<a href="#cl-586"> 586</a>
<a href="#cl-587"> 587</a>
<a href="#cl-588"> 588</a>
<a href="#cl-589"> 589</a>
<a href="#cl-590"> 590</a>
<a href="#cl-591"> 591</a>
<a href="#cl-592"> 592</a>
<a href="#cl-593"> 593</a>
<a href="#cl-594"> 594</a>
<a href="#cl-595"> 595</a>
<a href="#cl-596"> 596</a>
<a href="#cl-597"> 597</a>
<a href="#cl-598"> 598</a>
<a href="#cl-599"> 599</a>
<a href="#cl-600"> 600</a>
<a href="#cl-601"> 601</a>
<a href="#cl-602"> 602</a>
<a href="#cl-603"> 603</a>
<a href="#cl-604"> 604</a>
<a href="#cl-605"> 605</a>
<a href="#cl-606"> 606</a>
<a href="#cl-607"> 607</a>
<a href="#cl-608"> 608</a>
<a href="#cl-609"> 609</a>
<a href="#cl-610"> 610</a>
<a href="#cl-611"> 611</a>
<a href="#cl-612"> 612</a>
<a href="#cl-613"> 613</a>
<a href="#cl-614"> 614</a>
<a href="#cl-615"> 615</a>
<a href="#cl-616"> 616</a>
<a href="#cl-617"> 617</a>
<a href="#cl-618"> 618</a>
<a href="#cl-619"> 619</a>
<a href="#cl-620"> 620</a>
<a href="#cl-621"> 621</a>
<a href="#cl-622"> 622</a>
<a href="#cl-623"> 623</a>
<a href="#cl-624"> 624</a>
<a href="#cl-625"> 625</a>
<a href="#cl-626"> 626</a>
<a href="#cl-627"> 627</a>
<a href="#cl-628"> 628</a>
<a href="#cl-629"> 629</a>
<a href="#cl-630"> 630</a>
<a href="#cl-631"> 631</a>
<a href="#cl-632"> 632</a>
<a href="#cl-633"> 633</a>
<a href="#cl-634"> 634</a>
<a href="#cl-635"> 635</a>
<a href="#cl-636"> 636</a>
<a href="#cl-637"> 637</a>
<a href="#cl-638"> 638</a>
<a href="#cl-639"> 639</a>
<a href="#cl-640"> 640</a>
<a href="#cl-641"> 641</a>
<a href="#cl-642"> 642</a>
<a href="#cl-643"> 643</a>
<a href="#cl-644"> 644</a>
<a href="#cl-645"> 645</a>
<a href="#cl-646"> 646</a>
<a href="#cl-647"> 647</a>
<a href="#cl-648"> 648</a>
<a href="#cl-649"> 649</a>
<a href="#cl-650"> 650</a>
<a href="#cl-651"> 651</a>
<a href="#cl-652"> 652</a>
<a href="#cl-653"> 653</a>
<a href="#cl-654"> 654</a>
<a href="#cl-655"> 655</a>
<a href="#cl-656"> 656</a>
<a href="#cl-657"> 657</a>
<a href="#cl-658"> 658</a>
<a href="#cl-659"> 659</a>
<a href="#cl-660"> 660</a>
<a href="#cl-661"> 661</a>
<a href="#cl-662"> 662</a>
<a href="#cl-663"> 663</a>
<a href="#cl-664"> 664</a>
<a href="#cl-665"> 665</a>
<a href="#cl-666"> 666</a>
<a href="#cl-667"> 667</a>
<a href="#cl-668"> 668</a>
<a href="#cl-669"> 669</a>
<a href="#cl-670"> 670</a>
<a href="#cl-671"> 671</a>
<a href="#cl-672"> 672</a>
<a href="#cl-673"> 673</a>
<a href="#cl-674"> 674</a>
<a href="#cl-675"> 675</a>
<a href="#cl-676"> 676</a>
<a href="#cl-677"> 677</a>
<a href="#cl-678"> 678</a>
<a href="#cl-679"> 679</a>
<a href="#cl-680"> 680</a>
<a href="#cl-681"> 681</a>
<a href="#cl-682"> 682</a>
<a href="#cl-683"> 683</a>
<a href="#cl-684"> 684</a>
<a href="#cl-685"> 685</a>
<a href="#cl-686"> 686</a>
<a href="#cl-687"> 687</a>
<a href="#cl-688"> 688</a>
<a href="#cl-689"> 689</a>
<a href="#cl-690"> 690</a>
<a href="#cl-691"> 691</a>
<a href="#cl-692"> 692</a>
<a href="#cl-693"> 693</a>
<a href="#cl-694"> 694</a>
<a href="#cl-695"> 695</a>
<a href="#cl-696"> 696</a>
<a href="#cl-697"> 697</a>
<a href="#cl-698"> 698</a>
<a href="#cl-699"> 699</a>
<a href="#cl-700"> 700</a>
<a href="#cl-701"> 701</a>
<a href="#cl-702"> 702</a>
<a href="#cl-703"> 703</a>
<a href="#cl-704"> 704</a>
<a href="#cl-705"> 705</a>
<a href="#cl-706"> 706</a>
<a href="#cl-707"> 707</a>
<a href="#cl-708"> 708</a>
<a href="#cl-709"> 709</a>
<a href="#cl-710"> 710</a>
<a href="#cl-711"> 711</a>
<a href="#cl-712"> 712</a>
<a href="#cl-713"> 713</a>
<a href="#cl-714"> 714</a>
<a href="#cl-715"> 715</a>
<a href="#cl-716"> 716</a>
<a href="#cl-717"> 717</a>
<a href="#cl-718"> 718</a>
<a href="#cl-719"> 719</a>
<a href="#cl-720"> 720</a>
<a href="#cl-721"> 721</a>
<a href="#cl-722"> 722</a>
<a href="#cl-723"> 723</a>
<a href="#cl-724"> 724</a>
<a href="#cl-725"> 725</a>
<a href="#cl-726"> 726</a>
<a href="#cl-727"> 727</a>
<a href="#cl-728"> 728</a>
<a href="#cl-729"> 729</a>
<a href="#cl-730"> 730</a>
<a href="#cl-731"> 731</a>
<a href="#cl-732"> 732</a>
<a href="#cl-733"> 733</a>
<a href="#cl-734"> 734</a>
<a href="#cl-735"> 735</a>
<a href="#cl-736"> 736</a>
<a href="#cl-737"> 737</a>
<a href="#cl-738"> 738</a>
<a href="#cl-739"> 739</a>
<a href="#cl-740"> 740</a>
<a href="#cl-741"> 741</a>
<a href="#cl-742"> 742</a>
<a href="#cl-743"> 743</a>
<a href="#cl-744"> 744</a>
<a href="#cl-745"> 745</a>
<a href="#cl-746"> 746</a>
<a href="#cl-747"> 747</a>
<a href="#cl-748"> 748</a>
<a href="#cl-749"> 749</a>
<a href="#cl-750"> 750</a>
<a href="#cl-751"> 751</a>
<a href="#cl-752"> 752</a>
<a href="#cl-753"> 753</a>
<a href="#cl-754"> 754</a>
<a href="#cl-755"> 755</a>
<a href="#cl-756"> 756</a>
<a href="#cl-757"> 757</a>
<a href="#cl-758"> 758</a>
<a href="#cl-759"> 759</a>
<a href="#cl-760"> 760</a>
<a href="#cl-761"> 761</a>
<a href="#cl-762"> 762</a>
<a href="#cl-763"> 763</a>
<a href="#cl-764"> 764</a>
<a href="#cl-765"> 765</a>
<a href="#cl-766"> 766</a>
<a href="#cl-767"> 767</a>
<a href="#cl-768"> 768</a>
<a href="#cl-769"> 769</a>
<a href="#cl-770"> 770</a>
<a href="#cl-771"> 771</a>
<a href="#cl-772"> 772</a>
<a href="#cl-773"> 773</a>
<a href="#cl-774"> 774</a>
<a href="#cl-775"> 775</a>
<a href="#cl-776"> 776</a>
<a href="#cl-777"> 777</a>
<a href="#cl-778"> 778</a>
<a href="#cl-779"> 779</a>
<a href="#cl-780"> 780</a>
<a href="#cl-781"> 781</a>
<a href="#cl-782"> 782</a>
<a href="#cl-783"> 783</a>
<a href="#cl-784"> 784</a>
<a href="#cl-785"> 785</a>
<a href="#cl-786"> 786</a>
<a href="#cl-787"> 787</a>
<a href="#cl-788"> 788</a>
<a href="#cl-789"> 789</a>
<a href="#cl-790"> 790</a>
<a href="#cl-791"> 791</a>
<a href="#cl-792"> 792</a>
<a href="#cl-793"> 793</a>
<a href="#cl-794"> 794</a>
<a href="#cl-795"> 795</a>
<a href="#cl-796"> 796</a>
<a href="#cl-797"> 797</a>
<a href="#cl-798"> 798</a>
<a href="#cl-799"> 799</a>
<a href="#cl-800"> 800</a>
<a href="#cl-801"> 801</a>
<a href="#cl-802"> 802</a>
<a href="#cl-803"> 803</a>
<a href="#cl-804"> 804</a>
<a href="#cl-805"> 805</a>
<a href="#cl-806"> 806</a>
<a href="#cl-807"> 807</a>
<a href="#cl-808"> 808</a>
<a href="#cl-809"> 809</a>
<a href="#cl-810"> 810</a>
<a href="#cl-811"> 811</a>
<a href="#cl-812"> 812</a>
<a href="#cl-813"> 813</a>
<a href="#cl-814"> 814</a>
<a href="#cl-815"> 815</a>
<a href="#cl-816"> 816</a>
<a href="#cl-817"> 817</a>
<a href="#cl-818"> 818</a>
<a href="#cl-819"> 819</a>
<a href="#cl-820"> 820</a>
<a href="#cl-821"> 821</a>
<a href="#cl-822"> 822</a>
<a href="#cl-823"> 823</a>
<a href="#cl-824"> 824</a>
<a href="#cl-825"> 825</a>
<a href="#cl-826"> 826</a>
<a href="#cl-827"> 827</a>
<a href="#cl-828"> 828</a>
<a href="#cl-829"> 829</a>
<a href="#cl-830"> 830</a>
<a href="#cl-831"> 831</a>
<a href="#cl-832"> 832</a>
<a href="#cl-833"> 833</a>
<a href="#cl-834"> 834</a>
<a href="#cl-835"> 835</a>
<a href="#cl-836"> 836</a>
<a href="#cl-837"> 837</a>
<a href="#cl-838"> 838</a>
<a href="#cl-839"> 839</a>
<a href="#cl-840"> 840</a>
<a href="#cl-841"> 841</a>
<a href="#cl-842"> 842</a>
<a href="#cl-843"> 843</a>
<a href="#cl-844"> 844</a>
<a href="#cl-845"> 845</a>
<a href="#cl-846"> 846</a>
<a href="#cl-847"> 847</a>
<a href="#cl-848"> 848</a>
<a href="#cl-849"> 849</a>
<a href="#cl-850"> 850</a>
<a href="#cl-851"> 851</a>
<a href="#cl-852"> 852</a>
<a href="#cl-853"> 853</a>
<a href="#cl-854"> 854</a>
<a href="#cl-855"> 855</a>
<a href="#cl-856"> 856</a>
<a href="#cl-857"> 857</a>
<a href="#cl-858"> 858</a>
<a href="#cl-859"> 859</a>
<a href="#cl-860"> 860</a>
<a href="#cl-861"> 861</a>
<a href="#cl-862"> 862</a>
<a href="#cl-863"> 863</a>
<a href="#cl-864"> 864</a>
<a href="#cl-865"> 865</a>
<a href="#cl-866"> 866</a>
<a href="#cl-867"> 867</a>
<a href="#cl-868"> 868</a>
<a href="#cl-869"> 869</a>
<a href="#cl-870"> 870</a>
<a href="#cl-871"> 871</a>
<a href="#cl-872"> 872</a>
<a href="#cl-873"> 873</a>
<a href="#cl-874"> 874</a>
<a href="#cl-875"> 875</a>
<a href="#cl-876"> 876</a>
<a href="#cl-877"> 877</a>
<a href="#cl-878"> 878</a>
<a href="#cl-879"> 879</a>
<a href="#cl-880"> 880</a>
<a href="#cl-881"> 881</a>
<a href="#cl-882"> 882</a>
<a href="#cl-883"> 883</a>
<a href="#cl-884"> 884</a>
<a href="#cl-885"> 885</a>
<a href="#cl-886"> 886</a>
<a href="#cl-887"> 887</a>
<a href="#cl-888"> 888</a>
<a href="#cl-889"> 889</a>
<a href="#cl-890"> 890</a>
<a href="#cl-891"> 891</a>
<a href="#cl-892"> 892</a>
<a href="#cl-893"> 893</a>
<a href="#cl-894"> 894</a>
<a href="#cl-895"> 895</a>
<a href="#cl-896"> 896</a>
<a href="#cl-897"> 897</a>
<a href="#cl-898"> 898</a>
<a href="#cl-899"> 899</a>
<a href="#cl-900"> 900</a>
<a href="#cl-901"> 901</a>
<a href="#cl-902"> 902</a>
<a href="#cl-903"> 903</a>
<a href="#cl-904"> 904</a>
<a href="#cl-905"> 905</a>
<a href="#cl-906"> 906</a>
<a href="#cl-907"> 907</a>
<a href="#cl-908"> 908</a>
<a href="#cl-909"> 909</a>
<a href="#cl-910"> 910</a>
<a href="#cl-911"> 911</a>
<a href="#cl-912"> 912</a>
<a href="#cl-913"> 913</a>
<a href="#cl-914"> 914</a>
<a href="#cl-915"> 915</a>
<a href="#cl-916"> 916</a>
<a href="#cl-917"> 917</a>
<a href="#cl-918"> 918</a>
<a href="#cl-919"> 919</a>
<a href="#cl-920"> 920</a>
<a href="#cl-921"> 921</a>
<a href="#cl-922"> 922</a>
<a href="#cl-923"> 923</a>
<a href="#cl-924"> 924</a>
<a href="#cl-925"> 925</a>
<a href="#cl-926"> 926</a>
<a href="#cl-927"> 927</a>
<a href="#cl-928"> 928</a>
<a href="#cl-929"> 929</a>
<a href="#cl-930"> 930</a>
<a href="#cl-931"> 931</a>
<a href="#cl-932"> 932</a>
<a href="#cl-933"> 933</a>
<a href="#cl-934"> 934</a>
<a href="#cl-935"> 935</a>
<a href="#cl-936"> 936</a>
<a href="#cl-937"> 937</a>
<a href="#cl-938"> 938</a>
<a href="#cl-939"> 939</a>
<a href="#cl-940"> 940</a>
<a href="#cl-941"> 941</a>
<a href="#cl-942"> 942</a>
<a href="#cl-943"> 943</a>
<a href="#cl-944"> 944</a>
<a href="#cl-945"> 945</a>
<a href="#cl-946"> 946</a>
<a href="#cl-947"> 947</a>
<a href="#cl-948"> 948</a>
<a href="#cl-949"> 949</a>
<a href="#cl-950"> 950</a>
<a href="#cl-951"> 951</a>
<a href="#cl-952"> 952</a>
<a href="#cl-953"> 953</a>
<a href="#cl-954"> 954</a>
<a href="#cl-955"> 955</a>
<a href="#cl-956"> 956</a>
<a href="#cl-957"> 957</a>
<a href="#cl-958"> 958</a>
<a href="#cl-959"> 959</a>
<a href="#cl-960"> 960</a>
<a href="#cl-961"> 961</a>
<a href="#cl-962"> 962</a>
<a href="#cl-963"> 963</a>
<a href="#cl-964"> 964</a>
<a href="#cl-965"> 965</a>
<a href="#cl-966"> 966</a>
<a href="#cl-967"> 967</a>
<a href="#cl-968"> 968</a>
<a href="#cl-969"> 969</a>
<a href="#cl-970"> 970</a>
<a href="#cl-971"> 971</a>
<a href="#cl-972"> 972</a>
<a href="#cl-973"> 973</a>
<a href="#cl-974"> 974</a>
<a href="#cl-975"> 975</a>
<a href="#cl-976"> 976</a>
<a href="#cl-977"> 977</a>
<a href="#cl-978"> 978</a>
<a href="#cl-979"> 979</a>
<a href="#cl-980"> 980</a>
<a href="#cl-981"> 981</a>
<a href="#cl-982"> 982</a>
<a href="#cl-983"> 983</a>
<a href="#cl-984"> 984</a>
<a href="#cl-985"> 985</a>
<a href="#cl-986"> 986</a>
<a href="#cl-987"> 987</a>
<a href="#cl-988"> 988</a>
<a href="#cl-989"> 989</a>
<a href="#cl-990"> 990</a>
<a href="#cl-991"> 991</a>
<a href="#cl-992"> 992</a>
<a href="#cl-993"> 993</a>
<a href="#cl-994"> 994</a>
<a href="#cl-995"> 995</a>
<a href="#cl-996"> 996</a>
<a href="#cl-997"> 997</a>
<a href="#cl-998"> 998</a>
<a href="#cl-999"> 999</a>
<a href="#cl-1000">1000</a>
<a href="#cl-1001">1001</a>
<a href="#cl-1002">1002</a>
<a href="#cl-1003">1003</a>
<a href="#cl-1004">1004</a>
<a href="#cl-1005">1005</a>
<a href="#cl-1006">1006</a>
<a href="#cl-1007">1007</a>
<a href="#cl-1008">1008</a>
<a href="#cl-1009">1009</a>
<a href="#cl-1010">1010</a>
<a href="#cl-1011">1011</a>
<a href="#cl-1012">1012</a>
<a href="#cl-1013">1013</a>
<a href="#cl-1014">1014</a>
<a href="#cl-1015">1015</a>
<a href="#cl-1016">1016</a>
<a href="#cl-1017">1017</a>
<a href="#cl-1018">1018</a>
<a href="#cl-1019">1019</a>
<a href="#cl-1020">1020</a>
<a href="#cl-1021">1021</a>
<a href="#cl-1022">1022</a>
<a href="#cl-1023">1023</a>
<a href="#cl-1024">1024</a>
<a href="#cl-1025">1025</a>
<a href="#cl-1026">1026</a>
<a href="#cl-1027">1027</a>
<a href="#cl-1028">1028</a>
<a href="#cl-1029">1029</a>
<a href="#cl-1030">1030</a>
<a href="#cl-1031">1031</a>
<a href="#cl-1032">1032</a>
<a href="#cl-1033">1033</a>
<a href="#cl-1034">1034</a>
<a href="#cl-1035">1035</a>
<a href="#cl-1036">1036</a>
<a href="#cl-1037">1037</a>
<a href="#cl-1038">1038</a>
<a href="#cl-1039">1039</a>
<a href="#cl-1040">1040</a>
<a href="#cl-1041">1041</a>
<a href="#cl-1042">1042</a>
<a href="#cl-1043">1043</a>
<a href="#cl-1044">1044</a>
<a href="#cl-1045">1045</a>
<a href="#cl-1046">1046</a>
<a href="#cl-1047">1047</a>
<a href="#cl-1048">1048</a>
<a href="#cl-1049">1049</a>
<a href="#cl-1050">1050</a>
<a href="#cl-1051">1051</a>
<a href="#cl-1052">1052</a>
<a href="#cl-1053">1053</a>
<a href="#cl-1054">1054</a>
<a href="#cl-1055">1055</a>
<a href="#cl-1056">1056</a>
<a href="#cl-1057">1057</a>
<a href="#cl-1058">1058</a>
<a href="#cl-1059">1059</a>
<a href="#cl-1060">1060</a>
<a href="#cl-1061">1061</a>
<a href="#cl-1062">1062</a>
<a href="#cl-1063">1063</a>
<a href="#cl-1064">1064</a>
<a href="#cl-1065">1065</a>
<a href="#cl-1066">1066</a>
<a href="#cl-1067">1067</a>
<a href="#cl-1068">1068</a>
<a href="#cl-1069">1069</a>
<a href="#cl-1070">1070</a>
<a href="#cl-1071">1071</a>
<a href="#cl-1072">1072</a>
<a href="#cl-1073">1073</a>
<a href="#cl-1074">1074</a>
<a href="#cl-1075">1075</a>
<a href="#cl-1076">1076</a>
<a href="#cl-1077">1077</a>
<a href="#cl-1078">1078</a>
<a href="#cl-1079">1079</a>
<a href="#cl-1080">1080</a>
<a href="#cl-1081">1081</a>
<a href="#cl-1082">1082</a>
<a href="#cl-1083">1083</a>
<a href="#cl-1084">1084</a>
<a href="#cl-1085">1085</a>
<a href="#cl-1086">1086</a>
<a href="#cl-1087">1087</a>
<a href="#cl-1088">1088</a>
<a href="#cl-1089">1089</a>
<a href="#cl-1090">1090</a>
<a href="#cl-1091">1091</a>
<a href="#cl-1092">1092</a>
<a href="#cl-1093">1093</a>
<a href="#cl-1094">1094</a>
<a href="#cl-1095">1095</a>
<a href="#cl-1096">1096</a>
<a href="#cl-1097">1097</a>
<a href="#cl-1098">1098</a>
<a href="#cl-1099">1099</a>
<a href="#cl-1100">1100</a>
<a href="#cl-1101">1101</a>
<a href="#cl-1102">1102</a>
<a href="#cl-1103">1103</a>
<a href="#cl-1104">1104</a>
<a href="#cl-1105">1105</a>
<a href="#cl-1106">1106</a>
<a href="#cl-1107">1107</a>
<a href="#cl-1108">1108</a>
<a href="#cl-1109">1109</a>
<a href="#cl-1110">1110</a>
<a href="#cl-1111">1111</a>
<a href="#cl-1112">1112</a>
<a href="#cl-1113">1113</a>
<a href="#cl-1114">1114</a>
<a href="#cl-1115">1115</a>
<a href="#cl-1116">1116</a>
<a href="#cl-1117">1117</a>
<a href="#cl-1118">1118</a>
<a href="#cl-1119">1119</a>
<a href="#cl-1120">1120</a>
<a href="#cl-1121">1121</a>
<a href="#cl-1122">1122</a>
<a href="#cl-1123">1123</a>
<a href="#cl-1124">1124</a>
<a href="#cl-1125">1125</a>
<a href="#cl-1126">1126</a>
<a href="#cl-1127">1127</a>
<a href="#cl-1128">1128</a>
<a href="#cl-1129">1129</a>
<a href="#cl-1130">1130</a>
<a href="#cl-1131">1131</a>
<a href="#cl-1132">1132</a>
<a href="#cl-1133">1133</a>
<a href="#cl-1134">1134</a>
<a href="#cl-1135">1135</a>
<a href="#cl-1136">1136</a>
<a href="#cl-1137">1137</a>
<a href="#cl-1138">1138</a>
<a href="#cl-1139">1139</a>
<a href="#cl-1140">1140</a>
<a href="#cl-1141">1141</a>
<a href="#cl-1142">1142</a>
<a href="#cl-1143">1143</a>
<a href="#cl-1144">1144</a>
<a href="#cl-1145">1145</a>
<a href="#cl-1146">1146</a>
<a href="#cl-1147">1147</a>
<a href="#cl-1148">1148</a>
<a href="#cl-1149">1149</a>
<a href="#cl-1150">1150</a>
<a href="#cl-1151">1151</a>
<a href="#cl-1152">1152</a>
<a href="#cl-1153">1153</a>
<a href="#cl-1154">1154</a>
<a href="#cl-1155">1155</a>
<a href="#cl-1156">1156</a>
<a href="#cl-1157">1157</a>
<a href="#cl-1158">1158</a>
<a href="#cl-1159">1159</a>
<a href="#cl-1160">1160</a>
<a href="#cl-1161">1161</a>
<a href="#cl-1162">1162</a>
<a href="#cl-1163">1163</a>
<a href="#cl-1164">1164</a>
<a href="#cl-1165">1165</a>
<a href="#cl-1166">1166</a>
<a href="#cl-1167">1167</a>
<a href="#cl-1168">1168</a>
<a href="#cl-1169">1169</a>
<a href="#cl-1170">1170</a>
<a href="#cl-1171">1171</a>
<a href="#cl-1172">1172</a>
<a href="#cl-1173">1173</a>
<a href="#cl-1174">1174</a>
<a href="#cl-1175">1175</a>
<a href="#cl-1176">1176</a>
<a href="#cl-1177">1177</a>
<a href="#cl-1178">1178</a>
<a href="#cl-1179">1179</a>
<a href="#cl-1180">1180</a>
<a href="#cl-1181">1181</a>
<a href="#cl-1182">1182</a>
<a href="#cl-1183">1183</a>
<a href="#cl-1184">1184</a>
<a href="#cl-1185">1185</a>
<a href="#cl-1186">1186</a>
<a href="#cl-1187">1187</a>
<a href="#cl-1188">1188</a>
<a href="#cl-1189">1189</a>
<a href="#cl-1190">1190</a>
<a href="#cl-1191">1191</a>
<a href="#cl-1192">1192</a>
<a href="#cl-1193">1193</a>
<a href="#cl-1194">1194</a>
<a href="#cl-1195">1195</a>
<a href="#cl-1196">1196</a>
<a href="#cl-1197">1197</a>
<a href="#cl-1198">1198</a>
<a href="#cl-1199">1199</a>
<a href="#cl-1200">1200</a>
<a href="#cl-1201">1201</a>
<a href="#cl-1202">1202</a>
<a href="#cl-1203">1203</a>
<a href="#cl-1204">1204</a>
<a href="#cl-1205">1205</a>
<a href="#cl-1206">1206</a>
<a href="#cl-1207">1207</a>
<a href="#cl-1208">1208</a>
<a href="#cl-1209">1209</a>
<a href="#cl-1210">1210</a>
<a href="#cl-1211">1211</a>
<a href="#cl-1212">1212</a>
<a href="#cl-1213">1213</a>
<a href="#cl-1214">1214</a>
<a href="#cl-1215">1215</a>
<a href="#cl-1216">1216</a>
<a href="#cl-1217">1217</a>
<a href="#cl-1218">1218</a>
<a href="#cl-1219">1219</a>
<a href="#cl-1220">1220</a>
<a href="#cl-1221">1221</a>
<a href="#cl-1222">1222</a>
<a href="#cl-1223">1223</a>
<a href="#cl-1224">1224</a>
<a href="#cl-1225">1225</a>
<a href="#cl-1226">1226</a>
<a href="#cl-1227">1227</a>
<a href="#cl-1228">1228</a>
<a href="#cl-1229">1229</a>
<a href="#cl-1230">1230</a>
<a href="#cl-1231">1231</a>
<a href="#cl-1232">1232</a>
<a href="#cl-1233">1233</a>
<a href="#cl-1234">1234</a>
<a href="#cl-1235">1235</a>
<a href="#cl-1236">1236</a>
<a href="#cl-1237">1237</a>
<a href="#cl-1238">1238</a>
<a href="#cl-1239">1239</a>
<a href="#cl-1240">1240</a>
<a href="#cl-1241">1241</a>
<a href="#cl-1242">1242</a>
<a href="#cl-1243">1243</a>
<a href="#cl-1244">1244</a>
<a href="#cl-1245">1245</a>
<a href="#cl-1246">1246</a>
<a href="#cl-1247">1247</a>
<a href="#cl-1248">1248</a>
<a href="#cl-1249">1249</a>
<a href="#cl-1250">1250</a>
<a href="#cl-1251">1251</a>
<a href="#cl-1252">1252</a>
<a href="#cl-1253">1253</a>
<a href="#cl-1254">1254</a>
<a href="#cl-1255">1255</a>
<a href="#cl-1256">1256</a>
<a href="#cl-1257">1257</a>
<a href="#cl-1258">1258</a>
<a href="#cl-1259">1259</a>
<a href="#cl-1260">1260</a>
<a href="#cl-1261">1261</a>
<a href="#cl-1262">1262</a>
<a href="#cl-1263">1263</a>
<a href="#cl-1264">1264</a>
<a href="#cl-1265">1265</a>
<a href="#cl-1266">1266</a>
<a href="#cl-1267">1267</a>
<a href="#cl-1268">1268</a>
<a href="#cl-1269">1269</a>
<a href="#cl-1270">1270</a>
<a href="#cl-1271">1271</a>
<a href="#cl-1272">1272</a>
<a href="#cl-1273">1273</a>
<a href="#cl-1274">1274</a>
<a href="#cl-1275">1275</a>
<a href="#cl-1276">1276</a>
<a href="#cl-1277">1277</a>
<a href="#cl-1278">1278</a>
<a href="#cl-1279">1279</a>
<a href="#cl-1280">1280</a>
<a href="#cl-1281">1281</a>
<a href="#cl-1282">1282</a>
<a href="#cl-1283">1283</a>
<a href="#cl-1284">1284</a>
<a href="#cl-1285">1285</a>
<a href="#cl-1286">1286</a>
<a href="#cl-1287">1287</a>
<a href="#cl-1288">1288</a>
<a href="#cl-1289">1289</a>
<a href="#cl-1290">1290</a>
<a href="#cl-1291">1291</a>
<a href="#cl-1292">1292</a>
<a href="#cl-1293">1293</a>
<a href="#cl-1294">1294</a>
<a href="#cl-1295">1295</a>
<a href="#cl-1296">1296</a>
<a href="#cl-1297">1297</a>
<a href="#cl-1298">1298</a>
<a href="#cl-1299">1299</a>
<a href="#cl-1300">1300</a>
<a href="#cl-1301">1301</a>
<a href="#cl-1302">1302</a>
<a href="#cl-1303">1303</a>
<a href="#cl-1304">1304</a>
<a href="#cl-1305">1305</a>
<a href="#cl-1306">1306</a>
<a href="#cl-1307">1307</a>
<a href="#cl-1308">1308</a>
<a href="#cl-1309">1309</a>
<a href="#cl-1310">1310</a>
<a href="#cl-1311">1311</a>
<a href="#cl-1312">1312</a>
<a href="#cl-1313">1313</a>
<a href="#cl-1314">1314</a>
<a href="#cl-1315">1315</a>
<a href="#cl-1316">1316</a>
<a href="#cl-1317">1317</a>
<a href="#cl-1318">1318</a>
<a href="#cl-1319">1319</a>
<a href="#cl-1320">1320</a>
<a href="#cl-1321">1321</a>
<a href="#cl-1322">1322</a>
<a href="#cl-1323">1323</a>
<a href="#cl-1324">1324</a>
<a href="#cl-1325">1325</a>
<a href="#cl-1326">1326</a>
<a href="#cl-1327">1327</a>
<a href="#cl-1328">1328</a>
<a href="#cl-1329">1329</a>
<a href="#cl-1330">1330</a>
<a href="#cl-1331">1331</a>
<a href="#cl-1332">1332</a>
<a href="#cl-1333">1333</a>
<a href="#cl-1334">1334</a>
<a href="#cl-1335">1335</a>
<a href="#cl-1336">1336</a>
<a href="#cl-1337">1337</a>
<a href="#cl-1338">1338</a>
<a href="#cl-1339">1339</a>
<a href="#cl-1340">1340</a>
<a href="#cl-1341">1341</a>
<a href="#cl-1342">1342</a>
<a href="#cl-1343">1343</a>
<a href="#cl-1344">1344</a>
<a href="#cl-1345">1345</a>
<a href="#cl-1346">1346</a>
<a href="#cl-1347">1347</a>
<a href="#cl-1348">1348</a>
<a href="#cl-1349">1349</a>
<a href="#cl-1350">1350</a>
<a href="#cl-1351">1351</a>
<a href="#cl-1352">1352</a>
<a href="#cl-1353">1353</a>
<a href="#cl-1354">1354</a>
<a href="#cl-1355">1355</a>
<a href="#cl-1356">1356</a>
<a href="#cl-1357">1357</a>
<a href="#cl-1358">1358</a>
<a href="#cl-1359">1359</a>
<a href="#cl-1360">1360</a>
<a href="#cl-1361">1361</a>
<a href="#cl-1362">1362</a>
<a href="#cl-1363">1363</a>
<a href="#cl-1364">1364</a>
<a href="#cl-1365">1365</a>
<a href="#cl-1366">1366</a>
<a href="#cl-1367">1367</a>
<a href="#cl-1368">1368</a>
<a href="#cl-1369">1369</a>
<a href="#cl-1370">1370</a>
<a href="#cl-1371">1371</a>
<a href="#cl-1372">1372</a>
<a href="#cl-1373">1373</a>
<a href="#cl-1374">1374</a>
<a href="#cl-1375">1375</a>
<a href="#cl-1376">1376</a>
<a href="#cl-1377">1377</a>
<a href="#cl-1378">1378</a>
<a href="#cl-1379">1379</a>
<a href="#cl-1380">1380</a>
<a href="#cl-1381">1381</a>
<a href="#cl-1382">1382</a>
<a href="#cl-1383">1383</a>
<a href="#cl-1384">1384</a>
<a href="#cl-1385">1385</a>
<a href="#cl-1386">1386</a>
<a href="#cl-1387">1387</a>
<a href="#cl-1388">1388</a>
<a href="#cl-1389">1389</a>
<a href="#cl-1390">1390</a>
<a href="#cl-1391">1391</a>
<a href="#cl-1392">1392</a>
<a href="#cl-1393">1393</a>
<a href="#cl-1394">1394</a>
<a href="#cl-1395">1395</a>
<a href="#cl-1396">1396</a>
<a href="#cl-1397">1397</a>
<a href="#cl-1398">1398</a>
<a href="#cl-1399">1399</a>
<a href="#cl-1400">1400</a>
<a href="#cl-1401">1401</a>
<a href="#cl-1402">1402</a>
<a href="#cl-1403">1403</a>
<a href="#cl-1404">1404</a>
<a href="#cl-1405">1405</a>
<a href="#cl-1406">1406</a>
<a href="#cl-1407">1407</a>
<a href="#cl-1408">1408</a>
<a href="#cl-1409">1409</a>
<a href="#cl-1410">1410</a>
<a href="#cl-1411">1411</a>
<a href="#cl-1412">1412</a>
<a href="#cl-1413">1413</a>
<a href="#cl-1414">1414</a>
<a href="#cl-1415">1415</a>
<a href="#cl-1416">1416</a>
<a href="#cl-1417">1417</a>
<a href="#cl-1418">1418</a>
<a href="#cl-1419">1419</a>
<a href="#cl-1420">1420</a>
<a href="#cl-1421">1421</a>
<a href="#cl-1422">1422</a>
<a href="#cl-1423">1423</a>
<a href="#cl-1424">1424</a>
<a href="#cl-1425">1425</a>
<a href="#cl-1426">1426</a>
<a href="#cl-1427">1427</a>
<a href="#cl-1428">1428</a>
<a href="#cl-1429">1429</a>
<a href="#cl-1430">1430</a>
<a href="#cl-1431">1431</a>
<a href="#cl-1432">1432</a>
<a href="#cl-1433">1433</a>
<a href="#cl-1434">1434</a>
<a href="#cl-1435">1435</a>
<a href="#cl-1436">1436</a>
<a href="#cl-1437">1437</a>
<a href="#cl-1438">1438</a>
<a href="#cl-1439">1439</a>
<a href="#cl-1440">1440</a>
<a href="#cl-1441">1441</a>
<a href="#cl-1442">1442</a>
<a href="#cl-1443">1443</a>
<a href="#cl-1444">1444</a>
<a href="#cl-1445">1445</a>
<a href="#cl-1446">1446</a>
<a href="#cl-1447">1447</a>
<a href="#cl-1448">1448</a>
<a href="#cl-1449">1449</a>
<a href="#cl-1450">1450</a>
<a href="#cl-1451">1451</a>
<a href="#cl-1452">1452</a>
<a href="#cl-1453">1453</a>
<a href="#cl-1454">1454</a>
<a href="#cl-1455">1455</a>
<a href="#cl-1456">1456</a>
<a href="#cl-1457">1457</a>
<a href="#cl-1458">1458</a>
<a href="#cl-1459">1459</a>
<a href="#cl-1460">1460</a>
<a href="#cl-1461">1461</a>
<a href="#cl-1462">1462</a>
<a href="#cl-1463">1463</a>
<a href="#cl-1464">1464</a>
<a href="#cl-1465">1465</a>
<a href="#cl-1466">1466</a>
<a href="#cl-1467">1467</a>
<a href="#cl-1468">1468</a>
<a href="#cl-1469">1469</a>
<a href="#cl-1470">1470</a>
<a href="#cl-1471">1471</a>
<a href="#cl-1472">1472</a>
<a href="#cl-1473">1473</a>
<a href="#cl-1474">1474</a>
<a href="#cl-1475">1475</a>
<a href="#cl-1476">1476</a>
<a href="#cl-1477">1477</a>
<a href="#cl-1478">1478</a>
<a href="#cl-1479">1479</a>
<a href="#cl-1480">1480</a>
<a href="#cl-1481">1481</a>
<a href="#cl-1482">1482</a>
<a href="#cl-1483">1483</a>
<a href="#cl-1484">1484</a>
<a href="#cl-1485">1485</a>
<a href="#cl-1486">1486</a>
<a href="#cl-1487">1487</a>
<a href="#cl-1488">1488</a>
<a href="#cl-1489">1489</a>
<a href="#cl-1490">1490</a>
<a href="#cl-1491">1491</a>
<a href="#cl-1492">1492</a>
<a href="#cl-1493">1493</a>
<a href="#cl-1494">1494</a>
<a href="#cl-1495">1495</a>
<a href="#cl-1496">1496</a>
<a href="#cl-1497">1497</a>
<a href="#cl-1498">1498</a>
<a href="#cl-1499">1499</a>
<a href="#cl-1500">1500</a>
<a href="#cl-1501">1501</a>
<a href="#cl-1502">1502</a>
<a href="#cl-1503">1503</a>
<a href="#cl-1504">1504</a>
<a href="#cl-1505">1505</a>
<a href="#cl-1506">1506</a>
<a href="#cl-1507">1507</a>
<a href="#cl-1508">1508</a>
<a href="#cl-1509">1509</a>
<a href="#cl-1510">1510</a>
<a href="#cl-1511">1511</a>
<a href="#cl-1512">1512</a>
<a href="#cl-1513">1513</a>
<a href="#cl-1514">1514</a>
<a href="#cl-1515">1515</a>
<a href="#cl-1516">1516</a>
<a href="#cl-1517">1517</a>
<a href="#cl-1518">1518</a>
<a href="#cl-1519">1519</a>
<a href="#cl-1520">1520</a>
<a href="#cl-1521">1521</a>
<a href="#cl-1522">1522</a>
<a href="#cl-1523">1523</a>
<a href="#cl-1524">1524</a>
<a href="#cl-1525">1525</a>
<a href="#cl-1526">1526</a>
<a href="#cl-1527">1527</a>
<a href="#cl-1528">1528</a>
<a href="#cl-1529">1529</a>
<a href="#cl-1530">1530</a>
<a href="#cl-1531">1531</a>
<a href="#cl-1532">1532</a>
<a href="#cl-1533">1533</a>
<a href="#cl-1534">1534</a>
<a href="#cl-1535">1535</a>
<a href="#cl-1536">1536</a>
<a href="#cl-1537">1537</a>
<a href="#cl-1538">1538</a>
<a href="#cl-1539">1539</a>
<a href="#cl-1540">1540</a>
<a href="#cl-1541">1541</a>
<a href="#cl-1542">1542</a>
<a href="#cl-1543">1543</a>
<a href="#cl-1544">1544</a>
<a href="#cl-1545">1545</a>
<a href="#cl-1546">1546</a>
<a href="#cl-1547">1547</a>
<a href="#cl-1548">1548</a>
<a href="#cl-1549">1549</a>
<a href="#cl-1550">1550</a>
<a href="#cl-1551">1551</a>
<a href="#cl-1552">1552</a>
<a href="#cl-1553">1553</a>
<a href="#cl-1554">1554</a>
<a href="#cl-1555">1555</a>
<a href="#cl-1556">1556</a>
<a href="#cl-1557">1557</a>
<a href="#cl-1558">1558</a>
<a href="#cl-1559">1559</a>
<a href="#cl-1560">1560</a>
<a href="#cl-1561">1561</a>
<a href="#cl-1562">1562</a>
<a href="#cl-1563">1563</a>
<a href="#cl-1564">1564</a>
<a href="#cl-1565">1565</a>
<a href="#cl-1566">1566</a>
<a href="#cl-1567">1567</a>
<a href="#cl-1568">1568</a>
<a href="#cl-1569">1569</a>
<a href="#cl-1570">1570</a>
<a href="#cl-1571">1571</a>
<a href="#cl-1572">1572</a>
<a href="#cl-1573">1573</a>
<a href="#cl-1574">1574</a>
<a href="#cl-1575">1575</a>
<a href="#cl-1576">1576</a>
<a href="#cl-1577">1577</a>
<a href="#cl-1578">1578</a>
<a href="#cl-1579">1579</a>
<a href="#cl-1580">1580</a>
<a href="#cl-1581">1581</a>
<a href="#cl-1582">1582</a>
<a href="#cl-1583">1583</a>
<a href="#cl-1584">1584</a>
<a href="#cl-1585">1585</a>
<a href="#cl-1586">1586</a>
<a href="#cl-1587">1587</a>
<a href="#cl-1588">1588</a>
<a href="#cl-1589">1589</a>
<a href="#cl-1590">1590</a>
<a href="#cl-1591">1591</a>
<a href="#cl-1592">1592</a>
<a href="#cl-1593">1593</a>
<a href="#cl-1594">1594</a>
<a href="#cl-1595">1595</a>
<a href="#cl-1596">1596</a>
<a href="#cl-1597">1597</a>
<a href="#cl-1598">1598</a>
<a href="#cl-1599">1599</a>
<a href="#cl-1600">1600</a>
<a href="#cl-1601">1601</a>
<a href="#cl-1602">1602</a>
<a href="#cl-1603">1603</a>
<a href="#cl-1604">1604</a>
<a href="#cl-1605">1605</a>
<a href="#cl-1606">1606</a>
<a href="#cl-1607">1607</a>
<a href="#cl-1608">1608</a>
<a href="#cl-1609">1609</a>
<a href="#cl-1610">1610</a>
<a href="#cl-1611">1611</a>
<a href="#cl-1612">1612</a>
<a href="#cl-1613">1613</a>
<a href="#cl-1614">1614</a>
<a href="#cl-1615">1615</a>
<a href="#cl-1616">1616</a>
<a href="#cl-1617">1617</a>
<a href="#cl-1618">1618</a>
<a href="#cl-1619">1619</a>
<a href="#cl-1620">1620</a>
<a href="#cl-1621">1621</a>
<a href="#cl-1622">1622</a>
<a href="#cl-1623">1623</a>
<a href="#cl-1624">1624</a>
<a href="#cl-1625">1625</a>
<a href="#cl-1626">1626</a>
<a href="#cl-1627">1627</a>
<a href="#cl-1628">1628</a>
<a href="#cl-1629">1629</a>
<a href="#cl-1630">1630</a>
<a href="#cl-1631">1631</a>
<a href="#cl-1632">1632</a>
<a href="#cl-1633">1633</a>
<a href="#cl-1634">1634</a>
<a href="#cl-1635">1635</a>
<a href="#cl-1636">1636</a>
<a href="#cl-1637">1637</a>
<a href="#cl-1638">1638</a>
<a href="#cl-1639">1639</a>
<a href="#cl-1640">1640</a>
<a href="#cl-1641">1641</a>
<a href="#cl-1642">1642</a>
<a href="#cl-1643">1643</a>
<a href="#cl-1644">1644</a>
<a href="#cl-1645">1645</a>
<a href="#cl-1646">1646</a>
<a href="#cl-1647">1647</a>
<a href="#cl-1648">1648</a>
<a href="#cl-1649">1649</a>
<a href="#cl-1650">1650</a>
<a href="#cl-1651">1651</a>
<a href="#cl-1652">1652</a>
<a href="#cl-1653">1653</a>
<a href="#cl-1654">1654</a>
<a href="#cl-1655">1655</a>
<a href="#cl-1656">1656</a>
<a href="#cl-1657">1657</a>
<a href="#cl-1658">1658</a>
<a href="#cl-1659">1659</a>
<a href="#cl-1660">1660</a>
<a href="#cl-1661">1661</a>
<a href="#cl-1662">1662</a>
<a href="#cl-1663">1663</a>
<a href="#cl-1664">1664</a>
<a href="#cl-1665">1665</a>
<a href="#cl-1666">1666</a>
<a href="#cl-1667">1667</a>
<a href="#cl-1668">1668</a>
<a href="#cl-1669">1669</a>
<a href="#cl-1670">1670</a>
<a href="#cl-1671">1671</a>
<a href="#cl-1672">1672</a>
<a href="#cl-1673">1673</a>
<a href="#cl-1674">1674</a>
<a href="#cl-1675">1675</a>
<a href="#cl-1676">1676</a>
<a href="#cl-1677">1677</a>
<a href="#cl-1678">1678</a>
<a href="#cl-1679">1679</a>
<a href="#cl-1680">1680</a>
<a href="#cl-1681">1681</a>
<a href="#cl-1682">1682</a>
<a href="#cl-1683">1683</a>
<a href="#cl-1684">1684</a>
<a href="#cl-1685">1685</a>
<a href="#cl-1686">1686</a>
<a href="#cl-1687">1687</a>
<a href="#cl-1688">1688</a>
<a href="#cl-1689">1689</a>
<a href="#cl-1690">1690</a>
<a href="#cl-1691">1691</a>
<a href="#cl-1692">1692</a>
<a href="#cl-1693">1693</a>
<a href="#cl-1694">1694</a>
<a href="#cl-1695">1695</a>
<a href="#cl-1696">1696</a>
<a href="#cl-1697">1697</a>
<a href="#cl-1698">1698</a>
<a href="#cl-1699">1699</a>
<a href="#cl-1700">1700</a>
<a href="#cl-1701">1701</a>
<a href="#cl-1702">1702</a>
<a href="#cl-1703">1703</a>
<a href="#cl-1704">1704</a>
<a href="#cl-1705">1705</a>
<a href="#cl-1706">1706</a>
<a href="#cl-1707">1707</a>
<a href="#cl-1708">1708</a>
<a href="#cl-1709">1709</a>
<a href="#cl-1710">1710</a>
<a href="#cl-1711">1711</a>
<a href="#cl-1712">1712</a>
<a href="#cl-1713">1713</a>
<a href="#cl-1714">1714</a>
<a href="#cl-1715">1715</a>
<a href="#cl-1716">1716</a>
<a href="#cl-1717">1717</a>
<a href="#cl-1718">1718</a>
<a href="#cl-1719">1719</a>
<a href="#cl-1720">1720</a>
<a href="#cl-1721">1721</a>
<a href="#cl-1722">1722</a>
<a href="#cl-1723">1723</a>
<a href="#cl-1724">1724</a>
<a href="#cl-1725">1725</a>
<a href="#cl-1726">1726</a>
<a href="#cl-1727">1727</a>
<a href="#cl-1728">1728</a>
<a href="#cl-1729">1729</a>
<a href="#cl-1730">1730</a>
<a href="#cl-1731">1731</a>
<a href="#cl-1732">1732</a>
<a href="#cl-1733">1733</a>
<a href="#cl-1734">1734</a>
<a href="#cl-1735">1735</a>
<a href="#cl-1736">1736</a>
<a href="#cl-1737">1737</a>
<a href="#cl-1738">1738</a>
<a href="#cl-1739">1739</a>
<a href="#cl-1740">1740</a>
<a href="#cl-1741">1741</a>
<a href="#cl-1742">1742</a>
<a href="#cl-1743">1743</a>
<a href="#cl-1744">1744</a>
<a href="#cl-1745">1745</a>
<a href="#cl-1746">1746</a>
<a href="#cl-1747">1747</a>
<a href="#cl-1748">1748</a>
<a href="#cl-1749">1749</a>
<a href="#cl-1750">1750</a>
<a href="#cl-1751">1751</a>
<a href="#cl-1752">1752</a>
<a href="#cl-1753">1753</a>
<a href="#cl-1754">1754</a>
<a href="#cl-1755">1755</a>
<a href="#cl-1756">1756</a>
<a href="#cl-1757">1757</a>
<a href="#cl-1758">1758</a>
<a href="#cl-1759">1759</a>
<a href="#cl-1760">1760</a>
<a href="#cl-1761">1761</a>
<a href="#cl-1762">1762</a>
<a href="#cl-1763">1763</a>
<a href="#cl-1764">1764</a>
<a href="#cl-1765">1765</a>
<a href="#cl-1766">1766</a>
<a href="#cl-1767">1767</a>
<a href="#cl-1768">1768</a>
<a href="#cl-1769">1769</a>
<a href="#cl-1770">1770</a>
<a href="#cl-1771">1771</a>
<a href="#cl-1772">1772</a>
<a href="#cl-1773">1773</a>
<a href="#cl-1774">1774</a>
<a href="#cl-1775">1775</a>
<a href="#cl-1776">1776</a>
<a href="#cl-1777">1777</a>
<a href="#cl-1778">1778</a>
<a href="#cl-1779">1779</a>
<a href="#cl-1780">1780</a>
<a href="#cl-1781">1781</a>
<a href="#cl-1782">1782</a>
<a href="#cl-1783">1783</a>
<a href="#cl-1784">1784</a>
<a href="#cl-1785">1785</a>
<a href="#cl-1786">1786</a>
<a href="#cl-1787">1787</a>
<a href="#cl-1788">1788</a>
<a href="#cl-1789">1789</a>
<a href="#cl-1790">1790</a>
<a href="#cl-1791">1791</a>
<a href="#cl-1792">1792</a>
<a href="#cl-1793">1793</a>
<a href="#cl-1794">1794</a>
<a href="#cl-1795">1795</a>
<a href="#cl-1796">1796</a>
<a href="#cl-1797">1797</a>
<a href="#cl-1798">1798</a>
<a href="#cl-1799">1799</a>
<a href="#cl-1800">1800</a>
<a href="#cl-1801">1801</a>
<a href="#cl-1802">1802</a>
<a href="#cl-1803">1803</a>
<a href="#cl-1804">1804</a>
<a href="#cl-1805">1805</a>
<a href="#cl-1806">1806</a>
<a href="#cl-1807">1807</a>
<a href="#cl-1808">1808</a>
<a href="#cl-1809">1809</a>
<a href="#cl-1810">1810</a>
<a href="#cl-1811">1811</a>
<a href="#cl-1812">1812</a>
<a href="#cl-1813">1813</a>
<a href="#cl-1814">1814</a>
<a href="#cl-1815">1815</a>
<a href="#cl-1816">1816</a>
<a href="#cl-1817">1817</a>
<a href="#cl-1818">1818</a>
<a href="#cl-1819">1819</a>
<a href="#cl-1820">1820</a>
<a href="#cl-1821">1821</a>
<a href="#cl-1822">1822</a>
<a href="#cl-1823">1823</a>
<a href="#cl-1824">1824</a>
<a href="#cl-1825">1825</a>
<a href="#cl-1826">1826</a>
<a href="#cl-1827">1827</a>
<a href="#cl-1828">1828</a>
<a href="#cl-1829">1829</a>
<a href="#cl-1830">1830</a>
<a href="#cl-1831">1831</a>
<a href="#cl-1832">1832</a>
<a href="#cl-1833">1833</a>
<a href="#cl-1834">1834</a>
<a href="#cl-1835">1835</a>
<a href="#cl-1836">1836</a>
<a href="#cl-1837">1837</a>
<a href="#cl-1838">1838</a>
<a href="#cl-1839">1839</a>
<a href="#cl-1840">1840</a>
<a href="#cl-1841">1841</a>
<a href="#cl-1842">1842</a>
<a href="#cl-1843">1843</a>
<a href="#cl-1844">1844</a>
<a href="#cl-1845">1845</a>
<a href="#cl-1846">1846</a>
<a href="#cl-1847">1847</a>
<a href="#cl-1848">1848</a>
<a href="#cl-1849">1849</a>
<a href="#cl-1850">1850</a>
<a href="#cl-1851">1851</a>
<a href="#cl-1852">1852</a>
<a href="#cl-1853">1853</a>
<a href="#cl-1854">1854</a>
<a href="#cl-1855">1855</a>
<a href="#cl-1856">1856</a>
<a href="#cl-1857">1857</a>
<a href="#cl-1858">1858</a>
<a href="#cl-1859">1859</a>
<a href="#cl-1860">1860</a>
<a href="#cl-1861">1861</a>
<a href="#cl-1862">1862</a>
<a href="#cl-1863">1863</a>
<a href="#cl-1864">1864</a>
<a href="#cl-1865">1865</a>
<a href="#cl-1866">1866</a>
<a href="#cl-1867">1867</a>
<a href="#cl-1868">1868</a>
<a href="#cl-1869">1869</a>
<a href="#cl-1870">1870</a>
<a href="#cl-1871">1871</a>
<a href="#cl-1872">1872</a>
<a href="#cl-1873">1873</a>
<a href="#cl-1874">1874</a>
<a href="#cl-1875">1875</a>
<a href="#cl-1876">1876</a>
<a href="#cl-1877">1877</a>
<a href="#cl-1878">1878</a>
<a href="#cl-1879">1879</a>
<a href="#cl-1880">1880</a>
<a href="#cl-1881">1881</a>
<a href="#cl-1882">1882</a>
<a href="#cl-1883">1883</a>
<a href="#cl-1884">1884</a>
<a href="#cl-1885">1885</a>
<a href="#cl-1886">1886</a>
<a href="#cl-1887">1887</a>
<a href="#cl-1888">1888</a>
<a href="#cl-1889">1889</a>
<a href="#cl-1890">1890</a>
<a href="#cl-1891">1891</a>
<a href="#cl-1892">1892</a>
<a href="#cl-1893">1893</a>
<a href="#cl-1894">1894</a>
<a href="#cl-1895">1895</a>
<a href="#cl-1896">1896</a>
<a href="#cl-1897">1897</a>
<a href="#cl-1898">1898</a>
<a href="#cl-1899">1899</a>
<a href="#cl-1900">1900</a>
<a href="#cl-1901">1901</a>
<a href="#cl-1902">1902</a>
<a href="#cl-1903">1903</a>
<a href="#cl-1904">1904</a>
<a href="#cl-1905">1905</a>
<a href="#cl-1906">1906</a>
<a href="#cl-1907">1907</a>
<a href="#cl-1908">1908</a>
<a href="#cl-1909">1909</a>
<a href="#cl-1910">1910</a>
<a href="#cl-1911">1911</a>
<a href="#cl-1912">1912</a>
<a href="#cl-1913">1913</a>
<a href="#cl-1914">1914</a>
<a href="#cl-1915">1915</a>
<a href="#cl-1916">1916</a>
<a href="#cl-1917">1917</a>
<a href="#cl-1918">1918</a>
<a href="#cl-1919">1919</a>
<a href="#cl-1920">1920</a>
<a href="#cl-1921">1921</a>
<a href="#cl-1922">1922</a>
<a href="#cl-1923">1923</a>
<a href="#cl-1924">1924</a>
<a href="#cl-1925">1925</a>
<a href="#cl-1926">1926</a>
<a href="#cl-1927">1927</a>
<a href="#cl-1928">1928</a>
<a href="#cl-1929">1929</a>
<a href="#cl-1930">1930</a>
<a href="#cl-1931">1931</a>
<a href="#cl-1932">1932</a>
<a href="#cl-1933">1933</a>
<a href="#cl-1934">1934</a>
<a href="#cl-1935">1935</a>
<a href="#cl-1936">1936</a>
<a href="#cl-1937">1937</a>
<a href="#cl-1938">1938</a>
<a href="#cl-1939">1939</a>
<a href="#cl-1940">1940</a>
<a href="#cl-1941">1941</a>
<a href="#cl-1942">1942</a>
<a href="#cl-1943">1943</a>
<a href="#cl-1944">1944</a>
<a href="#cl-1945">1945</a>
<a href="#cl-1946">1946</a>
<a href="#cl-1947">1947</a>
<a href="#cl-1948">1948</a>
<a href="#cl-1949">1949</a>
<a href="#cl-1950">1950</a>
<a href="#cl-1951">1951</a>
<a href="#cl-1952">1952</a>
<a href="#cl-1953">1953</a>
<a href="#cl-1954">1954</a>
<a href="#cl-1955">1955</a>
<a href="#cl-1956">1956</a>
<a href="#cl-1957">1957</a>
<a href="#cl-1958">1958</a>
<a href="#cl-1959">1959</a>
<a href="#cl-1960">1960</a>
<a href="#cl-1961">1961</a>
<a href="#cl-1962">1962</a>
<a href="#cl-1963">1963</a>
<a href="#cl-1964">1964</a>
<a href="#cl-1965">1965</a>
<a href="#cl-1966">1966</a>
<a href="#cl-1967">1967</a>
<a href="#cl-1968">1968</a>
<a href="#cl-1969">1969</a>
<a href="#cl-1970">1970</a>
<a href="#cl-1971">1971</a>
<a href="#cl-1972">1972</a>
<a href="#cl-1973">1973</a>
<a href="#cl-1974">1974</a>
<a href="#cl-1975">1975</a>
<a href="#cl-1976">1976</a>
<a href="#cl-1977">1977</a>
<a href="#cl-1978">1978</a>
<a href="#cl-1979">1979</a>
<a href="#cl-1980">1980</a>
<a href="#cl-1981">1981</a>
<a href="#cl-1982">1982</a>
<a href="#cl-1983">1983</a>
<a href="#cl-1984">1984</a>
<a href="#cl-1985">1985</a>
<a href="#cl-1986">1986</a>
<a href="#cl-1987">1987</a>
<a href="#cl-1988">1988</a>
<a href="#cl-1989">1989</a>
<a href="#cl-1990">1990</a>
<a href="#cl-1991">1991</a>
<a href="#cl-1992">1992</a>
<a href="#cl-1993">1993</a>
<a href="#cl-1994">1994</a>
<a href="#cl-1995">1995</a>
<a href="#cl-1996">1996</a>
<a href="#cl-1997">1997</a>
<a href="#cl-1998">1998</a>
<a href="#cl-1999">1999</a>
<a href="#cl-2000">2000</a>
<a href="#cl-2001">2001</a>
<a href="#cl-2002">2002</a>
<a href="#cl-2003">2003</a>
<a href="#cl-2004">2004</a>
<a href="#cl-2005">2005</a>
<a href="#cl-2006">2006</a>
<a href="#cl-2007">2007</a>
<a href="#cl-2008">2008</a>
<a href="#cl-2009">2009</a>
<a href="#cl-2010">2010</a>
<a href="#cl-2011">2011</a>
<a href="#cl-2012">2012</a>
<a href="#cl-2013">2013</a>
<a href="#cl-2014">2014</a>
<a href="#cl-2015">2015</a>
<a href="#cl-2016">2016</a>
<a href="#cl-2017">2017</a>
<a href="#cl-2018">2018</a>
<a href="#cl-2019">2019</a>
<a href="#cl-2020">2020</a>
<a href="#cl-2021">2021</a>
<a href="#cl-2022">2022</a>
<a href="#cl-2023">2023</a>
<a href="#cl-2024">2024</a>
<a href="#cl-2025">2025</a>
<a href="#cl-2026">2026</a>
<a href="#cl-2027">2027</a>
<a href="#cl-2028">2028</a>
<a href="#cl-2029">2029</a>
<a href="#cl-2030">2030</a>
<a href="#cl-2031">2031</a>
<a href="#cl-2032">2032</a>
<a href="#cl-2033">2033</a>
<a href="#cl-2034">2034</a>
<a href="#cl-2035">2035</a>
<a href="#cl-2036">2036</a>
<a href="#cl-2037">2037</a>
<a href="#cl-2038">2038</a>
<a href="#cl-2039">2039</a>
<a href="#cl-2040">2040</a>
<a href="#cl-2041">2041</a>
<a href="#cl-2042">2042</a>
<a href="#cl-2043">2043</a>
<a href="#cl-2044">2044</a>
<a href="#cl-2045">2045</a>
<a href="#cl-2046">2046</a>
<a href="#cl-2047">2047</a>
<a href="#cl-2048">2048</a>
<a href="#cl-2049">2049</a>
<a href="#cl-2050">2050</a>
<a href="#cl-2051">2051</a>
<a href="#cl-2052">2052</a>
<a href="#cl-2053">2053</a>
<a href="#cl-2054">2054</a>
<a href="#cl-2055">2055</a>
<a href="#cl-2056">2056</a>
<a href="#cl-2057">2057</a>
<a href="#cl-2058">2058</a>
<a href="#cl-2059">2059</a>
<a href="#cl-2060">2060</a>
<a href="#cl-2061">2061</a>
<a href="#cl-2062">2062</a>
<a href="#cl-2063">2063</a>
<a href="#cl-2064">2064</a>
<a href="#cl-2065">2065</a>
<a href="#cl-2066">2066</a>
<a href="#cl-2067">2067</a>
<a href="#cl-2068">2068</a>
<a href="#cl-2069">2069</a>
<a href="#cl-2070">2070</a>
<a href="#cl-2071">2071</a>
<a href="#cl-2072">2072</a>
<a href="#cl-2073">2073</a>
<a href="#cl-2074">2074</a>
<a href="#cl-2075">2075</a>
<a href="#cl-2076">2076</a>
<a href="#cl-2077">2077</a>
<a href="#cl-2078">2078</a>
<a href="#cl-2079">2079</a>
<a href="#cl-2080">2080</a>
<a href="#cl-2081">2081</a>
<a href="#cl-2082">2082</a>
<a href="#cl-2083">2083</a>
<a href="#cl-2084">2084</a>
<a href="#cl-2085">2085</a>
<a href="#cl-2086">2086</a>
<a href="#cl-2087">2087</a>
<a href="#cl-2088">2088</a>
<a href="#cl-2089">2089</a>
<a href="#cl-2090">2090</a>
<a href="#cl-2091">2091</a>
<a href="#cl-2092">2092</a>
<a href="#cl-2093">2093</a>
<a href="#cl-2094">2094</a>
<a href="#cl-2095">2095</a>
<a href="#cl-2096">2096</a>
<a href="#cl-2097">2097</a>
<a href="#cl-2098">2098</a>
<a href="#cl-2099">2099</a>
<a href="#cl-2100">2100</a>
<a href="#cl-2101">2101</a>
<a href="#cl-2102">2102</a>
<a href="#cl-2103">2103</a>
<a href="#cl-2104">2104</a>
<a href="#cl-2105">2105</a>
<a href="#cl-2106">2106</a>
<a href="#cl-2107">2107</a>
<a href="#cl-2108">2108</a>
<a href="#cl-2109">2109</a>
<a href="#cl-2110">2110</a>
<a href="#cl-2111">2111</a>
<a href="#cl-2112">2112</a>
<a href="#cl-2113">2113</a>
<a href="#cl-2114">2114</a>
<a href="#cl-2115">2115</a>
<a href="#cl-2116">2116</a>
<a href="#cl-2117">2117</a>
<a href="#cl-2118">2118</a>
<a href="#cl-2119">2119</a>
<a href="#cl-2120">2120</a>
<a href="#cl-2121">2121</a>
<a href="#cl-2122">2122</a>
<a href="#cl-2123">2123</a>
<a href="#cl-2124">2124</a>
<a href="#cl-2125">2125</a>
<a href="#cl-2126">2126</a>
<a href="#cl-2127">2127</a>
<a href="#cl-2128">2128</a>
<a href="#cl-2129">2129</a>
<a href="#cl-2130">2130</a>
<a href="#cl-2131">2131</a>
<a href="#cl-2132">2132</a>
<a href="#cl-2133">2133</a>
<a href="#cl-2134">2134</a>
<a href="#cl-2135">2135</a>
<a href="#cl-2136">2136</a>
<a href="#cl-2137">2137</a>
<a href="#cl-2138">2138</a>
<a href="#cl-2139">2139</a>
<a href="#cl-2140">2140</a>
<a href="#cl-2141">2141</a>
<a href="#cl-2142">2142</a>
<a href="#cl-2143">2143</a>
<a href="#cl-2144">2144</a>
<a href="#cl-2145">2145</a>
<a href="#cl-2146">2146</a>
<a href="#cl-2147">2147</a>
<a href="#cl-2148">2148</a>
<a href="#cl-2149">2149</a>
<a href="#cl-2150">2150</a>
<a href="#cl-2151">2151</a>
<a href="#cl-2152">2152</a>
<a href="#cl-2153">2153</a>
<a href="#cl-2154">2154</a>
<a href="#cl-2155">2155</a>
<a href="#cl-2156">2156</a>
<a href="#cl-2157">2157</a>
<a href="#cl-2158">2158</a>
<a href="#cl-2159">2159</a>
<a href="#cl-2160">2160</a>
<a href="#cl-2161">2161</a>
<a href="#cl-2162">2162</a>
<a href="#cl-2163">2163</a>
<a href="#cl-2164">2164</a>
<a href="#cl-2165">2165</a>
<a href="#cl-2166">2166</a>
<a href="#cl-2167">2167</a>
<a href="#cl-2168">2168</a>
<a href="#cl-2169">2169</a>
<a href="#cl-2170">2170</a>
<a href="#cl-2171">2171</a>
<a href="#cl-2172">2172</a>
<a href="#cl-2173">2173</a>
<a href="#cl-2174">2174</a>
<a href="#cl-2175">2175</a>
<a href="#cl-2176">2176</a>
<a href="#cl-2177">2177</a>
<a href="#cl-2178">2178</a>
<a href="#cl-2179">2179</a>
<a href="#cl-2180">2180</a>
<a href="#cl-2181">2181</a>
<a href="#cl-2182">2182</a>
<a href="#cl-2183">2183</a>
<a href="#cl-2184">2184</a>
<a href="#cl-2185">2185</a>
<a href="#cl-2186">2186</a>
<a href="#cl-2187">2187</a>
<a href="#cl-2188">2188</a>
<a href="#cl-2189">2189</a>
<a href="#cl-2190">2190</a>
<a href="#cl-2191">2191</a>
<a href="#cl-2192">2192</a>
<a href="#cl-2193">2193</a>
<a href="#cl-2194">2194</a>
<a href="#cl-2195">2195</a>
<a href="#cl-2196">2196</a>
<a href="#cl-2197">2197</a>
<a href="#cl-2198">2198</a>
<a href="#cl-2199">2199</a>
<a href="#cl-2200">2200</a>
<a href="#cl-2201">2201</a>
<a href="#cl-2202">2202</a>
<a href="#cl-2203">2203</a>
<a href="#cl-2204">2204</a>
<a href="#cl-2205">2205</a>
<a href="#cl-2206">2206</a>
<a href="#cl-2207">2207</a>
<a href="#cl-2208">2208</a>
<a href="#cl-2209">2209</a>
<a href="#cl-2210">2210</a>
<a href="#cl-2211">2211</a>
<a href="#cl-2212">2212</a>
<a href="#cl-2213">2213</a>
<a href="#cl-2214">2214</a>
<a href="#cl-2215">2215</a>
<a href="#cl-2216">2216</a>
<a href="#cl-2217">2217</a>
<a href="#cl-2218">2218</a>
<a href="#cl-2219">2219</a>
<a href="#cl-2220">2220</a>
<a href="#cl-2221">2221</a>
<a href="#cl-2222">2222</a>
<a href="#cl-2223">2223</a>
<a href="#cl-2224">2224</a>
<a href="#cl-2225">2225</a>
<a href="#cl-2226">2226</a>
<a href="#cl-2227">2227</a>
<a href="#cl-2228">2228</a>
<a href="#cl-2229">2229</a>
<a href="#cl-2230">2230</a>
<a href="#cl-2231">2231</a>
<a href="#cl-2232">2232</a>
<a href="#cl-2233">2233</a>
<a href="#cl-2234">2234</a>
<a href="#cl-2235">2235</a>
<a href="#cl-2236">2236</a>
<a href="#cl-2237">2237</a>
<a href="#cl-2238">2238</a>
<a href="#cl-2239">2239</a>
<a href="#cl-2240">2240</a>
<a href="#cl-2241">2241</a>
<a href="#cl-2242">2242</a>
<a href="#cl-2243">2243</a>
<a href="#cl-2244">2244</a>
<a href="#cl-2245">2245</a>
<a href="#cl-2246">2246</a>
<a href="#cl-2247">2247</a>
<a href="#cl-2248">2248</a>
<a href="#cl-2249">2249</a>
<a href="#cl-2250">2250</a>
<a href="#cl-2251">2251</a>
<a href="#cl-2252">2252</a>
<a href="#cl-2253">2253</a>
<a href="#cl-2254">2254</a>
<a href="#cl-2255">2255</a>
<a href="#cl-2256">2256</a>
<a href="#cl-2257">2257</a>
<a href="#cl-2258">2258</a>
<a href="#cl-2259">2259</a>
<a href="#cl-2260">2260</a>
<a href="#cl-2261">2261</a>
<a href="#cl-2262">2262</a>
<a href="#cl-2263">2263</a>
<a href="#cl-2264">2264</a>
<a href="#cl-2265">2265</a>
<a href="#cl-2266">2266</a>
<a href="#cl-2267">2267</a>
<a href="#cl-2268">2268</a>
<a href="#cl-2269">2269</a>
<a href="#cl-2270">2270</a>
<a href="#cl-2271">2271</a>
<a href="#cl-2272">2272</a>
<a href="#cl-2273">2273</a>
<a href="#cl-2274">2274</a>
<a href="#cl-2275">2275</a>
<a href="#cl-2276">2276</a>
<a href="#cl-2277">2277</a>
<a href="#cl-2278">2278</a>
<a href="#cl-2279">2279</a>
<a href="#cl-2280">2280</a>
<a href="#cl-2281">2281</a>
<a href="#cl-2282">2282</a>
<a href="#cl-2283">2283</a>
<a href="#cl-2284">2284</a>
<a href="#cl-2285">2285</a>
<a href="#cl-2286">2286</a>
<a href="#cl-2287">2287</a>
<a href="#cl-2288">2288</a>
<a href="#cl-2289">2289</a>
<a href="#cl-2290">2290</a>
<a href="#cl-2291">2291</a>
<a href="#cl-2292">2292</a>
<a href="#cl-2293">2293</a>
<a href="#cl-2294">2294</a>
<a href="#cl-2295">2295</a>
<a href="#cl-2296">2296</a>
<a href="#cl-2297">2297</a>
<a href="#cl-2298">2298</a>
<a href="#cl-2299">2299</a>
<a href="#cl-2300">2300</a>
<a href="#cl-2301">2301</a>
<a href="#cl-2302">2302</a>
<a href="#cl-2303">2303</a>
<a href="#cl-2304">2304</a>
<a href="#cl-2305">2305</a>
<a href="#cl-2306">2306</a>
<a href="#cl-2307">2307</a>
<a href="#cl-2308">2308</a>
<a href="#cl-2309">2309</a>
<a href="#cl-2310">2310</a>
<a href="#cl-2311">2311</a>
<a href="#cl-2312">2312</a>
<a href="#cl-2313">2313</a>
<a href="#cl-2314">2314</a>
<a href="#cl-2315">2315</a>
<a href="#cl-2316">2316</a>
<a href="#cl-2317">2317</a>
<a href="#cl-2318">2318</a>
<a href="#cl-2319">2319</a>
<a href="#cl-2320">2320</a>
<a href="#cl-2321">2321</a>
<a href="#cl-2322">2322</a>
<a href="#cl-2323">2323</a>
<a href="#cl-2324">2324</a>
<a href="#cl-2325">2325</a>
<a href="#cl-2326">2326</a>
<a href="#cl-2327">2327</a>
<a href="#cl-2328">2328</a>
<a href="#cl-2329">2329</a>
<a href="#cl-2330">2330</a>
<a href="#cl-2331">2331</a>
<a href="#cl-2332">2332</a>
<a href="#cl-2333">2333</a>
<a href="#cl-2334">2334</a>
<a href="#cl-2335">2335</a>
<a href="#cl-2336">2336</a>
<a href="#cl-2337">2337</a>
<a href="#cl-2338">2338</a>
<a href="#cl-2339">2339</a>
<a href="#cl-2340">2340</a>
<a href="#cl-2341">2341</a>
<a href="#cl-2342">2342</a>
<a href="#cl-2343">2343</a>
<a href="#cl-2344">2344</a>
<a href="#cl-2345">2345</a>
<a href="#cl-2346">2346</a>
<a href="#cl-2347">2347</a>
<a href="#cl-2348">2348</a>
<a href="#cl-2349">2349</a>
<a href="#cl-2350">2350</a>
<a href="#cl-2351">2351</a>
<a href="#cl-2352">2352</a>
<a href="#cl-2353">2353</a>
<a href="#cl-2354">2354</a>
<a href="#cl-2355">2355</a>
<a href="#cl-2356">2356</a>
<a href="#cl-2357">2357</a>
<a href="#cl-2358">2358</a>
<a href="#cl-2359">2359</a>
<a href="#cl-2360">2360</a>
<a href="#cl-2361">2361</a>
<a href="#cl-2362">2362</a>
<a href="#cl-2363">2363</a>
<a href="#cl-2364">2364</a>
<a href="#cl-2365">2365</a>
<a href="#cl-2366">2366</a>
<a href="#cl-2367">2367</a>
<a href="#cl-2368">2368</a>
<a href="#cl-2369">2369</a>
<a href="#cl-2370">2370</a>
<a href="#cl-2371">2371</a>
<a href="#cl-2372">2372</a>
<a href="#cl-2373">2373</a>
<a href="#cl-2374">2374</a>
<a href="#cl-2375">2375</a>
<a href="#cl-2376">2376</a>
<a href="#cl-2377">2377</a>
<a href="#cl-2378">2378</a>
<a href="#cl-2379">2379</a>
<a href="#cl-2380">2380</a>
<a href="#cl-2381">2381</a>
<a href="#cl-2382">2382</a>
<a href="#cl-2383">2383</a>
<a href="#cl-2384">2384</a>
<a href="#cl-2385">2385</a>
<a href="#cl-2386">2386</a>
<a href="#cl-2387">2387</a>
<a href="#cl-2388">2388</a>
<a href="#cl-2389">2389</a>
<a href="#cl-2390">2390</a>
<a href="#cl-2391">2391</a>
<a href="#cl-2392">2392</a>
<a href="#cl-2393">2393</a>
<a href="#cl-2394">2394</a>
<a href="#cl-2395">2395</a>
<a href="#cl-2396">2396</a>
<a href="#cl-2397">2397</a>
<a href="#cl-2398">2398</a>
<a href="#cl-2399">2399</a>
<a href="#cl-2400">2400</a>
<a href="#cl-2401">2401</a>
<a href="#cl-2402">2402</a>
<a href="#cl-2403">2403</a>
<a href="#cl-2404">2404</a>
<a href="#cl-2405">2405</a>
<a href="#cl-2406">2406</a>
<a href="#cl-2407">2407</a>
<a href="#cl-2408">2408</a>
<a href="#cl-2409">2409</a>
<a href="#cl-2410">2410</a>
<a href="#cl-2411">2411</a>
<a href="#cl-2412">2412</a>
<a href="#cl-2413">2413</a>
<a href="#cl-2414">2414</a>
<a href="#cl-2415">2415</a>
<a href="#cl-2416">2416</a>
<a href="#cl-2417">2417</a>
<a href="#cl-2418">2418</a>
<a href="#cl-2419">2419</a>
<a href="#cl-2420">2420</a>
<a href="#cl-2421">2421</a>
<a href="#cl-2422">2422</a>
<a href="#cl-2423">2423</a>
<a href="#cl-2424">2424</a>
<a href="#cl-2425">2425</a>
<a href="#cl-2426">2426</a>
<a href="#cl-2427">2427</a>
<a href="#cl-2428">2428</a>
<a href="#cl-2429">2429</a>
<a href="#cl-2430">2430</a>
<a href="#cl-2431">2431</a>
<a href="#cl-2432">2432</a>
<a href="#cl-2433">2433</a>
<a href="#cl-2434">2434</a>
<a href="#cl-2435">2435</a>
<a href="#cl-2436">2436</a>
<a href="#cl-2437">2437</a>
<a href="#cl-2438">2438</a>
<a href="#cl-2439">2439</a>
<a href="#cl-2440">2440</a>
<a href="#cl-2441">2441</a>
<a href="#cl-2442">2442</a>
<a href="#cl-2443">2443</a>
<a href="#cl-2444">2444</a>
<a href="#cl-2445">2445</a>
<a href="#cl-2446">2446</a>
<a href="#cl-2447">2447</a>
<a href="#cl-2448">2448</a>
<a href="#cl-2449">2449</a>
<a href="#cl-2450">2450</a>
<a href="#cl-2451">2451</a>
<a href="#cl-2452">2452</a>
<a href="#cl-2453">2453</a>
<a href="#cl-2454">2454</a>
<a href="#cl-2455">2455</a>
<a href="#cl-2456">2456</a>
<a href="#cl-2457">2457</a>
<a href="#cl-2458">2458</a>
<a href="#cl-2459">2459</a>
<a href="#cl-2460">2460</a>
<a href="#cl-2461">2461</a>
<a href="#cl-2462">2462</a>
<a href="#cl-2463">2463</a>
<a href="#cl-2464">2464</a>
<a href="#cl-2465">2465</a>
<a href="#cl-2466">2466</a>
<a href="#cl-2467">2467</a>
<a href="#cl-2468">2468</a>
<a href="#cl-2469">2469</a>
<a href="#cl-2470">2470</a>
<a href="#cl-2471">2471</a>
<a href="#cl-2472">2472</a>
<a href="#cl-2473">2473</a>
<a href="#cl-2474">2474</a>
<a href="#cl-2475">2475</a>
<a href="#cl-2476">2476</a>
<a href="#cl-2477">2477</a>
<a href="#cl-2478">2478</a>
<a href="#cl-2479">2479</a>
<a href="#cl-2480">2480</a>
<a href="#cl-2481">2481</a>
<a href="#cl-2482">2482</a>
<a href="#cl-2483">2483</a>
<a href="#cl-2484">2484</a>
<a href="#cl-2485">2485</a>
<a href="#cl-2486">2486</a>
<a href="#cl-2487">2487</a>
<a href="#cl-2488">2488</a>
<a href="#cl-2489">2489</a>
<a href="#cl-2490">2490</a>
<a href="#cl-2491">2491</a>
<a href="#cl-2492">2492</a>
<a href="#cl-2493">2493</a>
<a href="#cl-2494">2494</a>
<a href="#cl-2495">2495</a>
<a href="#cl-2496">2496</a>
<a href="#cl-2497">2497</a>
<a href="#cl-2498">2498</a>
<a href="#cl-2499">2499</a>
<a href="#cl-2500">2500</a>
<a href="#cl-2501">2501</a>
<a href="#cl-2502">2502</a>
<a href="#cl-2503">2503</a>
<a href="#cl-2504">2504</a>
<a href="#cl-2505">2505</a>
<a href="#cl-2506">2506</a>
<a href="#cl-2507">2507</a>
<a href="#cl-2508">2508</a>
<a href="#cl-2509">2509</a>
<a href="#cl-2510">2510</a>
<a href="#cl-2511">2511</a>
<a href="#cl-2512">2512</a>
<a href="#cl-2513">2513</a>
<a href="#cl-2514">2514</a>
<a href="#cl-2515">2515</a>
<a href="#cl-2516">2516</a>
<a href="#cl-2517">2517</a>
<a href="#cl-2518">2518</a>
<a href="#cl-2519">2519</a>
<a href="#cl-2520">2520</a>
<a href="#cl-2521">2521</a>
<a href="#cl-2522">2522</a>
<a href="#cl-2523">2523</a>
<a href="#cl-2524">2524</a>
<a href="#cl-2525">2525</a>
<a href="#cl-2526">2526</a>
<a href="#cl-2527">2527</a>
<a href="#cl-2528">2528</a>
<a href="#cl-2529">2529</a>
<a href="#cl-2530">2530</a>
<a href="#cl-2531">2531</a>
<a href="#cl-2532">2532</a>
<a href="#cl-2533">2533</a>
<a href="#cl-2534">2534</a>
<a href="#cl-2535">2535</a>
<a href="#cl-2536">2536</a>
<a href="#cl-2537">2537</a>
<a href="#cl-2538">2538</a>
<a href="#cl-2539">2539</a>
<a href="#cl-2540">2540</a>
<a href="#cl-2541">2541</a>
<a href="#cl-2542">2542</a>
<a href="#cl-2543">2543</a>
<a href="#cl-2544">2544</a>
<a href="#cl-2545">2545</a>
<a href="#cl-2546">2546</a>
<a href="#cl-2547">2547</a>
<a href="#cl-2548">2548</a>
<a href="#cl-2549">2549</a>
<a href="#cl-2550">2550</a>
<a href="#cl-2551">2551</a>
<a href="#cl-2552">2552</a>
<a href="#cl-2553">2553</a>
<a href="#cl-2554">2554</a>
<a href="#cl-2555">2555</a>
<a href="#cl-2556">2556</a>
<a href="#cl-2557">2557</a>
<a href="#cl-2558">2558</a>
<a href="#cl-2559">2559</a>
<a href="#cl-2560">2560</a>
<a href="#cl-2561">2561</a>
<a href="#cl-2562">2562</a>
<a href="#cl-2563">2563</a>
<a href="#cl-2564">2564</a>
<a href="#cl-2565">2565</a>
<a href="#cl-2566">2566</a>
<a href="#cl-2567">2567</a>
<a href="#cl-2568">2568</a>
<a href="#cl-2569">2569</a>
<a href="#cl-2570">2570</a>
<a href="#cl-2571">2571</a>
<a href="#cl-2572">2572</a>
<a href="#cl-2573">2573</a>
<a href="#cl-2574">2574</a>
<a href="#cl-2575">2575</a>
<a href="#cl-2576">2576</a>
<a href="#cl-2577">2577</a>
<a href="#cl-2578">2578</a>
<a href="#cl-2579">2579</a>
<a href="#cl-2580">2580</a>
<a href="#cl-2581">2581</a>
<a href="#cl-2582">2582</a>
<a href="#cl-2583">2583</a>
<a href="#cl-2584">2584</a>
<a href="#cl-2585">2585</a>
<a href="#cl-2586">2586</a>
<a href="#cl-2587">2587</a>
<a href="#cl-2588">2588</a>
<a href="#cl-2589">2589</a>
<a href="#cl-2590">2590</a>
<a href="#cl-2591">2591</a>
<a href="#cl-2592">2592</a>
<a href="#cl-2593">2593</a>
<a href="#cl-2594">2594</a>
<a href="#cl-2595">2595</a>
<a href="#cl-2596">2596</a>
<a href="#cl-2597">2597</a>
<a href="#cl-2598">2598</a>
<a href="#cl-2599">2599</a>
<a href="#cl-2600">2600</a>
<a href="#cl-2601">2601</a>
<a href="#cl-2602">2602</a>
<a href="#cl-2603">2603</a>
<a href="#cl-2604">2604</a>
<a href="#cl-2605">2605</a>
<a href="#cl-2606">2606</a>
<a href="#cl-2607">2607</a>
<a href="#cl-2608">2608</a>
<a href="#cl-2609">2609</a>
<a href="#cl-2610">2610</a>
<a href="#cl-2611">2611</a>
<a href="#cl-2612">2612</a>
<a href="#cl-2613">2613</a>
<a href="#cl-2614">2614</a>
<a href="#cl-2615">2615</a>
<a href="#cl-2616">2616</a>
<a href="#cl-2617">2617</a>
<a href="#cl-2618">2618</a>
<a href="#cl-2619">2619</a>
<a href="#cl-2620">2620</a>
<a href="#cl-2621">2621</a>
<a href="#cl-2622">2622</a>
<a href="#cl-2623">2623</a>
<a href="#cl-2624">2624</a>
<a href="#cl-2625">2625</a>
<a href="#cl-2626">2626</a>
<a href="#cl-2627">2627</a>
<a href="#cl-2628">2628</a>
<a href="#cl-2629">2629</a>
<a href="#cl-2630">2630</a>
<a href="#cl-2631">2631</a>
<a href="#cl-2632">2632</a>
<a href="#cl-2633">2633</a>
<a href="#cl-2634">2634</a>
<a href="#cl-2635">2635</a>
<a href="#cl-2636">2636</a>
<a href="#cl-2637">2637</a>
<a href="#cl-2638">2638</a>
<a href="#cl-2639">2639</a>
<a href="#cl-2640">2640</a>
<a href="#cl-2641">2641</a>
<a href="#cl-2642">2642</a>
<a href="#cl-2643">2643</a>
<a href="#cl-2644">2644</a>
<a href="#cl-2645">2645</a>
<a href="#cl-2646">2646</a>
<a href="#cl-2647">2647</a>
<a href="#cl-2648">2648</a>
<a href="#cl-2649">2649</a>
<a href="#cl-2650">2650</a>
<a href="#cl-2651">2651</a>
<a href="#cl-2652">2652</a>
<a href="#cl-2653">2653</a>
<a href="#cl-2654">2654</a>
<a href="#cl-2655">2655</a>
<a href="#cl-2656">2656</a>
<a href="#cl-2657">2657</a>
<a href="#cl-2658">2658</a>
<a href="#cl-2659">2659</a>
<a href="#cl-2660">2660</a>
<a href="#cl-2661">2661</a>
<a href="#cl-2662">2662</a>
<a href="#cl-2663">2663</a>
<a href="#cl-2664">2664</a>
<a href="#cl-2665">2665</a>
<a href="#cl-2666">2666</a>
<a href="#cl-2667">2667</a>
<a href="#cl-2668">2668</a>
<a href="#cl-2669">2669</a>
<a href="#cl-2670">2670</a>
<a href="#cl-2671">2671</a>
<a href="#cl-2672">2672</a>
<a href="#cl-2673">2673</a>
<a href="#cl-2674">2674</a>
<a href="#cl-2675">2675</a>
<a href="#cl-2676">2676</a>
<a href="#cl-2677">2677</a>
<a href="#cl-2678">2678</a>
<a href="#cl-2679">2679</a>
<a href="#cl-2680">2680</a>
<a href="#cl-2681">2681</a>
<a href="#cl-2682">2682</a>
<a href="#cl-2683">2683</a>
<a href="#cl-2684">2684</a>
<a href="#cl-2685">2685</a>
<a href="#cl-2686">2686</a>
<a href="#cl-2687">2687</a>
<a href="#cl-2688">2688</a>
<a href="#cl-2689">2689</a>
<a href="#cl-2690">2690</a>
<a href="#cl-2691">2691</a>
</pre></div></td><td class="code"><div class="highlight"><pre><a name="cl-1"></a><span class="c"># -*- coding: utf-8 -*-</span>
<a name="cl-2"></a>
<a name="cl-3"></a><span class="sd">&quot;&quot;&quot;</span>
<a name="cl-4"></a><span class="sd">BSXPath.py: XPathEvaluator Extension for BeautifulSoup</span>
<a name="cl-5"></a>
<a name="cl-6"></a><span class="sd">&quot;&quot;&quot;</span>
<a name="cl-7"></a><span class="n">__version__</span> <span class="o">=</span> <span class="s">&#39;0.01e&#39;</span>             <span class="c"># based on JavaScript-XPath 0.1.11 (c) 2007 Cybozu Labs, Inc. (http://coderepos.org/share/wiki/JavaScript-XPath)</span>
<a name="cl-8"></a><span class="n">__date__</span>    <span class="o">=</span> <span class="s">&#39;2009-04-12&#39;</span>
<a name="cl-9"></a><span class="n">__license__</span> <span class="o">=</span> <span class="s">&#39;MIT-style license&#39;</span>
<a name="cl-10"></a><span class="n">__author__</span>  <span class="o">=</span> <span class="s">&#39;furyu&#39;</span>             <span class="c"># http://furyu.tea-nifty.com/annex/</span>
<a name="cl-11"></a>                                  <span class="c"># http://d.hatena.ne.jp/furyu-tei/</span>
<a name="cl-12"></a><span class="sd">&quot;&quot;&quot;</span>
<a name="cl-13"></a><span class="sd">Usage:</span>
<a name="cl-14"></a><span class="sd">  from BSXPath import BSXPathEvaluator,XPathResult</span>
<a name="cl-15"></a><span class="sd">  </span>
<a name="cl-16"></a><span class="sd">  #*** PREPARATION (create object)</span>
<a name="cl-17"></a><span class="sd">  document = BSXPathEvaluator(&lt;html&gt;) # BSXPathEvaluator is sub-class of BeautifulSoup</span>
<a name="cl-18"></a><span class="sd">    # html: HTML (text string)</span>
<a name="cl-19"></a><span class="sd">  </span>
<a name="cl-20"></a><span class="sd">  #*** BASIC OPERATIONS</span>
<a name="cl-21"></a><span class="sd">  result = document.evaluate(&lt;expression&gt;,&lt;node&gt;,None,&lt;type&gt;,None)</span>
<a name="cl-22"></a><span class="sd">    # expression: XPath expression</span>
<a name="cl-23"></a><span class="sd">    # node      : base context-node(document is document-root)</span>
<a name="cl-24"></a><span class="sd">    # type      : XPathResult.&lt;name&gt;</span>
<a name="cl-25"></a><span class="sd">    #   name      : ANY_TYPE, NUMBER_TYPE, STRING_TYPE, BOOLEAN_TYPE, UNORDERED_NODE_ITERATOR_TYPE, ORDERED_NODE_ITERATOR_TYPE</span>
<a name="cl-26"></a><span class="sd">    #               UNORDERED_NODE_SNAPSHOT_TYPE, ORDERED_NODE_SNAPSHOT_TYPE, ANY_UNORDERED_NODE_TYPE, FIRST_ORDERED_NODE_TYPE</span>
<a name="cl-27"></a><span class="sd">    # (*) 3rd(resolver) and 5th(result) arguments are not implemented</span>
<a name="cl-28"></a><span class="sd">  length = result.snapshotLength</span>
<a name="cl-29"></a><span class="sd">  node   = result.snapshotItem(&lt;number&gt;)</span>
<a name="cl-30"></a><span class="sd">  </span>
<a name="cl-31"></a><span class="sd">  #*** USEFUL WRAPPER-FUNCTIONS</span>
<a name="cl-32"></a><span class="sd">  nodes = document.getItemList(&lt;expression&gt;[,&lt;node&gt;])</span>
<a name="cl-33"></a><span class="sd">  first = document.getFirstItem(&lt;expression&gt;[,&lt;node&gt;])</span>
<a name="cl-34"></a><span class="sd">    # expression: XPath expression</span>
<a name="cl-35"></a><span class="sd">    # node(optional): base context-node(default: document(document-root))</span>
<a name="cl-36"></a>
<a name="cl-37"></a>
<a name="cl-38"></a><span class="sd">Examples:</span>
<a name="cl-39"></a><span class="sd">  from BSXPath import BSXPathEvaluator,XPathResult</span>
<a name="cl-40"></a><span class="sd">  </span>
<a name="cl-41"></a><span class="sd">  html = &#39;&lt;html&gt;&lt;head&gt;&lt;title&gt;Hello, DOM 3 XPath!&lt;/title&gt;&lt;/head&gt;&lt;body&gt;&lt;h1&gt;Hello, DOM 3 XPath!&lt;/h1&gt;&lt;p&gt;This is XPathEvaluator Extension for BeautifulSoup.&lt;/p&gt;&lt;p&gt;This is based on JavaScript-XPath!&lt;/p&gt;&lt;/body&gt;&#39;</span>
<a name="cl-42"></a><span class="sd">  </span>
<a name="cl-43"></a><span class="sd">  document = BSXPathEvaluator(html)</span>
<a name="cl-44"></a><span class="sd">  </span>
<a name="cl-45"></a><span class="sd">  result = document.evaluate(&#39;//h1/text()[1]&#39;,document,None,XPathResult.STRING_TYPE,None)</span>
<a name="cl-46"></a><span class="sd">  print result.stringValue</span>
<a name="cl-47"></a><span class="sd">  # Hello, DOM 3 XPath!</span>
<a name="cl-48"></a>
<a name="cl-49"></a><span class="sd">  result = document.evaluate(&#39;//h1&#39;,document,None,XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,None)</span>
<a name="cl-50"></a><span class="sd">  print result.snapshotLength</span>
<a name="cl-51"></a><span class="sd">  # 1</span>
<a name="cl-52"></a><span class="sd">  print result.snapshotItem(0)</span>
<a name="cl-53"></a><span class="sd">  # &lt;h1&gt;Hello, DOM 3 XPath!&lt;/h1&gt;</span>
<a name="cl-54"></a><span class="sd">  </span>
<a name="cl-55"></a><span class="sd">  nodes = document.getItemList(&#39;//p&#39;)</span>
<a name="cl-56"></a><span class="sd">  print len(nodes)</span>
<a name="cl-57"></a><span class="sd">  # 2</span>
<a name="cl-58"></a><span class="sd">  print nodes</span>
<a name="cl-59"></a><span class="sd">  # [&lt;p&gt;This is XPathEvaluator Extension for BeautifulSoup.&lt;/p&gt;, &lt;p&gt;This is based on JavaScript-XPath!&lt;/p&gt;]</span>
<a name="cl-60"></a><span class="sd">  </span>
<a name="cl-61"></a><span class="sd">  first = document.getFirstItem(&#39;//p&#39;)</span>
<a name="cl-62"></a><span class="sd">  print first</span>
<a name="cl-63"></a><span class="sd">  # &lt;p&gt;This is XPathEvaluator Extension for BeautifulSoup.&lt;/p&gt;</span>
<a name="cl-64"></a>
<a name="cl-65"></a>
<a name="cl-66"></a><span class="sd">Notice:</span>
<a name="cl-67"></a><span class="sd">  - This is based on JavaScript-XPath (c) 2007 Cybozu Labs, Inc. (http://coderepos.org/share/wiki/JavaScript-XPath)</span>
<a name="cl-68"></a><span class="sd">  - Required:</span>
<a name="cl-69"></a><span class="sd">     - Python 2.5+</span>
<a name="cl-70"></a><span class="sd">     - BeautifulSoup 3.0.7+(recommended) or 3.1.0+</span>
<a name="cl-71"></a>
<a name="cl-72"></a><span class="sd">&quot;&quot;&quot;</span>
<a name="cl-73"></a><span class="kn">import</span> <span class="nn">re</span><span class="o">,</span><span class="nn">types</span><span class="o">,</span><span class="nn">math</span><span class="o">,</span><span class="nn">datetime</span>
<a name="cl-74"></a><span class="c">#import logging</span>
<a name="cl-75"></a><span class="kn">from</span> <span class="nn">BeautifulSoup</span> <span class="kn">import</span> <span class="o">*</span>
<a name="cl-76"></a>
<a name="cl-77"></a><span class="k">try</span><span class="p">:</span>
<a name="cl-78"></a>  <span class="k">if</span> <span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">:</span>
<a name="cl-79"></a>    <span class="k">pass</span>
<a name="cl-80"></a><span class="k">except</span><span class="p">:</span>
<a name="cl-81"></a>  <span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="o">=</span><span class="s">&#39;utf-8&#39;</span>
<a name="cl-82"></a>
<a name="cl-83"></a>
<a name="cl-84"></a><span class="c">#***** Optional Parameters</span>
<a name="cl-85"></a><span class="n">USE_NODE_CACHE</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-86"></a><span class="n">USE_NODE_INDEX</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-87"></a>
<a name="cl-88"></a>
<a name="cl-89"></a><span class="c">#***** General Functions</span>
<a name="cl-90"></a><span class="k">def</span> <span class="nf">throwError</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
<a name="cl-91"></a>  <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">,</span> <span class="nb">str</span>
<a name="cl-92"></a>  
<a name="cl-93"></a>
<a name="cl-94"></a><span class="k">def</span> <span class="nf">typeof</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
<a name="cl-95"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">bool</span><span class="p">):</span>
<a name="cl-96"></a>    <span class="k">return</span> <span class="s">&#39;boolean&#39;</span>
<a name="cl-97"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">int</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">float</span><span class="p">):</span>
<a name="cl-98"></a>    <span class="k">return</span> <span class="s">&#39;number&#39;</span>
<a name="cl-99"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">basestring</span><span class="p">):</span>
<a name="cl-100"></a>    <span class="k">return</span> <span class="s">&#39;string&#39;</span>
<a name="cl-101"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="n">types</span><span class="o">.</span><span class="n">FunctionType</span><span class="p">):</span>
<a name="cl-102"></a>    <span class="k">return</span> <span class="s">&#39;function&#39;</span>
<a name="cl-103"></a>  <span class="k">return</span> <span class="s">&#39;object&#39;</span>
<a name="cl-104"></a>
<a name="cl-105"></a>
<a name="cl-106"></a><span class="k">def</span> <span class="nf">isNaN</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
<a name="cl-107"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">int</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">float</span><span class="p">):</span>
<a name="cl-108"></a>    <span class="k">return</span> <span class="bp">False</span>
<a name="cl-109"></a>  <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">basestring</span><span class="p">):</span>
<a name="cl-110"></a>    <span class="k">return</span> <span class="bp">True</span>
<a name="cl-111"></a>  <span class="k">if</span> <span class="n">obj</span><span class="o">.</span><span class="n">isdigit</span><span class="p">():</span>
<a name="cl-112"></a>    <span class="k">return</span> <span class="bp">False</span>
<a name="cl-113"></a>  <span class="k">try</span><span class="p">:</span>
<a name="cl-114"></a>    <span class="nb">float</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
<a name="cl-115"></a>    <span class="k">return</span> <span class="bp">False</span>
<a name="cl-116"></a>  <span class="k">except</span><span class="p">:</span>
<a name="cl-117"></a>    <span class="k">return</span> <span class="bp">True</span>
<a name="cl-118"></a>
<a name="cl-119"></a>
<a name="cl-120"></a><span class="k">def</span> <span class="nf">toNumber</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
<a name="cl-121"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">int</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">float</span><span class="p">):</span>
<a name="cl-122"></a>    <span class="k">return</span> <span class="n">obj</span>
<a name="cl-123"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">basestring</span><span class="p">):</span>
<a name="cl-124"></a>    <span class="k">if</span> <span class="n">obj</span><span class="o">.</span><span class="n">isdigit</span><span class="p">():</span>
<a name="cl-125"></a>      <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
<a name="cl-126"></a>    <span class="k">try</span><span class="p">:</span>
<a name="cl-127"></a>      <span class="k">return</span> <span class="nb">float</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
<a name="cl-128"></a>    <span class="k">except</span><span class="p">:</span>
<a name="cl-129"></a>      <span class="k">return</span> <span class="n">obj</span>
<a name="cl-130"></a>  <span class="k">return</span> <span class="n">obj</span>
<a name="cl-131"></a>
<a name="cl-132"></a><span class="k">def</span> <span class="nf">toBoolean</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
<a name="cl-133"></a>  <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
<a name="cl-134"></a>
<a name="cl-135"></a>
<a name="cl-136"></a><span class="k">def</span> <span class="nf">toString</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
<a name="cl-137"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">bool</span><span class="p">):</span>
<a name="cl-138"></a>    <span class="k">return</span> <span class="s">u&#39;true&#39;</span> <span class="k">if</span> <span class="n">obj</span> <span class="k">else</span> <span class="s">u&#39;false&#39;</span>
<a name="cl-139"></a>  <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">str</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">int</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">float</span><span class="p">):</span>
<a name="cl-140"></a>    <span class="k">return</span> <span class="nb">unicode</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
<a name="cl-141"></a>  <span class="k">return</span> <span class="n">obj</span>
<a name="cl-142"></a>
<a name="cl-143"></a>
<a name="cl-144"></a>
<a name="cl-145"></a><span class="c">#***** General Classes</span>
<a name="cl-146"></a><span class="k">class</span> <span class="nc">ExtDict</span><span class="p">(</span><span class="nb">dict</span><span class="p">):</span>
<a name="cl-147"></a>  <span class="k">def</span> <span class="nf">__getattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-148"></a>    <span class="k">try</span><span class="p">:</span>
<a name="cl-149"></a>      <span class="n">attr</span><span class="o">=</span><span class="nb">super</span><span class="p">(</span><span class="n">ExtDict</span><span class="p">,</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__getattr__</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
<a name="cl-150"></a>    <span class="k">except</span><span class="p">:</span>
<a name="cl-151"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="n">name</span><span class="p">):</span>
<a name="cl-152"></a>        <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">,</span><span class="n">name</span>
<a name="cl-153"></a>      <span class="n">attr</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
<a name="cl-154"></a>    <span class="k">return</span> <span class="n">attr</span>
<a name="cl-155"></a>
<a name="cl-156"></a>
<a name="cl-157"></a>
<a name="cl-158"></a><span class="c">#***** Common Definitions</span>
<a name="cl-159"></a><span class="n">indent_space</span><span class="o">=</span><span class="s">&#39;    &#39;</span>
<a name="cl-160"></a>
<a name="cl-161"></a>
<a name="cl-162"></a><span class="c">#{ // Regular Expressions</span>
<a name="cl-163"></a><span class="n">re_has_ualpha</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;(?![0-9])[\w]&#39;</span><span class="p">)</span>
<a name="cl-164"></a><span class="n">re_seqspace</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;\s+&#39;</span><span class="p">)</span>
<a name="cl-165"></a><span class="n">re_firstspace</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^\s&#39;</span><span class="p">)</span>
<a name="cl-166"></a><span class="n">re_lastspace</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;\s$&#39;</span><span class="p">)</span>
<a name="cl-167"></a><span class="c">#} // end of Regular Expressions</span>
<a name="cl-168"></a>
<a name="cl-169"></a>
<a name="cl-170"></a><span class="c">#{ // NodeTypeDOM</span>
<a name="cl-171"></a><span class="n">NodeTypeDOM</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-172"></a>  <span class="s">&#39;ANY_NODE&#39;</span>                   <span class="p">:</span><span class="mi">0</span>
<a name="cl-173"></a><span class="p">,</span> <span class="s">&#39;ELEMENT_NODE&#39;</span>               <span class="p">:</span><span class="mi">1</span>
<a name="cl-174"></a><span class="p">,</span> <span class="s">&#39;ATTRIBUTE_NODE&#39;</span>             <span class="p">:</span><span class="mi">2</span>
<a name="cl-175"></a><span class="p">,</span> <span class="s">&#39;TEXT_NODE&#39;</span>                  <span class="p">:</span><span class="mi">3</span>
<a name="cl-176"></a><span class="p">,</span> <span class="s">&#39;CDATA_SECTION_NODE&#39;</span>         <span class="p">:</span><span class="mi">4</span>
<a name="cl-177"></a><span class="p">,</span> <span class="s">&#39;ENTITY_REFERENCE_NODE&#39;</span>      <span class="p">:</span><span class="mi">5</span>
<a name="cl-178"></a><span class="p">,</span> <span class="s">&#39;ENTITY_NODE&#39;</span>                <span class="p">:</span><span class="mi">6</span>
<a name="cl-179"></a><span class="p">,</span> <span class="s">&#39;PROCESSING_INSTRUCTION_NODE&#39;</span><span class="p">:</span><span class="mi">7</span>
<a name="cl-180"></a><span class="p">,</span> <span class="s">&#39;COMMENT_NODE&#39;</span>               <span class="p">:</span><span class="mi">8</span>
<a name="cl-181"></a><span class="p">,</span> <span class="s">&#39;DOCUMENT_NODE&#39;</span>              <span class="p">:</span><span class="mi">9</span>
<a name="cl-182"></a><span class="p">,</span> <span class="s">&#39;DOCUMENT_TYPE_NODE&#39;</span>         <span class="p">:</span><span class="mi">10</span>
<a name="cl-183"></a><span class="p">,</span> <span class="s">&#39;DOCUMENT_FRAGMENT_NODE&#39;</span>     <span class="p">:</span><span class="mi">11</span>
<a name="cl-184"></a><span class="p">,</span> <span class="s">&#39;NOTATION_NODE&#39;</span>              <span class="p">:</span><span class="mi">12</span>
<a name="cl-185"></a><span class="p">})</span>
<a name="cl-186"></a>
<a name="cl-187"></a><span class="n">NodeTypeBS</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-188"></a>  <span class="s">&#39;BSXPathEvaluator&#39;</span>     <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span>
<a name="cl-189"></a><span class="p">,</span> <span class="s">&#39;NavigableString&#39;</span>      <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">TEXT_NODE</span>
<a name="cl-190"></a><span class="p">,</span> <span class="s">&#39;CData&#39;</span>                <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">CDATA_SECTION_NODE</span>
<a name="cl-191"></a><span class="p">,</span> <span class="s">&#39;ProcessingInstruction&#39;</span><span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">PROCESSING_INSTRUCTION_NODE</span>
<a name="cl-192"></a><span class="p">,</span> <span class="s">&#39;Comment&#39;</span>              <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">COMMENT_NODE</span>
<a name="cl-193"></a><span class="p">,</span> <span class="s">&#39;Declaration&#39;</span>          <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ANY_NODE</span>
<a name="cl-194"></a><span class="p">,</span> <span class="s">&#39;Tag&#39;</span>                  <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span>
<a name="cl-195"></a><span class="p">})</span>
<a name="cl-196"></a><span class="c">#} // end of NodeTypeDOM</span>
<a name="cl-197"></a>
<a name="cl-198"></a>
<a name="cl-199"></a><span class="c">#{ // NodeUtil</span>
<a name="cl-200"></a><span class="k">def</span> <span class="nf">makeNodeUtils</span><span class="p">():</span>
<a name="cl-201"></a>  <span class="n">re_type_document_type</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^DOCTYPE\s&#39;</span><span class="p">)</span>
<a name="cl-202"></a>  <span class="n">re_type_entity</span>       <span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^ENTITY\s&#39;</span><span class="p">)</span>
<a name="cl-203"></a>  <span class="n">re_type_notation</span>     <span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^NOTATION\s&#39;</span><span class="p">)</span>
<a name="cl-204"></a>  
<a name="cl-205"></a>  <span class="c">#re_processing_instruction=re.compile(r&#39;^(.*?)\s+(.*?)\?*$&#39;)</span>
<a name="cl-206"></a>  <span class="n">re_processing_instruction</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^(.*?)(\s+.*?)\?*$&#39;</span><span class="p">)</span>
<a name="cl-207"></a>  
<a name="cl-208"></a>  <span class="n">re_declaration_name</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^([^\s]+)\s+([\%]?)\s*([^\s]+)\s&#39;</span><span class="p">)</span>
<a name="cl-209"></a>  
<a name="cl-210"></a>  <span class="k">def</span> <span class="nf">makeNU_BS</span><span class="p">():</span>
<a name="cl-211"></a>    <span class="k">def</span> <span class="nf">_nodeType</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-212"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;nodeType&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-213"></a>        <span class="k">return</span> <span class="n">node</span><span class="o">.</span><span class="n">nodeType</span>
<a name="cl-214"></a>      <span class="n">nodeType</span><span class="o">=</span><span class="n">NodeTypeBS</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__name__</span><span class="p">)</span>
<a name="cl-215"></a>      <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ANY_NODE</span><span class="p">:</span>
<a name="cl-216"></a>        <span class="nb">str</span><span class="o">=</span><span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-217"></a>        <span class="k">if</span> <span class="n">re_type_document_type</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
<a name="cl-218"></a>          <span class="n">nodeType</span><span class="o">=</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_TYPE_NODE</span>
<a name="cl-219"></a>        <span class="k">elif</span> <span class="n">re_type_entity</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
<a name="cl-220"></a>          <span class="n">nodeType</span><span class="o">=</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ENTITY_NODE</span>
<a name="cl-221"></a>        <span class="k">elif</span> <span class="n">re_type_notation</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
<a name="cl-222"></a>          <span class="n">nodeType</span><span class="o">=</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">NOTATION_NODE</span>
<a name="cl-223"></a>      <span class="k">return</span> <span class="n">nodeType</span>
<a name="cl-224"></a>    
<a name="cl-225"></a>    <span class="k">def</span> <span class="nf">_nodeName</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-226"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;nodeType&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-227"></a>        <span class="k">return</span> <span class="n">node</span><span class="o">.</span><span class="n">nodeName</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<a name="cl-228"></a>      <span class="n">nodeType</span><span class="o">=</span><span class="n">_nodeType</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-229"></a>      <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span><span class="p">:</span>
<a name="cl-230"></a>        <span class="k">return</span> <span class="s">&#39;#document&#39;</span>
<a name="cl-231"></a>      <span class="k">elif</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">TEXT_NODE</span><span class="p">:</span>
<a name="cl-232"></a>        <span class="k">return</span> <span class="s">&#39;#text&#39;</span>
<a name="cl-233"></a>      <span class="k">elif</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">CDATA_SECTION_NODE</span><span class="p">:</span>
<a name="cl-234"></a>        <span class="k">return</span> <span class="s">&#39;#cdata-section&#39;</span>
<a name="cl-235"></a>      <span class="k">elif</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">PROCESSING_INSTRUCTION_NODE</span><span class="p">:</span>
<a name="cl-236"></a>        <span class="n">mrslt</span><span class="o">=</span><span class="n">re_processing_instruction</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">))</span>
<a name="cl-237"></a>        <span class="k">if</span> <span class="n">mrslt</span><span class="p">:</span>
<a name="cl-238"></a>          <span class="k">return</span> <span class="n">mrslt</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-239"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-240"></a>          <span class="k">return</span> <span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-241"></a>      <span class="k">elif</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">COMMENT_NODE</span><span class="p">:</span>
<a name="cl-242"></a>        <span class="k">return</span> <span class="s">&#39;#comment&#39;</span>
<a name="cl-243"></a>      <span class="k">elif</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_TYPE_NODE</span> <span class="ow">or</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ENTITY_NODE</span> <span class="ow">or</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">NOTATION_NODE</span><span class="p">:</span>
<a name="cl-244"></a>        <span class="n">mrslt</span><span class="o">=</span><span class="n">re_declaration_name</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">))</span>
<a name="cl-245"></a>        <span class="k">if</span> <span class="n">mrslt</span><span class="p">:</span>
<a name="cl-246"></a>          <span class="k">return</span> <span class="n">mrslt</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<a name="cl-247"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-248"></a>          <span class="k">return</span> <span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-249"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-250"></a>        <span class="k">return</span> <span class="n">node</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<a name="cl-251"></a>    
<a name="cl-252"></a>    <span class="k">def</span> <span class="nf">_nodeValue</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-253"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;nodeType&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-254"></a>        <span class="k">return</span> <span class="n">node</span><span class="o">.</span><span class="n">nodeValue</span>
<a name="cl-255"></a>      <span class="n">nodeType</span><span class="o">=</span><span class="n">_nodeType</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-256"></a>      <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">CDATA_SECTION_NODE</span> <span class="ow">or</span> \
<a name="cl-257"></a>         <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">COMMENT_NODE</span> <span class="ow">or</span> \
<a name="cl-258"></a>         <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">TEXT_NODE</span><span class="p">:</span>
<a name="cl-259"></a>        <span class="k">return</span> <span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-260"></a>      <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">PROCESSING_INSTRUCTION_NODE</span><span class="p">:</span>
<a name="cl-261"></a>        <span class="n">mrslt</span><span class="o">=</span><span class="n">re_processing_instruction</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">))</span>
<a name="cl-262"></a>        <span class="k">if</span> <span class="n">mrslt</span><span class="p">:</span>
<a name="cl-263"></a>          <span class="k">return</span> <span class="n">mrslt</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<a name="cl-264"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-265"></a>          <span class="k">return</span> <span class="bp">None</span>
<a name="cl-266"></a>      <span class="k">return</span> <span class="bp">None</span>
<a name="cl-267"></a>    
<a name="cl-268"></a>    <span class="k">def</span> <span class="nf">_nodeAttrValue</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">attrName</span><span class="p">):</span>
<a name="cl-269"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;nodeType&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-270"></a>        <span class="k">return</span> <span class="bp">None</span>
<a name="cl-271"></a>      <span class="n">nodeType</span><span class="o">=</span><span class="n">_nodeType</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-272"></a>      <span class="k">if</span> <span class="n">nodeType</span><span class="o">!=</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span><span class="p">:</span>
<a name="cl-273"></a>        <span class="k">return</span> <span class="bp">None</span>
<a name="cl-274"></a>      <span class="k">return</span> <span class="n">node</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">attrName</span><span class="p">)</span>
<a name="cl-275"></a>    
<a name="cl-276"></a>    <span class="k">def</span> <span class="nf">_parentNode</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-277"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;nodeType&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-278"></a>        <span class="k">return</span> <span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-279"></a>      <span class="k">return</span> <span class="n">node</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-280"></a>    
<a name="cl-281"></a>    <span class="k">def</span> <span class="nf">_ownerDocument</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-282"></a>      <span class="n">owner</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;_owner&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-283"></a>      <span class="k">if</span> <span class="n">owner</span><span class="p">:</span>
<a name="cl-284"></a>        <span class="k">return</span> <span class="n">owner</span>
<a name="cl-285"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;nodeType&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-286"></a>        <span class="n">owner</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-287"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-288"></a>        <span class="n">owner</span><span class="o">=</span><span class="n">node</span>
<a name="cl-289"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-290"></a>        <span class="n">parent</span><span class="o">=</span><span class="n">owner</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-291"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">parent</span><span class="p">:</span>
<a name="cl-292"></a>          <span class="k">break</span>
<a name="cl-293"></a>        <span class="n">owner</span><span class="o">=</span><span class="n">parent</span>
<a name="cl-294"></a>      <span class="k">try</span><span class="p">:</span>
<a name="cl-295"></a>        <span class="n">node</span><span class="o">.</span><span class="n">_owner</span><span class="o">=</span><span class="n">owner</span>
<a name="cl-296"></a>      <span class="k">except</span><span class="p">:</span>
<a name="cl-297"></a>        <span class="k">pass</span>
<a name="cl-298"></a>      <span class="k">return</span> <span class="n">owner</span>
<a name="cl-299"></a>    
<a name="cl-300"></a>    <span class="k">def</span> <span class="nf">pairwise</span><span class="p">(</span><span class="n">iterable</span><span class="p">):</span>
<a name="cl-301"></a>      <span class="n">itnext</span> <span class="o">=</span> <span class="nb">iter</span><span class="p">(</span><span class="n">iterable</span><span class="p">)</span><span class="o">.</span><span class="n">next</span>
<a name="cl-302"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-303"></a>          <span class="k">yield</span> <span class="n">itnext</span><span class="p">(),</span> <span class="n">itnext</span><span class="p">()</span>
<a name="cl-304"></a>    
<a name="cl-305"></a>    <span class="k">def</span> <span class="nf">_attributes</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-306"></a>      <span class="k">if</span> <span class="n">_nodeType</span><span class="p">(</span><span class="n">node</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span><span class="p">:</span>
<a name="cl-307"></a>        <span class="c">#return node._getAttrMap()</span>
<a name="cl-308"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;attrMap&#39;</span><span class="p">):</span>
<a name="cl-309"></a>          <span class="n">node</span><span class="o">.</span><span class="n">attrMap</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">pairwise</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">attrs</span><span class="p">))</span>
<a name="cl-310"></a>        <span class="k">return</span> <span class="n">node</span><span class="o">.</span><span class="n">attrMap</span>
<a name="cl-311"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-312"></a>        <span class="k">return</span> <span class="bp">None</span>
<a name="cl-313"></a>    
<a name="cl-314"></a>    <span class="k">def</span> <span class="nf">_contains</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-315"></a>      <span class="k">if</span> <span class="n">_nodeType</span><span class="p">(</span><span class="n">node</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-316"></a>      <span class="k">if</span> <span class="n">_nodeType</span><span class="p">(</span><span class="n">cnode</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">cnode</span><span class="o">=</span><span class="n">cnode</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-317"></a>      <span class="k">return</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">cnode</span><span class="o">.</span><span class="n">findParents</span><span class="p">()</span>
<a name="cl-318"></a>    
<a name="cl-319"></a>    <span class="k">def</span> <span class="nf">_preceding</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-320"></a>      <span class="k">if</span> <span class="n">_nodeType</span><span class="p">(</span><span class="n">node</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-321"></a>      <span class="k">if</span> <span class="n">_nodeType</span><span class="p">(</span><span class="n">cnode</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">cnode</span><span class="o">=</span><span class="n">cnode</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-322"></a>      <span class="c">#return cnode in node.findAllPrevious()</span>
<a name="cl-323"></a>      <span class="k">return</span> <span class="n">cnode</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">findPreviousSiblings</span><span class="p">()</span>
<a name="cl-324"></a>    
<a name="cl-325"></a>    <span class="k">def</span> <span class="nf">_following</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-326"></a>      <span class="k">if</span> <span class="n">_nodeType</span><span class="p">(</span><span class="n">node</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-327"></a>      <span class="k">if</span> <span class="n">_nodeType</span><span class="p">(</span><span class="n">cnode</span><span class="p">)</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">cnode</span><span class="o">=</span><span class="n">cnode</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-328"></a>      <span class="c">#return cnode in node.findAllNext()</span>
<a name="cl-329"></a>      <span class="k">return</span> <span class="n">cnode</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">findNextSiblings</span><span class="p">()</span>
<a name="cl-330"></a>    
<a name="cl-331"></a>    <span class="k">def</span> <span class="nf">d_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-332"></a>      <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">,</span><span class="n">name</span>
<a name="cl-333"></a>    
<a name="cl-334"></a>    <span class="c">#{ // ExtPageElement</span>
<a name="cl-335"></a>    <span class="k">class</span> <span class="nc">ExtPageElement</span><span class="p">:</span>
<a name="cl-336"></a>      <span class="k">def</span> <span class="nf">__getattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-337"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeType&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_nodeType</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-338"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeName&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_nodeName</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-339"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeValue&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_nodeValue</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-340"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;parentNode&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_parentNode</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-341"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_ownerDocument</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-342"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;attributes&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_attributes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-343"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;get&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get</span>
<a name="cl-344"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;contains&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">contains</span>
<a name="cl-345"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;preceding&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">preceding</span>
<a name="cl-346"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;following&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">following</span>
<a name="cl-347"></a>        <span class="n">d_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">)</span>
<a name="cl-348"></a>      
<a name="cl-349"></a>      <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">key</span><span class="p">,</span><span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-350"></a>        <span class="k">return</span> <span class="n">_nodeAttrValue</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">key</span><span class="p">)</span>
<a name="cl-351"></a>      
<a name="cl-352"></a>      <span class="k">def</span> <span class="nf">contains</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-353"></a>        <span class="k">return</span> <span class="n">_contains</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">)</span>
<a name="cl-354"></a>      
<a name="cl-355"></a>      <span class="k">def</span> <span class="nf">preceding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-356"></a>        <span class="k">return</span> <span class="n">_preceding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">)</span>
<a name="cl-357"></a>      
<a name="cl-358"></a>      <span class="k">def</span> <span class="nf">following</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-359"></a>        <span class="k">return</span> <span class="n">_following</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">)</span>
<a name="cl-360"></a>    
<a name="cl-361"></a>    <span class="n">PageElement</span><span class="o">.</span><span class="n">__bases__</span><span class="o">+=</span><span class="p">(</span><span class="n">ExtPageElement</span><span class="p">,)</span>
<a name="cl-362"></a>    <span class="n">BeautifulSoup</span><span class="o">.</span><span class="n">__bases__</span><span class="o">+=</span><span class="p">(</span><span class="n">ExtPageElement</span><span class="p">,)</span>
<a name="cl-363"></a>    <span class="n">NavigableString</span><span class="o">.</span><span class="n">__bases__</span><span class="o">+=</span><span class="p">(</span><span class="n">ExtPageElement</span><span class="p">,)</span>
<a name="cl-364"></a>    <span class="n">CData</span><span class="o">.</span><span class="n">__bases__</span><span class="o">+=</span><span class="p">(</span><span class="n">ExtPageElement</span><span class="p">,)</span>
<a name="cl-365"></a>    <span class="n">ProcessingInstruction</span><span class="o">.</span><span class="n">__bases__</span><span class="o">+=</span><span class="p">(</span><span class="n">ExtPageElement</span><span class="p">,)</span>
<a name="cl-366"></a>    <span class="n">Comment</span><span class="o">.</span><span class="n">__bases__</span><span class="o">+=</span><span class="p">(</span><span class="n">ExtPageElement</span><span class="p">,)</span>
<a name="cl-367"></a>    <span class="n">Declaration</span><span class="o">.</span><span class="n">__bases__</span><span class="o">+=</span><span class="p">(</span><span class="n">ExtPageElement</span><span class="p">,)</span>
<a name="cl-368"></a>    <span class="n">Tag</span><span class="o">.</span><span class="n">__bases__</span><span class="o">+=</span><span class="p">(</span><span class="n">ExtPageElement</span><span class="p">,)</span>
<a name="cl-369"></a>    
<a name="cl-370"></a>    <span class="c">#} // ExtPageElement</span>
<a name="cl-371"></a>    
<a name="cl-372"></a>    <span class="c">#{ // _extBeautifulSoup</span>
<a name="cl-373"></a>    <span class="k">def</span> <span class="nf">_extBeautifulSoup</span><span class="p">():</span>
<a name="cl-374"></a>      <span class="n">o_getattr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">BeautifulSoup</span><span class="p">,</span><span class="s">&#39;__getattr__&#39;</span><span class="p">,</span><span class="n">d_getattr</span><span class="p">)</span>
<a name="cl-375"></a>      <span class="k">def</span> <span class="nf">e_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-376"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeType&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span>
<a name="cl-377"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeName&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;#document&#39;</span>
<a name="cl-378"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeValue&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-379"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;parentNode&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-380"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-381"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;attributes&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-382"></a>        <span class="k">return</span> <span class="n">o_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">)</span>
<a name="cl-383"></a>      <span class="n">BeautifulSoup</span><span class="o">.</span><span class="n">__getattr__</span><span class="o">=</span><span class="n">e_getattr</span>
<a name="cl-384"></a>    <span class="n">_extBeautifulSoup</span><span class="p">()</span>
<a name="cl-385"></a>    <span class="c">#} // _extBeautifulSoup</span>
<a name="cl-386"></a>    
<a name="cl-387"></a>    <span class="c">#{ // _extNavigableString</span>
<a name="cl-388"></a>    <span class="k">def</span> <span class="nf">_extNavigableString</span><span class="p">():</span>
<a name="cl-389"></a>      <span class="n">o_getattr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">NavigableString</span><span class="p">,</span><span class="s">&#39;__getattr__&#39;</span><span class="p">,</span><span class="n">d_getattr</span><span class="p">)</span>
<a name="cl-390"></a>      <span class="k">def</span> <span class="nf">e_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-391"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeType&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">TEXT_NODE</span>
<a name="cl-392"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeName&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;#text&#39;</span>
<a name="cl-393"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeValue&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-394"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;parentNode&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-395"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_ownerDocument</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-396"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;attributes&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-397"></a>        <span class="k">return</span> <span class="n">o_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">)</span>
<a name="cl-398"></a>      <span class="n">NavigableString</span><span class="o">.</span><span class="n">__getattr__</span><span class="o">=</span><span class="n">e_getattr</span>
<a name="cl-399"></a>    <span class="n">_extNavigableString</span><span class="p">()</span>
<a name="cl-400"></a>    <span class="c">#} // _extNavigableString</span>
<a name="cl-401"></a>    
<a name="cl-402"></a>    <span class="c">#{ // _extCData</span>
<a name="cl-403"></a>    <span class="k">def</span> <span class="nf">_extCData</span><span class="p">():</span>
<a name="cl-404"></a>      <span class="n">o_getattr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">CData</span><span class="p">,</span><span class="s">&#39;__getattr__&#39;</span><span class="p">,</span><span class="n">d_getattr</span><span class="p">)</span>
<a name="cl-405"></a>      <span class="k">def</span> <span class="nf">e_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-406"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeType&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">CDATA_SECTION_NODE</span>
<a name="cl-407"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeName&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;#cdata-section&#39;</span>
<a name="cl-408"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeValue&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-409"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;parentNode&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-410"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_ownerDocument</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-411"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;attributes&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-412"></a>        <span class="k">return</span> <span class="n">o_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">)</span>
<a name="cl-413"></a>      <span class="n">CData</span><span class="o">.</span><span class="n">__getattr__</span><span class="o">=</span><span class="n">e_getattr</span>
<a name="cl-414"></a>    <span class="n">_extCData</span><span class="p">()</span>
<a name="cl-415"></a>    <span class="c">#} // _extCData</span>
<a name="cl-416"></a>    
<a name="cl-417"></a>    <span class="c">#{ // _extProcessingInstruction</span>
<a name="cl-418"></a>    <span class="k">def</span> <span class="nf">_extProcessingInstruction</span><span class="p">():</span>
<a name="cl-419"></a>      <span class="n">o_getattr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">ProcessingInstruction</span><span class="p">,</span><span class="s">&#39;__getattr__&#39;</span><span class="p">,</span><span class="n">d_getattr</span><span class="p">)</span>
<a name="cl-420"></a>      <span class="k">def</span> <span class="nf">e_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-421"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeType&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">PROCESSING_INSTRUCTION_NODE</span>
<a name="cl-422"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeName&#39;</span><span class="p">:</span>
<a name="cl-423"></a>          <span class="n">mrslt</span><span class="o">=</span><span class="n">re_processing_instruction</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">))</span>
<a name="cl-424"></a>          <span class="k">return</span> <span class="n">mrslt</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="k">if</span> <span class="n">mrslt</span> <span class="k">else</span> <span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-425"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeValue&#39;</span><span class="p">:</span>
<a name="cl-426"></a>          <span class="n">mrslt</span><span class="o">=</span><span class="n">re_processing_instruction</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">))</span>
<a name="cl-427"></a>          <span class="k">return</span> <span class="n">mrslt</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span> <span class="k">if</span> <span class="n">mrslt</span> <span class="k">else</span> <span class="bp">None</span>
<a name="cl-428"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;parentNode&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-429"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_ownerDocument</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-430"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;attributes&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-431"></a>        <span class="k">return</span> <span class="n">o_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">)</span>
<a name="cl-432"></a>      <span class="n">ProcessingInstruction</span><span class="o">.</span><span class="n">__getattr__</span><span class="o">=</span><span class="n">e_getattr</span>
<a name="cl-433"></a>    <span class="n">_extProcessingInstruction</span><span class="p">()</span>
<a name="cl-434"></a>    <span class="c">#} // _extProcessingInstruction</span>
<a name="cl-435"></a>    
<a name="cl-436"></a>    <span class="c">#{ // _extComment</span>
<a name="cl-437"></a>    <span class="k">def</span> <span class="nf">_extComment</span><span class="p">():</span>
<a name="cl-438"></a>      <span class="n">o_getattr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">Comment</span><span class="p">,</span><span class="s">&#39;__getattr__&#39;</span><span class="p">,</span><span class="n">d_getattr</span><span class="p">)</span>
<a name="cl-439"></a>      <span class="k">def</span> <span class="nf">e_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-440"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeType&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">COMMENT_NODE</span>
<a name="cl-441"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeName&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;#comment&#39;</span>
<a name="cl-442"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeValue&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-443"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;parentNode&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-444"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_ownerDocument</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-445"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;attributes&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-446"></a>        <span class="k">return</span> <span class="n">o_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">)</span>
<a name="cl-447"></a>      <span class="n">Comment</span><span class="o">.</span><span class="n">__getattr__</span><span class="o">=</span><span class="n">e_getattr</span>
<a name="cl-448"></a>    <span class="n">_extComment</span><span class="p">()</span>
<a name="cl-449"></a>    <span class="c">#} // _extComment</span>
<a name="cl-450"></a>    
<a name="cl-451"></a>    <span class="c">#{ // _extDeclaration</span>
<a name="cl-452"></a>    <span class="k">def</span> <span class="nf">_extDeclaration</span><span class="p">():</span>
<a name="cl-453"></a>      <span class="n">o_getattr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">Declaration</span><span class="p">,</span><span class="s">&#39;__getattr__&#39;</span><span class="p">,</span><span class="n">d_getattr</span><span class="p">)</span>
<a name="cl-454"></a>      <span class="k">def</span> <span class="nf">e_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-455"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeType&#39;</span><span class="p">:</span>
<a name="cl-456"></a>          <span class="nb">str</span><span class="o">=</span><span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-457"></a>          <span class="k">if</span> <span class="n">re_type_document_type</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
<a name="cl-458"></a>            <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_TYPE_NODE</span>
<a name="cl-459"></a>          <span class="k">elif</span> <span class="n">re_type_entity</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
<a name="cl-460"></a>            <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ENTITY_NODE</span>
<a name="cl-461"></a>          <span class="k">elif</span> <span class="n">re_type_notation</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
<a name="cl-462"></a>            <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">NOTATION_NODE</span>
<a name="cl-463"></a>          <span class="k">else</span><span class="p">:</span>
<a name="cl-464"></a>            <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ANY_NODE</span>
<a name="cl-465"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeName&#39;</span><span class="p">:</span>
<a name="cl-466"></a>          <span class="n">mrslt</span><span class="o">=</span><span class="n">re_declaration_name</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">))</span>
<a name="cl-467"></a>          <span class="k">return</span> <span class="n">mrslt</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span> <span class="k">if</span> <span class="n">mrslt</span> <span class="k">else</span> <span class="n">NavigableString</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-468"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeValue&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-469"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;parentNode&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-470"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_ownerDocument</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-471"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;attributes&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-472"></a>        <span class="k">return</span> <span class="n">o_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">)</span>
<a name="cl-473"></a>      <span class="n">Declaration</span><span class="o">.</span><span class="n">__getattr__</span><span class="o">=</span><span class="n">e_getattr</span>
<a name="cl-474"></a>    <span class="n">_extDeclaration</span><span class="p">()</span>
<a name="cl-475"></a>    <span class="c">#} // _extDeclaration</span>
<a name="cl-476"></a>    
<a name="cl-477"></a>    <span class="c">#{ // _extTag</span>
<a name="cl-478"></a>    <span class="k">def</span> <span class="nf">_extTag</span><span class="p">():</span>
<a name="cl-479"></a>      <span class="n">o_getattr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">Tag</span><span class="p">,</span><span class="s">&#39;__getattr__&#39;</span><span class="p">,</span><span class="n">d_getattr</span><span class="p">)</span>
<a name="cl-480"></a>      <span class="k">def</span> <span class="nf">e_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-481"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeType&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span>
<a name="cl-482"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeName&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<a name="cl-483"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;nodeValue&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
<a name="cl-484"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;parentNode&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-485"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">_ownerDocument</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-486"></a>        <span class="k">if</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;attributes&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_getAttrMap</span><span class="p">()</span>
<a name="cl-487"></a>        <span class="k">return</span> <span class="n">o_getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">)</span>
<a name="cl-488"></a>      <span class="n">Tag</span><span class="o">.</span><span class="n">__getattr__</span><span class="o">=</span><span class="n">e_getattr</span>
<a name="cl-489"></a>    <span class="n">_extTag</span><span class="p">()</span>
<a name="cl-490"></a>    <span class="c">#} // _extTag</span>
<a name="cl-491"></a>    
<a name="cl-492"></a>    <span class="k">def</span> <span class="nf">_it_deepNodes</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-493"></a>      <span class="n">child_next</span><span class="o">=</span><span class="nb">iter</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;contents&#39;</span><span class="p">,[]))</span><span class="o">.</span><span class="n">next</span>
<a name="cl-494"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-495"></a>        <span class="n">child</span><span class="o">=</span><span class="n">child_next</span><span class="p">()</span>
<a name="cl-496"></a>        <span class="k">yield</span> <span class="n">child</span>
<a name="cl-497"></a>        <span class="k">for</span> <span class="n">gchild</span> <span class="ow">in</span> <span class="n">_it_deepNodes</span><span class="p">(</span><span class="n">child</span><span class="p">):</span>
<a name="cl-498"></a>          <span class="k">yield</span> <span class="n">gchild</span>
<a name="cl-499"></a>    
<a name="cl-500"></a>    <span class="k">return</span> <span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-501"></a>      <span class="s">&#39;nodeType&#39;</span>     <span class="p">:</span><span class="n">_nodeType</span>
<a name="cl-502"></a>    <span class="p">,</span> <span class="s">&#39;nodeName&#39;</span>     <span class="p">:</span><span class="n">_nodeName</span>
<a name="cl-503"></a>    <span class="p">,</span> <span class="s">&#39;nodeValue&#39;</span>    <span class="p">:</span><span class="n">_nodeValue</span>
<a name="cl-504"></a>    <span class="p">,</span> <span class="s">&#39;nodeAttrValue&#39;</span><span class="p">:</span><span class="n">_nodeAttrValue</span>
<a name="cl-505"></a>    <span class="p">,</span> <span class="s">&#39;parentNode&#39;</span>   <span class="p">:</span><span class="n">_parentNode</span>
<a name="cl-506"></a>    <span class="p">,</span> <span class="s">&#39;ownerDocument&#39;</span><span class="p">:</span><span class="n">_ownerDocument</span>
<a name="cl-507"></a>    <span class="p">,</span> <span class="s">&#39;attributes&#39;</span>   <span class="p">:</span><span class="n">_attributes</span>
<a name="cl-508"></a>    <span class="p">,</span> <span class="s">&#39;contains&#39;</span>     <span class="p">:</span><span class="n">_contains</span>
<a name="cl-509"></a>    <span class="p">,</span> <span class="s">&#39;preceding&#39;</span>    <span class="p">:</span><span class="n">_preceding</span>
<a name="cl-510"></a>    <span class="p">,</span> <span class="s">&#39;following&#39;</span>    <span class="p">:</span><span class="n">_following</span>
<a name="cl-511"></a>    <span class="p">,</span> <span class="s">&#39;it_deepNodes&#39;</span> <span class="p">:</span><span class="n">_it_deepNodes</span>
<a name="cl-512"></a>    <span class="p">})</span>
<a name="cl-513"></a>    <span class="k">return</span>
<a name="cl-514"></a>    
<a name="cl-515"></a>  <span class="k">def</span> <span class="nf">makeNU</span><span class="p">():</span>
<a name="cl-516"></a>    <span class="k">def</span> <span class="nf">_to</span><span class="p">(</span><span class="n">valueType</span><span class="p">,</span><span class="n">node</span><span class="p">):</span>
<a name="cl-517"></a>      <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">node</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;string&#39;</span><span class="p">:</span>
<a name="cl-518"></a>        <span class="n">result</span><span class="o">=</span><span class="n">node</span>
<a name="cl-519"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-520"></a>        <span class="n">nodeType</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">nodeType</span>
<a name="cl-521"></a>        <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-522"></a>          <span class="n">result</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">nodeValue</span>
<a name="cl-523"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-524"></a>          <span class="n">strings</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-525"></a>          <span class="k">for</span> <span class="n">_node</span> <span class="ow">in</span> <span class="n">NodeUtilBS</span><span class="o">.</span><span class="n">it_deepNodes</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-526"></a>            <span class="k">if</span> <span class="n">_node</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">TEXT_NODE</span><span class="p">:</span>
<a name="cl-527"></a>              <span class="n">strings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">unicode</span><span class="p">(</span><span class="n">_node</span><span class="p">))</span>
<a name="cl-528"></a>          <span class="n">result</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">strings</span><span class="p">)</span>
<a name="cl-529"></a>      
<a name="cl-530"></a>      <span class="k">if</span> <span class="n">valueType</span><span class="o">==</span><span class="s">&#39;number&#39;</span><span class="p">:</span>
<a name="cl-531"></a>        <span class="k">return</span> <span class="n">toNumber</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
<a name="cl-532"></a>      <span class="k">elif</span> <span class="n">valueType</span><span class="o">==</span><span class="s">&#39;boolean&#39;</span><span class="p">:</span>
<a name="cl-533"></a>        <span class="k">return</span> <span class="n">toBoolean</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
<a name="cl-534"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-535"></a>        <span class="k">return</span> <span class="n">result</span>
<a name="cl-536"></a>    
<a name="cl-537"></a>    <span class="k">def</span> <span class="nf">_attrMatch</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">):</span>
<a name="cl-538"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">attrName</span> <span class="ow">or</span> \
<a name="cl-539"></a>         <span class="ow">not</span> <span class="n">attrValue</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">attrName</span><span class="p">)</span> <span class="ow">or</span> \
<a name="cl-540"></a>         <span class="p">(</span><span class="n">attrValue</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">attrName</span><span class="p">)</span><span class="o">==</span><span class="n">attrValue</span><span class="p">):</span>
<a name="cl-541"></a>        <span class="k">return</span> <span class="bp">True</span>
<a name="cl-542"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-543"></a>        <span class="k">return</span> <span class="bp">False</span>
<a name="cl-544"></a>    
<a name="cl-545"></a>    <span class="k">def</span> <span class="nf">_getDescendantNodes</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-546"></a>      <span class="k">if</span> <span class="n">prevNodeset</span><span class="p">:</span>
<a name="cl-547"></a>        <span class="n">prevNodeset</span><span class="o">.</span><span class="n">delDescendant</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-548"></a>      
<a name="cl-549"></a>      <span class="k">if</span> <span class="n">USE_NODE_CACHE</span><span class="p">:</span>
<a name="cl-550"></a>        <span class="n">_cachemap</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;_cachemap&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-551"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">_cachemap</span><span class="p">:</span>
<a name="cl-552"></a>          <span class="n">_cachemap</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">_cachemap</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span><span class="s">&#39;attrib&#39;</span><span class="p">:</span><span class="n">ExtDict</span><span class="p">({}),</span><span class="s">&#39;all&#39;</span><span class="p">:</span><span class="bp">None</span><span class="p">,</span><span class="s">&#39;tag&#39;</span><span class="p">:</span><span class="n">ExtDict</span><span class="p">({})})</span>
<a name="cl-553"></a>        
<a name="cl-554"></a>        <span class="k">if</span> <span class="n">attrValue</span> <span class="ow">and</span> <span class="n">attrName</span><span class="p">:</span>
<a name="cl-555"></a>          <span class="n">_cm</span><span class="o">=</span><span class="n">_cachemap</span><span class="o">.</span><span class="n">attrib</span>
<a name="cl-556"></a>          <span class="n">_anmap</span><span class="o">=</span><span class="n">_cm</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">attrName</span><span class="p">)</span>
<a name="cl-557"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">_anmap</span><span class="p">:</span>
<a name="cl-558"></a>            <span class="n">_anmap</span><span class="o">=</span><span class="n">_cm</span><span class="p">[</span><span class="n">attrName</span><span class="p">]</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({})</span>
<a name="cl-559"></a>          <span class="n">nodes</span><span class="o">=</span><span class="n">_anmap</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">attrValue</span><span class="p">)</span>
<a name="cl-560"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-561"></a>            <span class="n">nodes</span><span class="o">=</span><span class="n">_anmap</span><span class="p">[</span><span class="n">attrValue</span><span class="p">]</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-562"></a>            <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;findAll&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-563"></a>              <span class="n">nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">findAll</span><span class="p">(</span><span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="n">attrName</span><span class="p">:</span><span class="n">attrValue</span><span class="p">}))</span>
<a name="cl-564"></a>          <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-565"></a>            <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">elm</span><span class="p">):</span>
<a name="cl-566"></a>              <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-567"></a>        
<a name="cl-568"></a>        <span class="k">elif</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="s">&#39;notOnlyElement&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-569"></a>          <span class="n">nodes</span><span class="o">=</span><span class="n">_cachemap</span><span class="o">.</span><span class="n">all</span>
<a name="cl-570"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-571"></a>            <span class="n">nodes</span><span class="o">=</span><span class="n">_cachemap</span><span class="o">.</span><span class="n">all</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-572"></a>            <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">NodeUtilBS</span><span class="o">.</span><span class="n">it_deepNodes</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-573"></a>              <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-574"></a>          
<a name="cl-575"></a>          <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-576"></a>            <span class="k">if</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">attrMatch</span><span class="p">(</span><span class="n">elm</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">)</span> <span class="ow">and</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">elm</span><span class="p">):</span>
<a name="cl-577"></a>              <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-578"></a>        
<a name="cl-579"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-580"></a>          <span class="n">nodeType</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">nodeType</span>
<a name="cl-581"></a>          <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span> <span class="ow">or</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span><span class="p">:</span>
<a name="cl-582"></a>            <span class="n">_cm</span><span class="o">=</span><span class="n">_cachemap</span><span class="o">.</span><span class="n">tag</span>
<a name="cl-583"></a>            <span class="n">name</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="s">&#39;name&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-584"></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;*&#39;</span><span class="p">:</span>
<a name="cl-585"></a>              <span class="n">nodes</span><span class="o">=</span><span class="n">_cm</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;*&#39;</span><span class="p">)</span>
<a name="cl-586"></a>              <span class="k">if</span> <span class="ow">not</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-587"></a>                <span class="n">nodes</span><span class="o">=</span><span class="n">_cm</span><span class="p">[</span><span class="s">&#39;*&#39;</span><span class="p">]</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">findAll</span><span class="p">()</span>
<a name="cl-588"></a>            <span class="k">else</span><span class="p">:</span>
<a name="cl-589"></a>              <span class="n">nodes</span><span class="o">=</span><span class="n">_cm</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
<a name="cl-590"></a>              <span class="k">if</span> <span class="ow">not</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-591"></a>                <span class="n">nodes</span><span class="o">=</span><span class="n">_cm</span><span class="p">[</span><span class="n">name</span><span class="p">]</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">findAll</span><span class="p">([</span><span class="n">name</span><span class="p">])</span>
<a name="cl-592"></a>            <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-593"></a>              <span class="k">if</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">attrMatch</span><span class="p">(</span><span class="n">elm</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">):</span>
<a name="cl-594"></a>                <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-595"></a>      
<a name="cl-596"></a>      <span class="k">else</span><span class="p">:</span> <span class="c"># USE_NODE_CACHE is False</span>
<a name="cl-597"></a>        <span class="k">if</span> <span class="n">attrValue</span> <span class="ow">and</span> <span class="n">attrName</span><span class="p">:</span>
<a name="cl-598"></a>          <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;findAll&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-599"></a>            <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">findAll</span><span class="p">(</span><span class="n">attrs</span><span class="o">=</span><span class="p">{</span><span class="n">attrName</span><span class="p">:</span><span class="n">attrValue</span><span class="p">}):</span>
<a name="cl-600"></a>              <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">elm</span><span class="p">):</span>
<a name="cl-601"></a>                <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-602"></a>          
<a name="cl-603"></a>        <span class="k">elif</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="s">&#39;notOnlyElement&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-604"></a>          <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">NodeUtilBS</span><span class="o">.</span><span class="n">it_deepNodes</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-605"></a>            <span class="k">if</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">attrMatch</span><span class="p">(</span><span class="n">elm</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">)</span> <span class="ow">and</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">elm</span><span class="p">):</span>
<a name="cl-606"></a>              <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-607"></a>          
<a name="cl-608"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-609"></a>          <span class="n">nodeType</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">nodeType</span>
<a name="cl-610"></a>          <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span> <span class="ow">or</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span><span class="p">:</span>
<a name="cl-611"></a>            <span class="n">name</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="s">&#39;name&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-612"></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">name</span><span class="o">==</span><span class="s">&#39;*&#39;</span><span class="p">:</span>
<a name="cl-613"></a>              <span class="n">nodes</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">findAll</span><span class="p">()</span>
<a name="cl-614"></a>            <span class="k">else</span><span class="p">:</span>
<a name="cl-615"></a>              <span class="n">nodes</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">findAll</span><span class="p">([</span><span class="n">name</span><span class="p">])</span>
<a name="cl-616"></a>            <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-617"></a>              <span class="k">if</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">attrMatch</span><span class="p">(</span><span class="n">elm</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">):</span>
<a name="cl-618"></a>                <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-619"></a>      
<a name="cl-620"></a>      <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-621"></a>    
<a name="cl-622"></a>    <span class="k">def</span> <span class="nf">_getChildNodes</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-623"></a>      <span class="n">contents</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;contents&#39;</span><span class="p">,[])</span>
<a name="cl-624"></a>      <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">contents</span><span class="p">:</span>
<a name="cl-625"></a>        <span class="k">if</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">attrMatch</span><span class="p">(</span><span class="n">elm</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">)</span> <span class="ow">and</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">elm</span><span class="p">):</span>
<a name="cl-626"></a>           <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-627"></a>      
<a name="cl-628"></a>      <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-629"></a>    
<a name="cl-630"></a>    <span class="k">return</span> <span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-631"></a>      <span class="s">&#39;to&#39;</span>                <span class="p">:</span><span class="n">_to</span>
<a name="cl-632"></a>    <span class="p">,</span> <span class="s">&#39;attrMatch&#39;</span>         <span class="p">:</span><span class="n">_attrMatch</span>
<a name="cl-633"></a>    <span class="p">,</span> <span class="s">&#39;getDescendantNodes&#39;</span><span class="p">:</span><span class="n">_getDescendantNodes</span>
<a name="cl-634"></a>    <span class="p">,</span> <span class="s">&#39;getChildNodes&#39;</span>     <span class="p">:</span><span class="n">_getChildNodes</span>
<a name="cl-635"></a>    <span class="p">})</span>
<a name="cl-636"></a>  
<a name="cl-637"></a>  <span class="k">return</span> <span class="p">(</span><span class="n">makeNU_BS</span><span class="p">(),</span><span class="n">makeNU</span><span class="p">())</span>
<a name="cl-638"></a>  
<a name="cl-639"></a><span class="p">(</span><span class="n">NodeUtilBS</span><span class="p">,</span><span class="n">NodeUtil</span><span class="p">)</span><span class="o">=</span><span class="n">makeNodeUtils</span><span class="p">()</span>
<a name="cl-640"></a>
<a name="cl-641"></a><span class="c">#} // end of NodeUtil</span>
<a name="cl-642"></a>
<a name="cl-643"></a>
<a name="cl-644"></a>
<a name="cl-645"></a><span class="c">#***** Application Classes</span>
<a name="cl-646"></a><span class="c">#{ // Lexer</span>
<a name="cl-647"></a><span class="k">class</span> <span class="nc">Lexer</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-648"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">source</span><span class="p">):</span>
<a name="cl-649"></a>    <span class="n">tokens</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tokens</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-650"></a>    <span class="k">def</span> <span class="nf">anlz_token</span><span class="p">(</span><span class="n">mrslt</span><span class="p">):</span>
<a name="cl-651"></a>      <span class="n">token</span><span class="o">=</span><span class="n">mrslt</span><span class="o">.</span><span class="n">group</span><span class="p">()</span>
<a name="cl-652"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">re_strip</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">token</span><span class="p">):</span>
<a name="cl-653"></a>        <span class="n">tokens</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">token</span><span class="p">)</span>
<a name="cl-654"></a>      <span class="k">return</span> <span class="n">token</span>
<a name="cl-655"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">re_token</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">anlz_token</span><span class="p">,</span><span class="n">source</span><span class="p">,</span><span class="n">count</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
<a name="cl-656"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">=</span><span class="mi">0</span>
<a name="cl-657"></a>    
<a name="cl-658"></a>  <span class="k">def</span> <span class="nf">peek</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
<a name="cl-659"></a>    <span class="n">token</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tokens</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">+</span><span class="n">i</span><span class="p">]</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">+</span><span class="n">i</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tokens</span><span class="p">)</span> <span class="k">else</span> <span class="bp">None</span>
<a name="cl-660"></a>    <span class="k">return</span> <span class="n">token</span>
<a name="cl-661"></a>  
<a name="cl-662"></a>  <span class="k">def</span> <span class="nf">next</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-663"></a>    <span class="n">token</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tokens</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">]</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tokens</span><span class="p">)</span> <span class="k">else</span> <span class="bp">None</span>
<a name="cl-664"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-665"></a>    <span class="k">return</span> <span class="n">token</span>
<a name="cl-666"></a>  
<a name="cl-667"></a>  <span class="k">def</span> <span class="nf">back</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-668"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">-=</span><span class="mi">1</span>
<a name="cl-669"></a>    <span class="n">token</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">tokens</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">]</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tokens</span><span class="p">)</span> <span class="k">else</span> <span class="bp">None</span>
<a name="cl-670"></a>  
<a name="cl-671"></a>  <span class="k">def</span> <span class="nf">empty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-672"></a>    <span class="k">return</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tokens</span><span class="p">)</span><span class="o">&lt;=</span><span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
<a name="cl-673"></a>  
<a name="cl-674"></a>  <span class="n">re_token</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;\$?(?:(?![0-9-])[\w-]+:)?(?![0-9-])[\w-]+|\/\/|\.\.|::|\d+(?:\.\d*)?|\.\d+|&quot;[^&quot;]*&quot;|</span><span class="se">\&#39;</span><span class="s">[^</span><span class="se">\&#39;</span><span class="s">]*</span><span class="se">\&#39;</span><span class="s">|[!&lt;&gt;]=|(?![0-9-])[\w-]+:\*|\s+|.&#39;</span><span class="p">)</span>
<a name="cl-675"></a>  <span class="n">re_strip</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^\s&#39;</span><span class="p">)</span>
<a name="cl-676"></a>  
<a name="cl-677"></a><span class="c">#} // end of Lexer</span>
<a name="cl-678"></a>
<a name="cl-679"></a>
<a name="cl-680"></a><span class="c">#{ // Ctx</span>
<a name="cl-681"></a><span class="k">class</span> <span class="nc">Ctx</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-682"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">position</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">last</span><span class="o">=</span><span class="mi">1</span><span class="p">):</span>
<a name="cl-683"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="o">=</span><span class="n">node</span>
<a name="cl-684"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">position</span><span class="o">=</span><span class="n">position</span>
<a name="cl-685"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">last</span><span class="o">=</span><span class="n">last</span>
<a name="cl-686"></a>
<a name="cl-687"></a><span class="c">#} // end of Ctx</span>
<a name="cl-688"></a>
<a name="cl-689"></a>
<a name="cl-690"></a><span class="c">#{ // AttributeWrapper</span>
<a name="cl-691"></a><span class="k">class</span> <span class="nc">AttributeWrapper</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-692"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">,</span><span class="n">value</span><span class="p">,</span><span class="n">parent</span><span class="p">):</span>
<a name="cl-693"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">nodeType</span><span class="o">=</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span>
<a name="cl-694"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">nodeName</span><span class="o">=</span><span class="n">name</span>
<a name="cl-695"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">nodeValue</span><span class="o">=</span><span class="n">value</span>
<a name="cl-696"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">parentNode</span><span class="o">=</span><span class="n">parent</span>
<a name="cl-697"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">ownerElement</span><span class="o">=</span><span class="n">parent</span>
<a name="cl-698"></a>  
<a name="cl-699"></a>  <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">key</span><span class="p">,</span><span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-700"></a>    <span class="k">return</span> <span class="bp">None</span>
<a name="cl-701"></a>  
<a name="cl-702"></a>  <span class="k">def</span> <span class="nf">contains</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-703"></a>    <span class="k">return</span> <span class="n">NodeUtilBS</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">)</span>
<a name="cl-704"></a>  
<a name="cl-705"></a>  <span class="k">def</span> <span class="nf">preceding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-706"></a>    <span class="k">return</span> <span class="n">NodeUtilBS</span><span class="o">.</span><span class="n">preceding</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">)</span>
<a name="cl-707"></a>  
<a name="cl-708"></a>  <span class="k">def</span> <span class="nf">following</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">):</span>
<a name="cl-709"></a>    <span class="k">return</span> <span class="n">NodeUtilBS</span><span class="o">.</span><span class="n">following</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">cnode</span><span class="p">)</span>
<a name="cl-710"></a>  
<a name="cl-711"></a>  <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">):</span>
<a name="cl-712"></a>    <span class="k">if</span> <span class="n">encoding</span><span class="p">:</span>
<a name="cl-713"></a>      <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodeValue</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">)</span>
<a name="cl-714"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-715"></a>      <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodeValue</span>
<a name="cl-716"></a>  
<a name="cl-717"></a>  <span class="k">def</span> <span class="nf">__unicode__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-718"></a>    <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">)</span>
<a name="cl-719"></a>  
<a name="cl-720"></a>  <span class="nd">@classmethod</span>
<a name="cl-721"></a>  <span class="k">def</span> <span class="nf">getAttributeWrapper</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">name</span><span class="p">,</span><span class="n">value</span><span class="p">,</span><span class="n">parent</span><span class="p">):</span>
<a name="cl-722"></a>    <span class="n">_mapattr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">parent</span><span class="p">,</span><span class="s">&#39;_mapattr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-723"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">_mapattr</span><span class="p">:</span>
<a name="cl-724"></a>      <span class="n">_mapattr</span><span class="o">=</span><span class="n">parent</span><span class="o">.</span><span class="n">_mapattr</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({})</span>
<a name="cl-725"></a>    <span class="k">if</span> <span class="n">_mapattr</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">):</span>
<a name="cl-726"></a>      <span class="k">return</span> <span class="n">_mapattr</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
<a name="cl-727"></a>    <span class="n">_mapattr</span><span class="p">[</span><span class="n">name</span><span class="p">]</span><span class="o">=</span><span class="n">cls</span><span class="p">(</span><span class="n">name</span><span class="p">,</span><span class="n">value</span><span class="p">,</span><span class="n">parent</span><span class="p">)</span>
<a name="cl-728"></a>    <span class="k">return</span> <span class="n">_mapattr</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
<a name="cl-729"></a>  
<a name="cl-730"></a><span class="c">#} // end of AttributeWrapper</span>
<a name="cl-731"></a>
<a name="cl-732"></a>
<a name="cl-733"></a><span class="c">#{ // BaseExpr</span>
<a name="cl-734"></a><span class="k">class</span> <span class="nc">BaseExpr</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-735"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-736"></a>    <span class="k">pass</span>
<a name="cl-737"></a>  
<a name="cl-738"></a>  <span class="k">def</span> <span class="nf">number</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-739"></a>    <span class="n">exrs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-740"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">exrs</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-741"></a>      <span class="n">result</span><span class="o">=</span><span class="n">exrs</span><span class="o">.</span><span class="n">number</span><span class="p">()</span>
<a name="cl-742"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-743"></a>      <span class="n">result</span><span class="o">=</span><span class="n">toNumber</span><span class="p">(</span><span class="n">exrs</span><span class="p">)</span>
<a name="cl-744"></a>    <span class="k">return</span> <span class="n">result</span>
<a name="cl-745"></a>  
<a name="cl-746"></a>  <span class="k">def</span> <span class="nf">string</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-747"></a>    <span class="n">exrs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-748"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">exrs</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-749"></a>      <span class="n">result</span><span class="o">=</span><span class="n">exrs</span><span class="o">.</span><span class="n">string</span><span class="p">()</span>
<a name="cl-750"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-751"></a>      <span class="n">result</span><span class="o">=</span><span class="n">toString</span><span class="p">(</span><span class="n">exrs</span><span class="p">)</span>
<a name="cl-752"></a>    <span class="k">return</span> <span class="n">result</span>
<a name="cl-753"></a>  
<a name="cl-754"></a>  <span class="k">def</span> <span class="nf">bool</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-755"></a>    <span class="n">exrs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-756"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">exrs</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-757"></a>      <span class="n">result</span><span class="o">=</span><span class="n">exrs</span><span class="o">.</span><span class="n">bool</span><span class="p">()</span>
<a name="cl-758"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-759"></a>      <span class="n">result</span><span class="o">=</span><span class="n">toBoolean</span><span class="p">(</span><span class="n">exrs</span><span class="p">)</span>
<a name="cl-760"></a>    <span class="k">return</span> <span class="n">result</span>
<a name="cl-761"></a>  
<a name="cl-762"></a><span class="c">#} // end of BaseExpr</span>
<a name="cl-763"></a>
<a name="cl-764"></a>
<a name="cl-765"></a><span class="c">#{ // BaseExprHasPredicates</span>
<a name="cl-766"></a><span class="k">class</span> <span class="nc">BaseExprHasPredicates</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-767"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-768"></a>    <span class="k">pass</span>
<a name="cl-769"></a>  
<a name="cl-770"></a>  <span class="k">def</span> <span class="nf">evaluatePredicates</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">start</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
<a name="cl-771"></a>    <span class="n">reverse</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;reverse&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">)</span>
<a name="cl-772"></a>    <span class="n">predicates</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;predicates&#39;</span><span class="p">,[])</span>
<a name="cl-773"></a>    
<a name="cl-774"></a>    <span class="n">nodeset</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
<a name="cl-775"></a>    
<a name="cl-776"></a>    <span class="n">l0</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">predicates</span><span class="p">)</span>
<a name="cl-777"></a>    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">start</span><span class="p">,</span><span class="n">l0</span><span class="p">):</span>
<a name="cl-778"></a>      <span class="n">predicate</span><span class="o">=</span><span class="n">predicates</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<a name="cl-779"></a>      <span class="n">deleteIndexes</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-780"></a>      <span class="n">nodes</span><span class="o">=</span><span class="n">nodeset</span><span class="o">.</span><span class="n">list</span><span class="p">()</span>
<a name="cl-781"></a>      
<a name="cl-782"></a>      <span class="n">l1</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
<a name="cl-783"></a>      <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">l1</span><span class="p">):</span>
<a name="cl-784"></a>        <span class="n">position</span><span class="o">=</span><span class="p">(</span><span class="n">l1</span><span class="o">-</span><span class="n">j</span><span class="p">)</span> <span class="k">if</span> <span class="n">reverse</span> <span class="k">else</span> <span class="p">(</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-785"></a>        <span class="n">exrs</span><span class="o">=</span><span class="n">predicate</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">Ctx</span><span class="p">(</span><span class="n">nodes</span><span class="p">[</span><span class="n">j</span><span class="p">],</span><span class="n">position</span><span class="p">,</span><span class="n">l1</span><span class="p">))</span>
<a name="cl-786"></a>        
<a name="cl-787"></a>        <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">exrs</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;number&#39;</span><span class="p">:</span>
<a name="cl-788"></a>          <span class="n">exrs</span><span class="o">=</span><span class="p">(</span><span class="n">position</span><span class="o">==</span><span class="n">exrs</span><span class="p">)</span>
<a name="cl-789"></a>        <span class="k">elif</span> <span class="n">typeof</span><span class="p">(</span><span class="n">exrs</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;string&#39;</span><span class="p">:</span>
<a name="cl-790"></a>          <span class="n">exrs</span><span class="o">=</span><span class="bp">False</span> <span class="k">if</span> <span class="n">exrs</span><span class="o">==</span><span class="s">&#39;&#39;</span> <span class="k">else</span> <span class="bp">True</span>
<a name="cl-791"></a>        <span class="k">elif</span> <span class="n">typeof</span><span class="p">(</span><span class="n">exrs</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;object&#39;</span><span class="p">:</span>
<a name="cl-792"></a>          <span class="n">exrs</span><span class="o">=</span><span class="n">exrs</span><span class="o">.</span><span class="n">bool</span><span class="p">()</span>
<a name="cl-793"></a>        
<a name="cl-794"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">exrs</span><span class="p">:</span>
<a name="cl-795"></a>          <span class="n">deleteIndexes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">j</span><span class="p">)</span>
<a name="cl-796"></a>      
<a name="cl-797"></a>      <span class="n">r</span><span class="o">=</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">deleteIndexes</span><span class="p">))</span>
<a name="cl-798"></a>      <span class="n">r</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-799"></a>      <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">r</span><span class="p">:</span>
<a name="cl-800"></a>        <span class="n">nodeset</span><span class="o">.</span><span class="n">_del</span><span class="p">(</span><span class="n">deleteIndexes</span><span class="p">[</span><span class="n">j</span><span class="p">])</span>
<a name="cl-801"></a>    
<a name="cl-802"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-803"></a>  
<a name="cl-804"></a>  <span class="nd">@classmethod</span>
<a name="cl-805"></a>  <span class="k">def</span> <span class="nf">parsePredicates</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">,</span><span class="n">expr</span><span class="p">):</span>
<a name="cl-806"></a>    <span class="k">while</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span><span class="o">==</span><span class="s">&#39;[&#39;</span><span class="p">:</span>
<a name="cl-807"></a>      <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-808"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-809"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;missing predicate expr&#39;</span><span class="p">)</span>
<a name="cl-810"></a>      <span class="n">predicate</span><span class="o">=</span><span class="n">BinaryExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-811"></a>      <span class="n">expr</span><span class="o">.</span><span class="n">predicate</span><span class="p">(</span><span class="n">predicate</span><span class="p">)</span>
<a name="cl-812"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-813"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;unclosed predicate expr&#39;</span><span class="p">)</span>
<a name="cl-814"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span> <span class="o">!=</span> <span class="s">&#39;]&#39;</span><span class="p">:</span>
<a name="cl-815"></a>        <span class="n">lexer</span><span class="o">.</span><span class="n">back</span><span class="p">()</span>
<a name="cl-816"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad token: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()))</span>
<a name="cl-817"></a>
<a name="cl-818"></a><span class="c">#} // end of BaseExprHasPredicates</span>
<a name="cl-819"></a>
<a name="cl-820"></a>
<a name="cl-821"></a><span class="c">#{ // BinaryExpr</span>
<a name="cl-822"></a><span class="k">class</span> <span class="nc">BinaryExpr</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-823"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">op</span><span class="p">,</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">):</span>
<a name="cl-824"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="o">=</span><span class="n">op</span>
<a name="cl-825"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">left</span><span class="o">=</span><span class="n">left</span>
<a name="cl-826"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">right</span><span class="o">=</span><span class="n">right</span>
<a name="cl-827"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">dataType</span><span class="o">=</span><span class="n">BinaryExpr</span><span class="o">.</span><span class="n">ops</span><span class="p">[</span><span class="n">op</span><span class="p">][</span><span class="mi">2</span><span class="p">]</span>
<a name="cl-828"></a>    <span class="p">(</span><span class="n">lneedContextPosition</span><span class="p">,</span><span class="n">rneedContextPosition</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="s">&#39;needContextPosition&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">),</span><span class="nb">getattr</span><span class="p">(</span><span class="n">right</span><span class="p">,</span><span class="s">&#39;needContextPosition&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">))</span>
<a name="cl-829"></a>    <span class="p">(</span><span class="n">lneedContextNode</span><span class="p">,</span><span class="n">rneedContextNode</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="s">&#39;needContextNode&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">),</span><span class="nb">getattr</span><span class="p">(</span><span class="n">right</span><span class="p">,</span><span class="s">&#39;needContextNode&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">))</span>
<a name="cl-830"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="n">lneedContextPosition</span> <span class="ow">or</span> <span class="n">rneedContextPosition</span>
<a name="cl-831"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextNode</span><span class="o">=</span><span class="n">lneedContextNode</span> <span class="ow">or</span> <span class="n">rneedContextNode</span>
<a name="cl-832"></a>    
<a name="cl-833"></a>    <span class="k">if</span> <span class="n">op</span><span class="o">==</span><span class="s">&#39;=&#39;</span><span class="p">:</span>
<a name="cl-834"></a>      <span class="p">(</span><span class="n">ldatatype</span><span class="p">,</span><span class="n">rdatatype</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="s">&#39;datatype&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">),</span><span class="nb">getattr</span><span class="p">(</span><span class="n">right</span><span class="p">,</span><span class="s">&#39;datatype&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">))</span>
<a name="cl-835"></a>      <span class="p">(</span><span class="n">lqattr</span><span class="p">,</span><span class="n">rqattr</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="s">&#39;quickAttr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">),</span><span class="nb">getattr</span><span class="p">(</span><span class="n">right</span><span class="p">,</span><span class="s">&#39;quickAttr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">))</span>
<a name="cl-836"></a>      
<a name="cl-837"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">rneedContextNode</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">rneedContextPosition</span> <span class="ow">and</span> <span class="n">rdatatype</span><span class="o">!=</span><span class="s">&#39;nodeset&#39;</span> <span class="ow">and</span> <span class="n">rdatatype</span><span class="o">!=</span><span class="s">&#39;void&#39;</span> <span class="ow">and</span> <span class="n">lqattr</span><span class="p">:</span>
<a name="cl-838"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">quickAttr</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-839"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">attrName</span><span class="o">=</span><span class="n">left</span><span class="o">.</span><span class="n">attrName</span>
<a name="cl-840"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">attrValueExpr</span><span class="o">=</span><span class="n">right</span>
<a name="cl-841"></a>      <span class="k">elif</span> <span class="ow">not</span> <span class="n">lneedContextNode</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">lneedContextPosition</span> <span class="ow">and</span> <span class="n">ldatatype</span><span class="o">!=</span><span class="s">&#39;nodeset&#39;</span> <span class="ow">and</span> <span class="n">ldatatype</span><span class="o">!=</span><span class="s">&#39;void&#39;</span> <span class="ow">and</span> <span class="n">rqattr</span><span class="p">:</span>
<a name="cl-842"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">quickAttr</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-843"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">attrName</span><span class="o">=</span><span class="n">right</span><span class="o">.</span><span class="n">attrName</span>
<a name="cl-844"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">attrValueExpr</span><span class="o">=</span><span class="n">left</span>
<a name="cl-845"></a>  
<a name="cl-846"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-847"></a>    <span class="n">result</span><span class="o">=</span><span class="n">BinaryExpr</span><span class="o">.</span><span class="n">ops</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="p">][</span><span class="mi">1</span><span class="p">](</span><span class="bp">self</span><span class="o">.</span><span class="n">left</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-848"></a>    <span class="k">return</span> <span class="n">result</span>
<a name="cl-849"></a>  
<a name="cl-850"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-851"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-852"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;binary: &#39;</span><span class="o">+</span><span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-853"></a>    <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-854"></a>    <span class="n">t</span><span class="o">+=</span><span class="bp">self</span><span class="o">.</span><span class="n">left</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-855"></a>    <span class="n">t</span><span class="o">+=</span><span class="bp">self</span><span class="o">.</span><span class="n">right</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-856"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-857"></a>  
<a name="cl-858"></a>  <span class="c"># --- Local Functions</span>
<a name="cl-859"></a>  <span class="nd">@staticmethod</span>
<a name="cl-860"></a>  <span class="k">def</span> <span class="nf">_compare</span><span class="p">(</span><span class="n">op</span><span class="p">,</span><span class="n">comp</span><span class="p">,</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-861"></a>    <span class="n">left</span><span class="o">=</span><span class="n">left</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-862"></a>    <span class="n">right</span><span class="o">=</span><span class="n">right</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-863"></a>    
<a name="cl-864"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">right</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-865"></a>      <span class="n">lnodes</span><span class="o">=</span><span class="n">left</span><span class="o">.</span><span class="n">list</span><span class="p">()</span>
<a name="cl-866"></a>      <span class="n">rnodes</span><span class="o">=</span><span class="n">right</span><span class="o">.</span><span class="n">list</span><span class="p">()</span>
<a name="cl-867"></a>      <span class="k">for</span> <span class="n">lnode</span> <span class="ow">in</span> <span class="n">lnodes</span><span class="p">:</span>
<a name="cl-868"></a>        <span class="k">for</span> <span class="n">rnode</span> <span class="ow">in</span> <span class="n">rnodes</span><span class="p">:</span>
<a name="cl-869"></a>          <span class="k">if</span> <span class="n">comp</span><span class="p">(</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="s">&#39;string&#39;</span><span class="p">,</span><span class="n">lnode</span><span class="p">),</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="s">&#39;string&#39;</span><span class="p">,</span><span class="n">rnode</span><span class="p">)):</span>
<a name="cl-870"></a>            <span class="k">return</span> <span class="bp">True</span>
<a name="cl-871"></a>      <span class="k">return</span> <span class="bp">False</span>
<a name="cl-872"></a>    
<a name="cl-873"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">right</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-874"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-875"></a>        <span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="n">primitive</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">)</span>
<a name="cl-876"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-877"></a>        <span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="n">primitive</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">right</span><span class="p">,</span><span class="n">left</span><span class="p">)</span>
<a name="cl-878"></a>      
<a name="cl-879"></a>      <span class="n">nodes</span><span class="o">=</span><span class="n">nodeset</span><span class="o">.</span><span class="n">list</span><span class="p">()</span>
<a name="cl-880"></a>      <span class="nb">type</span><span class="o">=</span><span class="n">typeof</span><span class="p">(</span><span class="n">primitive</span><span class="p">)</span>
<a name="cl-881"></a>      <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-882"></a>        <span class="k">if</span> <span class="n">comp</span><span class="p">(</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="nb">type</span><span class="p">,</span><span class="n">node</span><span class="p">),</span><span class="n">primitive</span><span class="p">):</span>
<a name="cl-883"></a>          <span class="k">return</span> <span class="bp">True</span>
<a name="cl-884"></a>      <span class="k">return</span> <span class="bp">False</span>
<a name="cl-885"></a>    
<a name="cl-886"></a>    <span class="k">if</span> <span class="n">op</span><span class="o">==</span><span class="s">&#39;=&#39;</span> <span class="ow">or</span> <span class="n">op</span><span class="o">==</span><span class="s">&#39;!=&#39;</span><span class="p">:</span>
<a name="cl-887"></a>      <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">left</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;boolean&#39;</span> <span class="ow">or</span> <span class="n">typeof</span><span class="p">(</span><span class="n">right</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;boolean&#39;</span><span class="p">:</span>
<a name="cl-888"></a>        <span class="k">return</span> <span class="n">comp</span><span class="p">(</span><span class="n">toBoolean</span><span class="p">(</span><span class="n">left</span><span class="p">),</span><span class="n">toBoolean</span><span class="p">(</span><span class="n">right</span><span class="p">))</span>
<a name="cl-889"></a>      <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">left</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;number&#39;</span> <span class="ow">or</span> <span class="n">typeof</span><span class="p">(</span><span class="n">right</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;number&#39;</span><span class="p">:</span>
<a name="cl-890"></a>        <span class="k">return</span> <span class="n">comp</span><span class="p">(</span><span class="n">toNumber</span><span class="p">(</span><span class="n">left</span><span class="p">),</span><span class="n">toNumber</span><span class="p">(</span><span class="n">right</span><span class="p">))</span>
<a name="cl-891"></a>      <span class="k">return</span> <span class="n">comp</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">)</span>
<a name="cl-892"></a>    
<a name="cl-893"></a>    <span class="k">return</span> <span class="n">comp</span><span class="p">(</span><span class="n">toNumber</span><span class="p">(</span><span class="n">left</span><span class="p">),</span><span class="n">toNumber</span><span class="p">(</span><span class="n">right</span><span class="p">))</span>
<a name="cl-894"></a>  
<a name="cl-895"></a>  <span class="k">def</span> <span class="nf">_div</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-896"></a>    <span class="n">l</span><span class="o">=</span><span class="n">left</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-897"></a>    <span class="n">r</span><span class="o">=</span><span class="n">right</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-898"></a>    <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">l</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span> <span class="ow">or</span> <span class="n">typeof</span><span class="p">(</span><span class="n">r</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;NaN&#39;</span>
<a name="cl-899"></a>    <span class="k">if</span> <span class="n">r</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-900"></a>      <span class="n">sign</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="s">&#39;op&#39;</span><span class="p">,</span><span class="s">&#39;+&#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;1&#39;</span><span class="p">)</span><span class="o">*</span><span class="nb">int</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">right</span><span class="p">,</span><span class="s">&#39;op&#39;</span><span class="p">,</span><span class="s">&#39;+&#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;1&#39;</span><span class="p">)</span>
<a name="cl-901"></a>      <span class="k">if</span> <span class="n">l</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;NaN&#39;</span>
<a name="cl-902"></a>      <span class="k">elif</span> <span class="n">sign</span><span class="o">&lt;</span><span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;-Infinity&#39;</span>
<a name="cl-903"></a>      <span class="k">else</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;Infinity&#39;</span>
<a name="cl-904"></a>    <span class="n">n</span><span class="o">=</span><span class="nb">float</span><span class="p">(</span><span class="n">l</span><span class="p">)</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="n">r</span><span class="p">)</span>
<a name="cl-905"></a>    <span class="n">n1</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<a name="cl-906"></a>    <span class="k">return</span> <span class="n">n1</span> <span class="k">if</span> <span class="n">n1</span><span class="o">==</span><span class="n">n</span> <span class="k">else</span> <span class="n">n</span>
<a name="cl-907"></a>  
<a name="cl-908"></a>  <span class="k">def</span> <span class="nf">_mod</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-909"></a>    <span class="n">l</span><span class="o">=</span><span class="n">left</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-910"></a>    <span class="n">r</span><span class="o">=</span><span class="n">right</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-911"></a>    <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">l</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span> <span class="ow">or</span> <span class="n">typeof</span><span class="p">(</span><span class="n">r</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;NaN&#39;</span>
<a name="cl-912"></a>    <span class="k">if</span> <span class="n">r</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-913"></a>      <span class="k">if</span> <span class="n">l</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;NaN&#39;</span>
<a name="cl-914"></a>      <span class="k">else</span><span class="p">:</span> <span class="k">return</span> <span class="mi">0</span>
<a name="cl-915"></a>    <span class="k">return</span> <span class="n">l</span> <span class="o">%</span> <span class="n">r</span>
<a name="cl-916"></a>  
<a name="cl-917"></a>  <span class="k">def</span> <span class="nf">_mul</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-918"></a>    <span class="n">l</span><span class="o">=</span><span class="n">left</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-919"></a>    <span class="n">r</span><span class="o">=</span><span class="n">right</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-920"></a>    <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">l</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span> <span class="ow">or</span> <span class="n">typeof</span><span class="p">(</span><span class="n">r</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;NaN&#39;</span>
<a name="cl-921"></a>    <span class="n">n</span><span class="o">=</span><span class="n">l</span> <span class="o">*</span> <span class="n">r</span>
<a name="cl-922"></a>    <span class="n">n1</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<a name="cl-923"></a>    <span class="k">return</span> <span class="n">n1</span> <span class="k">if</span> <span class="n">n1</span><span class="o">==</span><span class="n">n</span> <span class="k">else</span> <span class="n">n</span>
<a name="cl-924"></a>  
<a name="cl-925"></a>  <span class="k">def</span> <span class="nf">_add</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-926"></a>    <span class="n">l</span><span class="o">=</span><span class="n">left</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-927"></a>    <span class="n">r</span><span class="o">=</span><span class="n">right</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-928"></a>    <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">l</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span> <span class="ow">or</span> <span class="n">typeof</span><span class="p">(</span><span class="n">r</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;NaN&#39;</span>
<a name="cl-929"></a>    <span class="n">n</span><span class="o">=</span><span class="n">l</span> <span class="o">+</span> <span class="n">r</span>
<a name="cl-930"></a>    <span class="n">n1</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<a name="cl-931"></a>    <span class="k">return</span> <span class="n">n1</span> <span class="k">if</span> <span class="n">n1</span><span class="o">==</span><span class="n">n</span> <span class="k">else</span> <span class="n">n</span>
<a name="cl-932"></a>  
<a name="cl-933"></a>  <span class="k">def</span> <span class="nf">_sub</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-934"></a>    <span class="n">l</span><span class="o">=</span><span class="n">left</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-935"></a>    <span class="n">r</span><span class="o">=</span><span class="n">right</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-936"></a>    <span class="k">if</span> <span class="n">typeof</span><span class="p">(</span><span class="n">l</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span> <span class="ow">or</span> <span class="n">typeof</span><span class="p">(</span><span class="n">r</span><span class="p">)</span><span class="o">!=</span><span class="s">&#39;number&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="s">&#39;NaN&#39;</span>
<a name="cl-937"></a>    <span class="n">n</span><span class="o">=</span><span class="n">l</span> <span class="o">-</span> <span class="n">r</span>
<a name="cl-938"></a>    <span class="n">n1</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<a name="cl-939"></a>    <span class="k">return</span> <span class="n">n1</span> <span class="k">if</span> <span class="n">n1</span><span class="o">==</span><span class="n">n</span> <span class="k">else</span> <span class="n">n</span>
<a name="cl-940"></a>  
<a name="cl-941"></a>  <span class="k">def</span> <span class="nf">_lt</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-942"></a>    <span class="k">return</span> <span class="n">BinaryExpr</span><span class="o">.</span><span class="n">_compare</span><span class="p">(</span><span class="s">&#39;&lt;&#39;</span><span class="p">,(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">:</span><span class="n">a</span><span class="o">&lt;</span><span class="n">b</span><span class="p">),</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-943"></a>  
<a name="cl-944"></a>  <span class="k">def</span> <span class="nf">_gt</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-945"></a>    <span class="k">return</span> <span class="n">BinaryExpr</span><span class="o">.</span><span class="n">_compare</span><span class="p">(</span><span class="s">&#39;&gt;&#39;</span><span class="p">,(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">:</span><span class="n">a</span><span class="o">&gt;</span><span class="n">b</span><span class="p">),</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-946"></a>  
<a name="cl-947"></a>  <span class="k">def</span> <span class="nf">_le</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-948"></a>    <span class="k">return</span> <span class="n">BinaryExpr</span><span class="o">.</span><span class="n">_compare</span><span class="p">(</span><span class="s">&#39;&lt;=&#39;</span><span class="p">,(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">:</span><span class="n">a</span><span class="o">&lt;=</span><span class="n">b</span><span class="p">),</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-949"></a>  
<a name="cl-950"></a>  <span class="k">def</span> <span class="nf">_ge</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-951"></a>    <span class="k">return</span> <span class="n">BinaryExpr</span><span class="o">.</span><span class="n">_compare</span><span class="p">(</span><span class="s">&#39;&gt;=&#39;</span><span class="p">,(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">:</span><span class="n">a</span><span class="o">&gt;=</span><span class="n">b</span><span class="p">),</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-952"></a>  
<a name="cl-953"></a>  <span class="k">def</span> <span class="nf">_eq</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-954"></a>    <span class="k">return</span> <span class="n">BinaryExpr</span><span class="o">.</span><span class="n">_compare</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">,(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">:</span><span class="n">a</span><span class="o">==</span><span class="n">b</span><span class="p">),</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-955"></a>  
<a name="cl-956"></a>  <span class="k">def</span> <span class="nf">_ne</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-957"></a>    <span class="k">return</span> <span class="n">BinaryExpr</span><span class="o">.</span><span class="n">_compare</span><span class="p">(</span><span class="s">&#39;!=&#39;</span><span class="p">,(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">:</span><span class="n">a</span><span class="o">!=</span><span class="n">b</span><span class="p">),</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-958"></a>  
<a name="cl-959"></a>  <span class="k">def</span> <span class="nf">_and</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-960"></a>    <span class="k">return</span> <span class="n">left</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span> <span class="o">&amp;</span> <span class="n">right</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-961"></a>  
<a name="cl-962"></a>  <span class="k">def</span> <span class="nf">_or</span><span class="p">(</span><span class="n">left</span><span class="p">,</span><span class="n">right</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-963"></a>    <span class="k">return</span> <span class="n">left</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span> <span class="o">|</span> <span class="n">right</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-964"></a>  
<a name="cl-965"></a>  <span class="n">ops</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-966"></a>      <span class="s">&#39;div&#39;</span><span class="p">:[</span><span class="mi">6</span><span class="p">,</span><span class="n">_div</span><span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">]</span>
<a name="cl-967"></a>    <span class="p">,</span> <span class="s">&#39;mod&#39;</span><span class="p">:[</span><span class="mi">6</span><span class="p">,</span><span class="n">_mod</span><span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">]</span>
<a name="cl-968"></a>    <span class="p">,</span> <span class="s">&#39;*&#39;</span>  <span class="p">:[</span><span class="mi">6</span><span class="p">,</span><span class="n">_mul</span><span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">]</span>
<a name="cl-969"></a>    <span class="p">,</span> <span class="s">&#39;+&#39;</span>  <span class="p">:[</span><span class="mi">5</span><span class="p">,</span><span class="n">_add</span><span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">]</span>
<a name="cl-970"></a>    <span class="p">,</span> <span class="s">&#39;-&#39;</span>  <span class="p">:[</span><span class="mi">5</span><span class="p">,</span><span class="n">_sub</span><span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">]</span>
<a name="cl-971"></a>    <span class="p">,</span> <span class="s">&#39;&lt;&#39;</span>  <span class="p">:[</span><span class="mi">4</span><span class="p">,</span><span class="n">_lt</span> <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">]</span>
<a name="cl-972"></a>    <span class="p">,</span> <span class="s">&#39;&gt;&#39;</span>  <span class="p">:[</span><span class="mi">4</span><span class="p">,</span><span class="n">_gt</span> <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">]</span>
<a name="cl-973"></a>    <span class="p">,</span> <span class="s">&#39;&lt;=&#39;</span> <span class="p">:[</span><span class="mi">4</span><span class="p">,</span><span class="n">_le</span> <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">]</span>
<a name="cl-974"></a>    <span class="p">,</span> <span class="s">&#39;&gt;=&#39;</span> <span class="p">:[</span><span class="mi">4</span><span class="p">,</span><span class="n">_ge</span> <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">]</span>
<a name="cl-975"></a>    <span class="p">,</span> <span class="s">&#39;=&#39;</span>  <span class="p">:[</span><span class="mi">3</span><span class="p">,</span><span class="n">_eq</span> <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">]</span>
<a name="cl-976"></a>    <span class="p">,</span> <span class="s">&#39;!=&#39;</span> <span class="p">:[</span><span class="mi">3</span><span class="p">,</span><span class="n">_ne</span> <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">]</span>
<a name="cl-977"></a>    <span class="p">,</span> <span class="s">&#39;and&#39;</span><span class="p">:[</span><span class="mi">2</span><span class="p">,</span><span class="n">_and</span><span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">]</span>
<a name="cl-978"></a>    <span class="p">,</span> <span class="s">&#39;or&#39;</span> <span class="p">:[</span><span class="mi">1</span><span class="p">,</span><span class="n">_or</span> <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">]</span>
<a name="cl-979"></a>  <span class="p">})</span>
<a name="cl-980"></a>  
<a name="cl-981"></a>  <span class="nd">@classmethod</span>
<a name="cl-982"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-983"></a>    <span class="n">ops</span><span class="o">=</span><span class="n">cls</span><span class="o">.</span><span class="n">ops</span>
<a name="cl-984"></a>    <span class="n">stack</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-985"></a>    <span class="n">index</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">index</span>
<a name="cl-986"></a>    
<a name="cl-987"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-988"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-989"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;missing right expression&#39;</span><span class="p">)</span>
<a name="cl-990"></a>      <span class="n">expr</span><span class="o">=</span><span class="n">UnaryExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-991"></a>      
<a name="cl-992"></a>      <span class="n">op</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-993"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">op</span><span class="p">:</span>
<a name="cl-994"></a>        <span class="k">break</span>
<a name="cl-995"></a>      
<a name="cl-996"></a>      <span class="n">info</span><span class="o">=</span><span class="n">ops</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">op</span><span class="p">)</span>
<a name="cl-997"></a>      <span class="n">precedence</span><span class="o">=</span><span class="n">info</span> <span class="ow">and</span> <span class="n">info</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-998"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">precedence</span><span class="p">:</span>
<a name="cl-999"></a>        <span class="n">lexer</span><span class="o">.</span><span class="n">back</span><span class="p">()</span>
<a name="cl-1000"></a>        <span class="k">break</span>
<a name="cl-1001"></a>      
<a name="cl-1002"></a>      <span class="k">while</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="n">stack</span><span class="p">)</span> <span class="ow">and</span> <span class="n">precedence</span><span class="o">&lt;=</span><span class="n">ops</span><span class="p">[</span><span class="n">stack</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">stack</span><span class="p">)</span><span class="o">-</span><span class="mi">1</span><span class="p">]][</span><span class="mi">0</span><span class="p">]:</span>
<a name="cl-1003"></a>        <span class="n">expr</span><span class="o">=</span><span class="n">BinaryExpr</span><span class="p">(</span><span class="n">stack</span><span class="o">.</span><span class="n">pop</span><span class="p">(),</span><span class="n">stack</span><span class="o">.</span><span class="n">pop</span><span class="p">(),</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-1004"></a>      
<a name="cl-1005"></a>      <span class="n">stack</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">expr</span><span class="p">,</span><span class="n">op</span><span class="p">])</span>
<a name="cl-1006"></a>    
<a name="cl-1007"></a>    <span class="k">while</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="n">stack</span><span class="p">):</span>
<a name="cl-1008"></a>      <span class="n">expr</span><span class="o">=</span><span class="n">BinaryExpr</span><span class="p">(</span><span class="n">stack</span><span class="o">.</span><span class="n">pop</span><span class="p">(),</span><span class="n">stack</span><span class="o">.</span><span class="n">pop</span><span class="p">(),</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-1009"></a>    
<a name="cl-1010"></a>    <span class="k">return</span> <span class="n">expr</span>
<a name="cl-1011"></a>
<a name="cl-1012"></a><span class="c">#} // end of BinaryExpr</span>
<a name="cl-1013"></a>
<a name="cl-1014"></a>
<a name="cl-1015"></a><span class="c">#{ // UnaryExpr</span>
<a name="cl-1016"></a><span class="k">class</span> <span class="nc">UnaryExpr</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1017"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">op</span><span class="p">,</span><span class="n">expr</span><span class="p">):</span>
<a name="cl-1018"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="o">=</span><span class="n">op</span>
<a name="cl-1019"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">expr</span><span class="o">=</span><span class="n">expr</span>
<a name="cl-1020"></a>    
<a name="cl-1021"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">expr</span><span class="p">,</span><span class="s">&#39;needContextPosition&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1022"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextNode</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">expr</span><span class="p">,</span><span class="s">&#39;needContextNode&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1023"></a>    
<a name="cl-1024"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">datatype</span><span class="o">=</span><span class="s">&#39;number&#39;</span>
<a name="cl-1025"></a>  
<a name="cl-1026"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-1027"></a>    <span class="n">result</span><span class="o">=-</span><span class="bp">self</span><span class="o">.</span><span class="n">expr</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-1028"></a>    <span class="k">return</span> <span class="n">result</span>
<a name="cl-1029"></a>  
<a name="cl-1030"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1031"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1032"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;unary: &#39;</span><span class="o">+</span><span class="bp">self</span><span class="o">.</span><span class="n">op</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1033"></a>    <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1034"></a>    <span class="n">t</span><span class="o">+=</span><span class="bp">self</span><span class="o">.</span><span class="n">expr</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-1035"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1036"></a>
<a name="cl-1037"></a>  <span class="n">ops</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-1038"></a>    <span class="s">&#39;-&#39;</span><span class="p">:</span><span class="mi">1</span>
<a name="cl-1039"></a>  <span class="p">})</span>
<a name="cl-1040"></a>  
<a name="cl-1041"></a>  <span class="nd">@classmethod</span>
<a name="cl-1042"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1043"></a>    <span class="n">ops</span><span class="o">=</span><span class="n">cls</span><span class="o">.</span><span class="n">ops</span>
<a name="cl-1044"></a>    <span class="k">if</span> <span class="n">ops</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()):</span>
<a name="cl-1045"></a>      <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">(),</span><span class="n">cls</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">))</span>
<a name="cl-1046"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1047"></a>      <span class="k">return</span> <span class="n">UnionExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1048"></a>
<a name="cl-1049"></a><span class="c">#} // end of UnaryExpr</span>
<a name="cl-1050"></a>
<a name="cl-1051"></a>
<a name="cl-1052"></a><span class="c">#{ // UnionExpr</span>
<a name="cl-1053"></a><span class="k">class</span> <span class="nc">UnionExpr</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1054"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-1055"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">paths</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-1056"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">datatype</span><span class="o">=</span><span class="s">&#39;nodeset&#39;</span>
<a name="cl-1057"></a>  
<a name="cl-1058"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-1059"></a>    <span class="n">paths</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">paths</span>
<a name="cl-1060"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="n">NodeSet</span><span class="p">()</span>
<a name="cl-1061"></a>    <span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">paths</span><span class="p">:</span>
<a name="cl-1062"></a>      <span class="n">exrs</span><span class="o">=</span><span class="n">path</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-1063"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">exrs</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1064"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;PathExpr must be nodeset&#39;</span><span class="p">)</span>
<a name="cl-1065"></a>      <span class="n">nodeset</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">exrs</span><span class="p">)</span>
<a name="cl-1066"></a>    
<a name="cl-1067"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1068"></a>  
<a name="cl-1069"></a>  <span class="k">def</span> <span class="nf">path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">path</span><span class="p">):</span>
<a name="cl-1070"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">paths</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
<a name="cl-1071"></a>    
<a name="cl-1072"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">path</span><span class="p">,</span><span class="s">&#39;needContextPosition&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1073"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-1074"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">path</span><span class="p">,</span><span class="s">&#39;needContextNode&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1075"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">needContextNode</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-1076"></a>  
<a name="cl-1077"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1078"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1079"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;union: &#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1080"></a>    <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1081"></a>    <span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">paths</span><span class="p">:</span>
<a name="cl-1082"></a>      <span class="n">t</span><span class="o">+=</span><span class="n">path</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-1083"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1084"></a>  
<a name="cl-1085"></a>  <span class="n">ops</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-1086"></a>    <span class="s">&#39;|&#39;</span><span class="p">:</span><span class="mi">1</span>
<a name="cl-1087"></a>  <span class="p">})</span>
<a name="cl-1088"></a>  
<a name="cl-1089"></a>  <span class="nd">@classmethod</span>
<a name="cl-1090"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1091"></a>    <span class="n">ops</span><span class="o">=</span><span class="n">cls</span><span class="o">.</span><span class="n">ops</span>
<a name="cl-1092"></a>    <span class="n">expr</span><span class="o">=</span><span class="n">PathExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1093"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">ops</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()):</span>
<a name="cl-1094"></a>      <span class="k">return</span> <span class="n">expr</span>
<a name="cl-1095"></a>    
<a name="cl-1096"></a>    <span class="n">union</span><span class="o">=</span><span class="n">UnionExpr</span><span class="p">()</span>
<a name="cl-1097"></a>    <span class="n">union</span><span class="o">.</span><span class="n">path</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-1098"></a>    
<a name="cl-1099"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1100"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">ops</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()):</span>
<a name="cl-1101"></a>        <span class="k">break</span>
<a name="cl-1102"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-1103"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;missing next union location path&#39;</span><span class="p">)</span>
<a name="cl-1104"></a>      <span class="n">union</span><span class="o">.</span><span class="n">path</span><span class="p">(</span><span class="n">PathExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">))</span>
<a name="cl-1105"></a>    
<a name="cl-1106"></a>    <span class="n">lexer</span><span class="o">.</span><span class="n">back</span><span class="p">()</span>
<a name="cl-1107"></a>    <span class="k">return</span> <span class="n">union</span>
<a name="cl-1108"></a>
<a name="cl-1109"></a><span class="c">#} // end of UnionExpr</span>
<a name="cl-1110"></a>
<a name="cl-1111"></a>
<a name="cl-1112"></a><span class="c">#{ // PathExpr</span>
<a name="cl-1113"></a><span class="k">class</span> <span class="nc">PathExpr</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1114"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="nb">filter</span><span class="p">):</span>
<a name="cl-1115"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">filter</span><span class="o">=</span><span class="nb">filter</span>
<a name="cl-1116"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">steps</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-1117"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">datatype</span><span class="o">=</span><span class="nb">filter</span><span class="o">.</span><span class="n">datatype</span>
<a name="cl-1118"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="nb">filter</span><span class="o">.</span><span class="n">needContextPosition</span>
<a name="cl-1119"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextNode</span><span class="o">=</span><span class="nb">filter</span><span class="o">.</span><span class="n">needContextNode</span>
<a name="cl-1120"></a>  
<a name="cl-1121"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-1122"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">filter</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-1123"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1124"></a>      <span class="n">throwException</span><span class="p">(</span><span class="s">&#39;Filter nodeset must be nodeset type&#39;</span><span class="p">)</span>
<a name="cl-1125"></a>    
<a name="cl-1126"></a>    <span class="k">for</span> <span class="n">_step</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">steps</span><span class="p">:</span>
<a name="cl-1127"></a>      <span class="k">if</span> <span class="n">nodeset</span><span class="o">.</span><span class="n">length</span><span class="o">&lt;=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1128"></a>        <span class="k">break</span>
<a name="cl-1129"></a>      <span class="n">step</span><span class="o">=</span><span class="n">_step</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="c"># _step=[op,step]</span>
<a name="cl-1130"></a>      <span class="n">reverse</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">reverse</span>
<a name="cl-1131"></a>      <span class="nb">iter</span><span class="o">=</span><span class="n">nodeset</span><span class="o">.</span><span class="n">iterator</span><span class="p">(</span><span class="n">reverse</span><span class="p">)</span>
<a name="cl-1132"></a>      <span class="n">prevNodeset</span><span class="o">=</span><span class="n">nodeset</span>
<a name="cl-1133"></a>      <span class="n">nodeset</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-1134"></a>      <span class="n">needContextPosition</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">step</span><span class="p">,</span><span class="s">&#39;needContextPosition&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1135"></a>      <span class="n">axis</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">axis</span>
<a name="cl-1136"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">needContextPosition</span> <span class="ow">and</span> <span class="n">axis</span><span class="o">==</span><span class="s">&#39;following&#39;</span><span class="p">:</span>
<a name="cl-1137"></a>        <span class="n">node</span><span class="o">=</span><span class="nb">iter</span><span class="p">()</span>
<a name="cl-1138"></a>        <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1139"></a>          <span class="nb">next</span><span class="o">=</span><span class="nb">iter</span><span class="p">()</span>
<a name="cl-1140"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="nb">next</span><span class="p">:</span>
<a name="cl-1141"></a>            <span class="k">break</span>
<a name="cl-1142"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="nb">next</span><span class="p">):</span>
<a name="cl-1143"></a>            <span class="k">break</span>
<a name="cl-1144"></a>          <span class="n">node</span><span class="o">=</span><span class="nb">next</span>
<a name="cl-1145"></a>        
<a name="cl-1146"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">Ctx</span><span class="p">(</span><span class="n">node</span><span class="p">))</span>
<a name="cl-1147"></a>      
<a name="cl-1148"></a>      <span class="k">elif</span> <span class="ow">not</span> <span class="n">needContextPosition</span> <span class="ow">and</span> <span class="n">axis</span><span class="o">==</span><span class="s">&#39;preceding&#39;</span><span class="p">:</span>
<a name="cl-1149"></a>        <span class="n">node</span><span class="o">=</span><span class="nb">iter</span><span class="p">()</span>
<a name="cl-1150"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">Ctx</span><span class="p">(</span><span class="n">node</span><span class="p">))</span>
<a name="cl-1151"></a>      
<a name="cl-1152"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-1153"></a>        <span class="n">node</span><span class="o">=</span><span class="nb">iter</span><span class="p">()</span>
<a name="cl-1154"></a>        <span class="n">j</span><span class="o">=</span><span class="mi">0</span>
<a name="cl-1155"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">Ctx</span><span class="p">(</span><span class="n">node</span><span class="p">),</span><span class="bp">False</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">j</span><span class="p">)</span>
<a name="cl-1156"></a>        <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1157"></a>          <span class="n">node</span><span class="o">=</span><span class="nb">iter</span><span class="p">()</span>
<a name="cl-1158"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-1159"></a>            <span class="k">break</span>
<a name="cl-1160"></a>          <span class="n">j</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-1161"></a>          <span class="n">nodeset</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">step</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">Ctx</span><span class="p">(</span><span class="n">node</span><span class="p">),</span><span class="bp">False</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">j</span><span class="p">))</span>
<a name="cl-1162"></a>    
<a name="cl-1163"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1164"></a>  
<a name="cl-1165"></a>  <span class="k">def</span> <span class="nf">step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">op</span><span class="p">,</span><span class="n">step</span><span class="p">):</span>
<a name="cl-1166"></a>    <span class="n">step</span><span class="o">.</span><span class="n">op</span><span class="o">=</span><span class="n">op</span>
<a name="cl-1167"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">steps</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">op</span><span class="p">,</span><span class="n">step</span><span class="p">])</span>
<a name="cl-1168"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">quickAttr</span><span class="o">=</span><span class="bp">False</span>
<a name="cl-1169"></a>    
<a name="cl-1170"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">steps</span><span class="p">)</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-1171"></a>      <span class="k">if</span> <span class="n">op</span><span class="o">==</span><span class="s">&#39;/&#39;</span> <span class="ow">and</span> <span class="n">step</span><span class="o">.</span><span class="n">axis</span><span class="o">==</span><span class="s">&#39;attribute&#39;</span><span class="p">:</span>
<a name="cl-1172"></a>        <span class="n">test</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">test</span>
<a name="cl-1173"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="s">&#39;notOnlyElement&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">and</span> <span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="o">!=</span><span class="s">&#39;*&#39;</span><span class="p">:</span>
<a name="cl-1174"></a>          <span class="bp">self</span><span class="o">.</span><span class="n">quickAttr</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-1175"></a>          <span class="bp">self</span><span class="o">.</span><span class="n">attrName</span><span class="o">=</span><span class="n">test</span><span class="o">.</span><span class="n">name</span>
<a name="cl-1176"></a>  
<a name="cl-1177"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1178"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1179"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;path: &#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1180"></a>    <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1181"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;filter:&#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1182"></a>    <span class="n">t</span><span class="o">+=</span><span class="bp">self</span><span class="o">.</span><span class="n">filter</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="o">+</span><span class="n">indent_space</span><span class="p">)</span>
<a name="cl-1183"></a>    <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">steps</span><span class="p">):</span>
<a name="cl-1184"></a>      <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;steps:&#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1185"></a>      <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1186"></a>      <span class="k">for</span> <span class="n">_step</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">steps</span><span class="p">:</span>
<a name="cl-1187"></a>        <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;operator: &#39;</span><span class="o">+</span><span class="n">step</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1188"></a>        <span class="n">t</span><span class="o">+=</span><span class="n">_step</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span> <span class="c"># _step=[op,step]</span>
<a name="cl-1189"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1190"></a>  
<a name="cl-1191"></a>  <span class="n">ops</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-1192"></a>    <span class="s">&#39;//&#39;</span><span class="p">:</span><span class="mi">1</span>
<a name="cl-1193"></a>  <span class="p">,</span> <span class="s">&#39;/&#39;</span><span class="p">:</span> <span class="mi">1</span>
<a name="cl-1194"></a>  <span class="p">})</span>
<a name="cl-1195"></a>  
<a name="cl-1196"></a>  <span class="nd">@classmethod</span>
<a name="cl-1197"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1198"></a>    <span class="n">ops</span><span class="o">=</span><span class="n">cls</span><span class="o">.</span><span class="n">ops</span>
<a name="cl-1199"></a>    <span class="k">if</span> <span class="n">ops</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()):</span>
<a name="cl-1200"></a>      <span class="n">op</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1201"></a>      <span class="n">token</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span>
<a name="cl-1202"></a>      
<a name="cl-1203"></a>      <span class="k">if</span> <span class="n">op</span><span class="o">==</span><span class="s">&#39;/&#39;</span> <span class="ow">and</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span> <span class="ow">or</span> <span class="p">(</span><span class="n">token</span><span class="o">!=</span><span class="s">&#39;.&#39;</span> <span class="ow">and</span> <span class="n">token</span><span class="o">!=</span><span class="s">&#39;..&#39;</span> <span class="ow">and</span> <span class="n">token</span><span class="o">!=</span><span class="s">&#39;@&#39;</span> <span class="ow">and</span> <span class="n">token</span><span class="o">!=</span><span class="s">&#39;*&#39;</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">re_has_ualpha</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">token</span><span class="p">)):</span>
<a name="cl-1204"></a>        <span class="k">return</span> <span class="n">FilterExpr</span><span class="o">.</span><span class="n">root</span><span class="p">()</span>
<a name="cl-1205"></a>      
<a name="cl-1206"></a>      <span class="n">path</span><span class="o">=</span><span class="n">PathExpr</span><span class="p">(</span><span class="n">FilterExpr</span><span class="o">.</span><span class="n">root</span><span class="p">())</span> <span class="c"># RootExpr</span>
<a name="cl-1207"></a>      
<a name="cl-1208"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-1209"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;missing next location step&#39;</span><span class="p">)</span>
<a name="cl-1210"></a>      <span class="n">expr</span><span class="o">=</span><span class="n">Step</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1211"></a>      <span class="n">path</span><span class="o">.</span><span class="n">step</span><span class="p">(</span><span class="n">op</span><span class="p">,</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-1212"></a>    
<a name="cl-1213"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1214"></a>      <span class="n">expr</span><span class="o">=</span><span class="n">FilterExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1215"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">expr</span><span class="p">:</span>
<a name="cl-1216"></a>        <span class="n">expr</span><span class="o">=</span><span class="n">Step</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1217"></a>        <span class="n">path</span><span class="o">=</span><span class="n">PathExpr</span><span class="p">(</span><span class="n">FilterExpr</span><span class="o">.</span><span class="n">context</span><span class="p">())</span>
<a name="cl-1218"></a>        <span class="n">path</span><span class="o">.</span><span class="n">step</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">,</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-1219"></a>      <span class="k">elif</span> <span class="ow">not</span> <span class="n">ops</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()):</span>
<a name="cl-1220"></a>        <span class="k">return</span> <span class="n">expr</span>
<a name="cl-1221"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-1222"></a>        <span class="n">path</span><span class="o">=</span><span class="n">PathExpr</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-1223"></a>    
<a name="cl-1224"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1225"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">ops</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()):</span>
<a name="cl-1226"></a>        <span class="k">break</span>
<a name="cl-1227"></a>      <span class="n">op</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1228"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-1229"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;missing next location step&#39;</span><span class="p">)</span>
<a name="cl-1230"></a>      <span class="n">path</span><span class="o">.</span><span class="n">step</span><span class="p">(</span><span class="n">op</span><span class="p">,</span><span class="n">Step</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">))</span>
<a name="cl-1231"></a>    
<a name="cl-1232"></a>    <span class="k">return</span> <span class="n">path</span>
<a name="cl-1233"></a>  
<a name="cl-1234"></a><span class="c">#} // end of PathExpr</span>
<a name="cl-1235"></a>
<a name="cl-1236"></a>
<a name="cl-1237"></a><span class="c">#{ // FilterExpr</span>
<a name="cl-1238"></a><span class="k">class</span> <span class="nc">FilterExpr</span><span class="p">(</span><span class="n">BaseExprHasPredicates</span><span class="p">):</span>
<a name="cl-1239"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">primary</span><span class="p">):</span>
<a name="cl-1240"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">primary</span><span class="o">=</span><span class="n">primary</span>
<a name="cl-1241"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-1242"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">datatype</span><span class="o">=</span><span class="n">primary</span><span class="o">.</span><span class="n">datatype</span>
<a name="cl-1243"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="n">primary</span><span class="o">.</span><span class="n">needContextPosition</span>
<a name="cl-1244"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextNode</span><span class="o">=</span><span class="n">primary</span><span class="o">.</span><span class="n">needContextNode</span>
<a name="cl-1245"></a>  
<a name="cl-1246"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-1247"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">primary</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
<a name="cl-1248"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1249"></a>      <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="p">):</span>
<a name="cl-1250"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Primary result must be nodeset type if filter have predicate expression&#39;</span><span class="p">)</span>
<a name="cl-1251"></a>        <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1252"></a>    
<a name="cl-1253"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluatePredicates</span><span class="p">(</span><span class="n">nodeset</span><span class="p">)</span>
<a name="cl-1254"></a>  
<a name="cl-1255"></a>  <span class="k">def</span> <span class="nf">predicate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">predicate</span><span class="p">):</span>
<a name="cl-1256"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">predicate</span><span class="p">)</span>
<a name="cl-1257"></a>  
<a name="cl-1258"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1259"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1260"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;filter: &#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1261"></a>    <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1262"></a>    <span class="n">t</span><span class="o">+=</span><span class="bp">self</span><span class="o">.</span><span class="n">primary</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="o">+</span><span class="n">indent_space</span><span class="p">)</span>
<a name="cl-1263"></a>    <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="p">):</span>
<a name="cl-1264"></a>      <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;predicates:&#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1265"></a>      <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1266"></a>      <span class="k">for</span> <span class="n">predicate</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="p">:</span>
<a name="cl-1267"></a>        <span class="n">t</span><span class="o">+=</span><span class="n">predicate</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-1268"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1269"></a>
<a name="cl-1270"></a>  <span class="nd">@classmethod</span>
<a name="cl-1271"></a>  <span class="k">def</span> <span class="nf">root</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
<a name="cl-1272"></a>    <span class="k">return</span> <span class="n">FunctionCall</span><span class="p">(</span><span class="s">&#39;root-node&#39;</span><span class="p">)</span>
<a name="cl-1273"></a>  
<a name="cl-1274"></a>  <span class="nd">@classmethod</span>
<a name="cl-1275"></a>  <span class="k">def</span> <span class="nf">context</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
<a name="cl-1276"></a>    <span class="k">return</span> <span class="n">FunctionCall</span><span class="p">(</span><span class="s">&#39;context-node&#39;</span><span class="p">)</span>
<a name="cl-1277"></a>  
<a name="cl-1278"></a>  <span class="nd">@classmethod</span>
<a name="cl-1279"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1280"></a>    <span class="n">token</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span>
<a name="cl-1281"></a>    <span class="n">ch</span><span class="o">=</span><span class="n">token</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">1</span><span class="p">]</span>
<a name="cl-1282"></a>    
<a name="cl-1283"></a>    <span class="k">if</span> <span class="n">ch</span><span class="o">==</span><span class="s">&#39;$&#39;</span><span class="p">:</span>
<a name="cl-1284"></a>      <span class="n">expr</span><span class="o">=</span><span class="n">VariableReference</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1285"></a>    <span class="k">elif</span> <span class="n">ch</span><span class="o">==</span><span class="s">&#39;(&#39;</span><span class="p">:</span>
<a name="cl-1286"></a>      <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1287"></a>      <span class="n">expr</span><span class="o">=</span><span class="n">BinaryExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1288"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-1289"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;unclosed &quot;(&quot;&#39;</span><span class="p">)</span>
<a name="cl-1290"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span><span class="o">!=</span><span class="s">&#39;)&#39;</span><span class="p">:</span>
<a name="cl-1291"></a>        <span class="n">lexer</span><span class="o">.</span><span class="n">back</span><span class="p">()</span>
<a name="cl-1292"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad token: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()))</span>
<a name="cl-1293"></a>    <span class="k">elif</span> <span class="n">ch</span><span class="o">==</span><span class="s">&#39;&quot;&#39;</span> <span class="ow">or</span> <span class="n">ch</span><span class="o">==</span><span class="s">&quot;&#39;&quot;</span><span class="p">:</span>
<a name="cl-1294"></a>      <span class="n">expr</span><span class="o">=</span><span class="n">Literal</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1295"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1296"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">isNaN</span><span class="p">(</span><span class="n">token</span><span class="p">):</span>
<a name="cl-1297"></a>        <span class="n">expr</span><span class="o">=</span><span class="n">Number</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1298"></a>      <span class="k">elif</span> <span class="n">NodeType</span><span class="o">.</span><span class="n">types</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">token</span><span class="p">):</span>
<a name="cl-1299"></a>        <span class="k">return</span> <span class="bp">None</span>
<a name="cl-1300"></a>      <span class="k">elif</span> <span class="n">re_has_ualpha</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">ch</span><span class="p">)</span> <span class="ow">and</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;(&#39;</span><span class="p">:</span>
<a name="cl-1301"></a>        <span class="n">expr</span><span class="o">=</span><span class="n">FunctionCall</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1302"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-1303"></a>        <span class="k">return</span> <span class="bp">None</span>
<a name="cl-1304"></a>    
<a name="cl-1305"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span><span class="o">!=</span><span class="s">&#39;[&#39;</span><span class="p">:</span>
<a name="cl-1306"></a>      <span class="k">return</span> <span class="n">expr</span>
<a name="cl-1307"></a>    
<a name="cl-1308"></a>    <span class="nb">filter</span><span class="o">=</span><span class="n">FilterExpr</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-1309"></a>    
<a name="cl-1310"></a>    <span class="n">BaseExprHasPredicates</span><span class="o">.</span><span class="n">parsePredicates</span><span class="p">(</span><span class="n">lexer</span><span class="p">,</span><span class="nb">filter</span><span class="p">)</span>
<a name="cl-1311"></a>    
<a name="cl-1312"></a>    <span class="k">return</span> <span class="nb">filter</span>
<a name="cl-1313"></a>
<a name="cl-1314"></a><span class="c">#} // end of FilterExpr</span>
<a name="cl-1315"></a>
<a name="cl-1316"></a>
<a name="cl-1317"></a><span class="c">#{ // Step</span>
<a name="cl-1318"></a><span class="k">class</span> <span class="nc">Step</span><span class="p">(</span><span class="n">BaseExprHasPredicates</span><span class="p">):</span>
<a name="cl-1319"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">axis</span><span class="p">,</span><span class="n">test</span><span class="p">):</span>
<a name="cl-1320"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">axis</span><span class="o">=</span><span class="n">axis</span>
<a name="cl-1321"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">reverse</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">axises</span><span class="p">[</span><span class="n">axis</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-1322"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">func</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">axises</span><span class="p">[</span><span class="n">axis</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
<a name="cl-1323"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="o">=</span><span class="n">test</span>
<a name="cl-1324"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-1325"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">_quickAttr</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">axises</span><span class="p">[</span><span class="n">axis</span><span class="p">][</span><span class="mi">2</span><span class="p">]</span>
<a name="cl-1326"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">quickAttr</span><span class="o">=</span><span class="bp">False</span>
<a name="cl-1327"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="bp">False</span>
<a name="cl-1328"></a>  
<a name="cl-1329"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">,</span><span class="n">special</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span><span class="n">prevNodeset</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span><span class="n">prevIndex</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1330"></a>    <span class="n">node</span><span class="o">=</span><span class="n">ctx</span><span class="o">.</span><span class="n">node</span>
<a name="cl-1331"></a>    <span class="n">reverse</span><span class="o">=</span><span class="bp">False</span>
<a name="cl-1332"></a>
<a name="cl-1333"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">special</span> <span class="ow">and</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;op&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;//&#39;</span><span class="p">:</span>
<a name="cl-1334"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">axis</span><span class="o">==</span><span class="s">&#39;child&#39;</span><span class="p">:</span>
<a name="cl-1335"></a>        <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;quickAttr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1336"></a>          <span class="n">attrValueExpr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;attrValueExpr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1337"></a>          <span class="n">attrValue</span><span class="o">=</span><span class="n">attrValueExpr</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span> <span class="k">if</span> <span class="n">attrValueExpr</span> <span class="k">else</span> <span class="bp">None</span>
<a name="cl-1338"></a>          <span class="n">nodeset</span><span class="o">=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">getDescendantNodes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">NodeSet</span><span class="p">(),</span><span class="bp">self</span><span class="o">.</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-1339"></a>          <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluatePredicates</span><span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-1340"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-1341"></a>          <span class="n">nodeset</span><span class="o">=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">getDescendantNodes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">NodeSet</span><span class="p">(),</span><span class="bp">None</span><span class="p">,</span><span class="bp">None</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-1342"></a>          <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluatePredicates</span><span class="p">(</span><span class="n">nodeset</span><span class="p">)</span>
<a name="cl-1343"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-1344"></a>        <span class="n">step</span><span class="o">=</span><span class="n">Step</span><span class="p">(</span><span class="s">&#39;descendant-or-self&#39;</span><span class="p">,</span><span class="n">NodeType</span><span class="p">(</span><span class="s">&#39;node&#39;</span><span class="p">))</span>
<a name="cl-1345"></a>        <span class="n">nodes</span><span class="o">=</span><span class="n">step</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">,</span><span class="bp">False</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span><span class="o">.</span><span class="n">list</span><span class="p">()</span>
<a name="cl-1346"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-1347"></a>        <span class="n">step</span><span class="o">.</span><span class="n">op</span><span class="o">=</span><span class="s">&#39;/&#39;</span>
<a name="cl-1348"></a>        <span class="k">for</span> <span class="n">_node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-1349"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">nodeset</span><span class="p">:</span>
<a name="cl-1350"></a>            <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">Ctx</span><span class="p">(</span><span class="n">_node</span><span class="p">),</span><span class="bp">True</span><span class="p">,</span><span class="bp">None</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1351"></a>          <span class="k">else</span><span class="p">:</span>
<a name="cl-1352"></a>            <span class="n">nodeset</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">Ctx</span><span class="p">(</span><span class="n">_node</span><span class="p">),</span><span class="bp">True</span><span class="p">,</span><span class="bp">None</span><span class="p">,</span><span class="bp">None</span><span class="p">))</span>
<a name="cl-1353"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="n">nodeset</span> <span class="ow">or</span> <span class="n">NodeSet</span><span class="p">()</span>
<a name="cl-1354"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1355"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;needContextPosition&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1356"></a>        <span class="n">prevNodeset</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-1357"></a>        <span class="n">prevIndex</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-1358"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;quickAttr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1359"></a>        <span class="n">attrValueExpr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;attrValueExpr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1360"></a>        <span class="n">attrValue</span><span class="o">=</span><span class="n">attrValueExpr</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span> <span class="k">if</span> <span class="n">attrValueExpr</span> <span class="k">else</span> <span class="bp">None</span>
<a name="cl-1361"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">func</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">NodeSet</span><span class="p">(),</span><span class="bp">self</span><span class="o">.</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-1362"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluatePredicates</span><span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-1363"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-1364"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">func</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">NodeSet</span><span class="p">(),</span><span class="bp">None</span><span class="p">,</span><span class="bp">None</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-1365"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluatePredicates</span><span class="p">(</span><span class="n">nodeset</span><span class="p">)</span>
<a name="cl-1366"></a>      <span class="k">if</span> <span class="n">prevNodeset</span><span class="p">:</span>
<a name="cl-1367"></a>        <span class="n">prevNodeset</span><span class="o">.</span><span class="n">doDel</span><span class="p">()</span>
<a name="cl-1368"></a>    
<a name="cl-1369"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1370"></a>  
<a name="cl-1371"></a>  <span class="k">def</span> <span class="nf">predicate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">predicate</span><span class="p">):</span>
<a name="cl-1372"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">predicate</span><span class="p">)</span>
<a name="cl-1373"></a>    <span class="n">datatype</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span><span class="s">&#39;datatype&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1374"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span><span class="s">&#39;needContextPosition&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">or</span> <span class="n">datatype</span><span class="o">==</span><span class="s">&#39;number&#39;</span> <span class="ow">or</span> <span class="n">datatype</span><span class="o">==</span><span class="s">&#39;void&#39;</span><span class="p">:</span>
<a name="cl-1375"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-1376"></a>    
<a name="cl-1377"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;_quickAttr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="p">)</span><span class="o">==</span><span class="mi">1</span> <span class="ow">and</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span><span class="s">&#39;quickAttr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1378"></a>      <span class="n">attrName</span><span class="o">=</span><span class="n">predicate</span><span class="o">.</span><span class="n">attrName</span>
<a name="cl-1379"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">attrName</span><span class="o">=</span><span class="n">attrName</span>
<a name="cl-1380"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">attrValueExpr</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span><span class="s">&#39;attrValueExpr&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1381"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">quickAttr</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-1382"></a>  
<a name="cl-1383"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1384"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1385"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;step: &#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1386"></a>    <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1387"></a>    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">axis</span><span class="p">:</span>
<a name="cl-1388"></a>      <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;axis: &#39;</span><span class="o">+</span><span class="bp">self</span><span class="o">.</span><span class="n">axis</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1389"></a>    <span class="n">t</span><span class="o">+=</span><span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-1390"></a>    <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="p">):</span>
<a name="cl-1391"></a>      <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;predicates:&#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1392"></a>      <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1393"></a>      <span class="k">for</span> <span class="n">predicate</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">predicates</span><span class="p">:</span>
<a name="cl-1394"></a>        <span class="n">t</span><span class="o">+=</span><span class="n">predicate</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-1395"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1396"></a>  
<a name="cl-1397"></a>  <span class="c"># --- Local Functions</span>
<a name="cl-1398"></a>  <span class="k">def</span> <span class="nf">_ancestor</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1399"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1400"></a>      <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-1401"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-1402"></a>        <span class="k">break</span>
<a name="cl-1403"></a>      <span class="k">if</span> <span class="n">prevNodeset</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span><span class="p">:</span>
<a name="cl-1404"></a>        <span class="n">prevNodeset</span><span class="o">.</span><span class="n">reserveDelByNode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">,</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-1405"></a>      <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1406"></a>        <span class="n">nodeset</span><span class="o">.</span><span class="n">unshift</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1407"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1408"></a>  
<a name="cl-1409"></a>  <span class="k">def</span> <span class="nf">_ancestorOrSelf</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1410"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1411"></a>      <span class="k">if</span> <span class="n">prevNodeset</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span><span class="p">:</span>
<a name="cl-1412"></a>        <span class="n">prevNodeset</span><span class="o">.</span><span class="n">reserveDelByNode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">,</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-1413"></a>      <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1414"></a>        <span class="n">nodeset</span><span class="o">.</span><span class="n">unshift</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1415"></a>      <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-1416"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-1417"></a>        <span class="k">break</span>
<a name="cl-1418"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1419"></a>  
<a name="cl-1420"></a>  <span class="k">def</span> <span class="nf">_attribute</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1421"></a>    <span class="n">attrs</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">attributes</span>
<a name="cl-1422"></a>    <span class="k">if</span> <span class="n">attrs</span><span class="p">:</span>
<a name="cl-1423"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="s">&#39;notOnlyElement&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">and</span> <span class="n">test</span><span class="o">.</span><span class="n">type</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ANY_NODE</span> <span class="ow">or</span> <span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="o">==</span><span class="s">&#39;*&#39;</span><span class="p">:</span>
<a name="cl-1424"></a>        <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">attrs</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span>
<a name="cl-1425"></a>          <span class="c">#nodeset.push(AttributeWrapper(name,attrs[name],node))</span>
<a name="cl-1426"></a>          <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">AttributeWrapper</span><span class="o">.</span><span class="n">getAttributeWrapper</span><span class="p">(</span><span class="n">name</span><span class="p">,</span><span class="n">attrs</span><span class="p">[</span><span class="n">name</span><span class="p">],</span><span class="n">node</span><span class="p">))</span>
<a name="cl-1427"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-1428"></a>        <span class="n">attr</span><span class="o">=</span><span class="n">attrs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<a name="cl-1429"></a>        <span class="k">if</span> <span class="n">attr</span><span class="o">!=</span><span class="bp">None</span><span class="p">:</span>
<a name="cl-1430"></a>          <span class="c">#nodeset.push(AttributeWrapper(test.name,attr,node))</span>
<a name="cl-1431"></a>          <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">AttributeWrapper</span><span class="o">.</span><span class="n">getAttributeWrapper</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">,</span><span class="n">attr</span><span class="p">,</span><span class="n">node</span><span class="p">))</span>
<a name="cl-1432"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1433"></a>  
<a name="cl-1434"></a>  <span class="k">def</span> <span class="nf">_child</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1435"></a>    <span class="k">return</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">getChildNodes</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-1436"></a>  
<a name="cl-1437"></a>  <span class="k">def</span> <span class="nf">_descendant</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1438"></a>    <span class="k">return</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">getDescendantNodes</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-1439"></a>  
<a name="cl-1440"></a>  <span class="k">def</span> <span class="nf">_descendantOrSelf</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1441"></a>    <span class="k">if</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">attrMatch</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">)</span> <span class="ow">and</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1442"></a>      <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1443"></a>    <span class="k">return</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">getDescendantNodes</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-1444"></a>  
<a name="cl-1445"></a>  <span class="k">def</span> <span class="nf">_following</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1446"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1447"></a>      <span class="n">child</span><span class="o">=</span><span class="n">node</span>
<a name="cl-1448"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1449"></a>        <span class="n">child</span><span class="o">=</span><span class="n">child</span><span class="o">.</span><span class="n">nextSibling</span>
<a name="cl-1450"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">child</span><span class="p">:</span>
<a name="cl-1451"></a>          <span class="k">break</span>
<a name="cl-1452"></a>        <span class="k">if</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">attrMatch</span><span class="p">(</span><span class="n">child</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">)</span> <span class="ow">and</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">child</span><span class="p">):</span>
<a name="cl-1453"></a>          <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">child</span><span class="p">)</span>
<a name="cl-1454"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">getDescendantNodes</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">child</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="bp">None</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1455"></a>      <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-1456"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-1457"></a>        <span class="k">break</span>
<a name="cl-1458"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1459"></a>  
<a name="cl-1460"></a>  <span class="k">def</span> <span class="nf">_followingSibling</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1461"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1462"></a>      <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">nextSibling</span>
<a name="cl-1463"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-1464"></a>        <span class="k">break</span>
<a name="cl-1465"></a>      <span class="k">if</span> <span class="n">prevNodeset</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span><span class="p">:</span>
<a name="cl-1466"></a>        <span class="n">prevNodeset</span><span class="o">.</span><span class="n">reserveDelByNode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">)</span>
<a name="cl-1467"></a>      <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1468"></a>        <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1469"></a>    <span class="k">return</span> <span class="n">nodeset</span><span class="p">;</span>
<a name="cl-1470"></a>  
<a name="cl-1471"></a>  <span class="k">def</span> <span class="nf">_namespace</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1472"></a>    <span class="c"># not implemented</span>
<a name="cl-1473"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1474"></a>  
<a name="cl-1475"></a>  <span class="k">def</span> <span class="nf">_parent</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1476"></a>    <span class="n">nodeType</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">nodeType</span>
<a name="cl-1477"></a>    <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span><span class="p">:</span>
<a name="cl-1478"></a>      <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1479"></a>    <span class="k">if</span> <span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-1480"></a>      <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">ownerElement</span><span class="p">)</span>
<a name="cl-1481"></a>      <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1482"></a>    <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-1483"></a>    <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1484"></a>      <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1485"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1486"></a>  
<a name="cl-1487"></a>  <span class="k">def</span> <span class="nf">_preceding</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1488"></a>    <span class="n">parents</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-1489"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1490"></a>      <span class="n">parents</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1491"></a>      <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-1492"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-1493"></a>        <span class="k">break</span>
<a name="cl-1494"></a>    
<a name="cl-1495"></a>    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">parents</span><span class="p">[</span><span class="mi">1</span><span class="p">:]:</span>
<a name="cl-1496"></a>      <span class="n">siblings</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-1497"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1498"></a>        <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">previousSibling</span>
<a name="cl-1499"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-1500"></a>          <span class="k">break</span>
<a name="cl-1501"></a>        <span class="n">siblings</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1502"></a>      
<a name="cl-1503"></a>      <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">siblings</span><span class="p">:</span>
<a name="cl-1504"></a>        <span class="k">if</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">attrMatch</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">)</span> <span class="ow">and</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1505"></a>          <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1506"></a>        <span class="n">nodeset</span><span class="o">=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">getDescendantNodes</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="bp">None</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-1507"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1508"></a>  
<a name="cl-1509"></a>  <span class="k">def</span> <span class="nf">_precedingSibling</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1510"></a>    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-1511"></a>      <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">previousSibling</span>
<a name="cl-1512"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-1513"></a>        <span class="k">break</span>
<a name="cl-1514"></a>      <span class="k">if</span> <span class="n">prevNodeset</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span><span class="p">:</span>
<a name="cl-1515"></a>        <span class="n">prevNodeset</span><span class="o">.</span><span class="n">reserveDelByNode</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">,</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-1516"></a>      <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1517"></a>        <span class="n">nodeset</span><span class="o">.</span><span class="n">unshift</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1518"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1519"></a>  
<a name="cl-1520"></a>  <span class="k">def</span> <span class="nf">_self</span><span class="p">(</span><span class="n">test</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">nodeset</span><span class="p">,</span><span class="n">attrName</span><span class="p">,</span><span class="n">attrValue</span><span class="p">,</span><span class="n">prevNodeset</span><span class="p">,</span><span class="n">prevIndex</span><span class="p">):</span>
<a name="cl-1521"></a>    <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1522"></a>      <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1523"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1524"></a>  
<a name="cl-1525"></a>  <span class="n">axises</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-1526"></a>    <span class="s">&#39;ancestor&#39;</span>          <span class="p">:[</span><span class="bp">True</span> <span class="p">,</span><span class="n">_ancestor</span>        <span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1527"></a>  <span class="p">,</span> <span class="s">&#39;ancestor-or-self&#39;</span>  <span class="p">:[</span><span class="bp">True</span> <span class="p">,</span><span class="n">_ancestorOrSelf</span>  <span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1528"></a>  <span class="p">,</span> <span class="s">&#39;attribute&#39;</span>         <span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_attribute</span>       <span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1529"></a>  <span class="p">,</span> <span class="s">&#39;child&#39;</span>             <span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_child</span><span class="p">,</span><span class="bp">True</span>      <span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1530"></a>  <span class="p">,</span> <span class="s">&#39;descendant&#39;</span>        <span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_descendant</span>      <span class="p">,</span><span class="bp">True</span> <span class="p">]</span>
<a name="cl-1531"></a>  <span class="p">,</span> <span class="s">&#39;descendant-or-self&#39;</span><span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_descendantOrSelf</span><span class="p">,</span><span class="bp">True</span> <span class="p">]</span>
<a name="cl-1532"></a>  <span class="p">,</span> <span class="s">&#39;following&#39;</span>         <span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_following</span>       <span class="p">,</span><span class="bp">True</span> <span class="p">]</span>
<a name="cl-1533"></a>  <span class="p">,</span> <span class="s">&#39;following-sibling&#39;</span> <span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_followingSibling</span><span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1534"></a>  <span class="p">,</span> <span class="s">&#39;namespace&#39;</span>         <span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_namespace</span>       <span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1535"></a>  <span class="p">,</span> <span class="s">&#39;parent&#39;</span>            <span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_parent</span>          <span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1536"></a>  <span class="p">,</span> <span class="s">&#39;preceding&#39;</span>         <span class="p">:[</span><span class="bp">True</span> <span class="p">,</span><span class="n">_preceding</span>       <span class="p">,</span><span class="bp">True</span> <span class="p">]</span>
<a name="cl-1537"></a>  <span class="p">,</span> <span class="s">&#39;preceding-sibling&#39;</span> <span class="p">:[</span><span class="bp">True</span> <span class="p">,</span><span class="n">_precedingSibling</span><span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1538"></a>  <span class="p">,</span> <span class="s">&#39;self&#39;</span>              <span class="p">:[</span><span class="bp">False</span><span class="p">,</span><span class="n">_self</span>            <span class="p">,</span><span class="bp">False</span><span class="p">]</span>
<a name="cl-1539"></a>  <span class="p">})</span>
<a name="cl-1540"></a>  
<a name="cl-1541"></a>  <span class="nd">@classmethod</span>
<a name="cl-1542"></a>  <span class="k">def</span> <span class="nf">_cself</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
<a name="cl-1543"></a>    <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="s">&#39;self&#39;</span><span class="p">,</span><span class="n">NodeType</span><span class="p">(</span><span class="s">&#39;node&#39;</span><span class="p">))</span>
<a name="cl-1544"></a>  
<a name="cl-1545"></a>  <span class="nd">@classmethod</span>
<a name="cl-1546"></a>  <span class="k">def</span> <span class="nf">parent</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
<a name="cl-1547"></a>    <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="s">&#39;parent&#39;</span><span class="p">,</span><span class="n">NodeType</span><span class="p">(</span><span class="s">&#39;node&#39;</span><span class="p">))</span>
<a name="cl-1548"></a>  
<a name="cl-1549"></a>  <span class="nd">@classmethod</span>
<a name="cl-1550"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1551"></a>    <span class="p">(</span><span class="n">parent</span><span class="p">,</span><span class="n">_cself</span><span class="p">,</span><span class="n">axises</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">cls</span><span class="o">.</span><span class="n">parent</span><span class="p">,</span><span class="n">cls</span><span class="o">.</span><span class="n">_cself</span><span class="p">,</span><span class="n">cls</span><span class="o">.</span><span class="n">axises</span><span class="p">)</span>
<a name="cl-1552"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span><span class="o">==</span><span class="s">&#39;.&#39;</span><span class="p">:</span>
<a name="cl-1553"></a>      <span class="n">step</span><span class="o">=</span><span class="n">_cself</span><span class="p">()</span>
<a name="cl-1554"></a>      <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1555"></a>    <span class="k">elif</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span><span class="o">==</span><span class="s">&#39;..&#39;</span><span class="p">:</span>
<a name="cl-1556"></a>      <span class="n">step</span><span class="o">=</span><span class="n">parent</span><span class="p">()</span>
<a name="cl-1557"></a>      <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1558"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1559"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span><span class="o">==</span><span class="s">&#39;@&#39;</span><span class="p">:</span>
<a name="cl-1560"></a>        <span class="n">axis</span><span class="o">=</span><span class="s">&#39;attribute&#39;</span>
<a name="cl-1561"></a>        <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1562"></a>        <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-1563"></a>          <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;missing attribute name&#39;</span><span class="p">)</span>
<a name="cl-1564"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-1565"></a>        <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;::&#39;</span><span class="p">:</span>
<a name="cl-1566"></a>          <span class="n">ch</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()[</span><span class="mi">0</span><span class="p">:</span><span class="mi">1</span><span class="p">]</span>
<a name="cl-1567"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">re_has_ualpha</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">ch</span><span class="p">):</span>
<a name="cl-1568"></a>            <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad token: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()))</span>
<a name="cl-1569"></a>          
<a name="cl-1570"></a>          <span class="n">axis</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1571"></a>          <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1572"></a>          
<a name="cl-1573"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">axises</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">axis</span><span class="p">):</span>
<a name="cl-1574"></a>            <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;invalid axis: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">axis</span><span class="p">))</span>
<a name="cl-1575"></a>          
<a name="cl-1576"></a>          <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-1577"></a>            <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;missing node name&#39;</span><span class="p">)</span>
<a name="cl-1578"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-1579"></a>          <span class="n">axis</span><span class="o">=</span><span class="s">&#39;child&#39;</span>
<a name="cl-1580"></a>      
<a name="cl-1581"></a>      <span class="n">token</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span>
<a name="cl-1582"></a>      <span class="n">ch</span><span class="o">=</span><span class="n">token</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">1</span><span class="p">]</span>
<a name="cl-1583"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">re_has_ualpha</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">ch</span><span class="p">):</span>
<a name="cl-1584"></a>        <span class="k">if</span> <span class="n">token</span><span class="o">==</span><span class="s">&#39;*&#39;</span><span class="p">:</span>
<a name="cl-1585"></a>          <span class="n">test</span><span class="o">=</span><span class="n">NameTest</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1586"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-1587"></a>          <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad token: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()))</span>
<a name="cl-1588"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-1589"></a>        <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;(&#39;</span><span class="p">:</span>
<a name="cl-1590"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">NodeType</span><span class="o">.</span><span class="n">types</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">token</span><span class="p">):</span>
<a name="cl-1591"></a>            <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;invalid node type: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">token</span><span class="p">))</span>
<a name="cl-1592"></a>          <span class="n">test</span><span class="o">=</span><span class="n">NodeType</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1593"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-1594"></a>          <span class="n">test</span><span class="o">=</span><span class="n">NameTest</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1595"></a>      <span class="n">step</span><span class="o">=</span><span class="n">Step</span><span class="p">(</span><span class="n">axis</span><span class="p">,</span><span class="n">test</span><span class="p">)</span>
<a name="cl-1596"></a>    
<a name="cl-1597"></a>    <span class="n">BaseExprHasPredicates</span><span class="o">.</span><span class="n">parsePredicates</span><span class="p">(</span><span class="n">lexer</span><span class="p">,</span><span class="n">step</span><span class="p">)</span>
<a name="cl-1598"></a>    
<a name="cl-1599"></a>    <span class="k">return</span> <span class="n">step</span>
<a name="cl-1600"></a>
<a name="cl-1601"></a><span class="c">#} // end of Step</span>
<a name="cl-1602"></a>
<a name="cl-1603"></a>
<a name="cl-1604"></a><span class="c">#{ // NodeType</span>
<a name="cl-1605"></a><span class="k">class</span> <span class="nc">NodeType</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1606"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">,</span><span class="n">literal</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1607"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">=</span><span class="n">name</span>
<a name="cl-1608"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">literal</span><span class="o">=</span><span class="n">literal</span>
<a name="cl-1609"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="o">=</span><span class="n">NodeType</span><span class="o">.</span><span class="n">typeNums</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">,</span><span class="n">NodeType</span><span class="o">.</span><span class="n">typeNums</span><span class="o">.</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1610"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">notOnlyElement</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-1611"></a>  
<a name="cl-1612"></a>  <span class="k">def</span> <span class="nf">match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1613"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ANY_NODE</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="o">==</span><span class="n">node</span><span class="o">.</span><span class="n">nodeType</span>
<a name="cl-1614"></a>  
<a name="cl-1615"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1616"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1617"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;nodetype: &#39;</span><span class="o">+</span><span class="n">toString</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1618"></a>    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">literal</span><span class="p">:</span>
<a name="cl-1619"></a>      <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1620"></a>      <span class="n">t</span><span class="o">+=</span><span class="bp">self</span><span class="o">.</span><span class="n">literal</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-1621"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1622"></a>  
<a name="cl-1623"></a>  <span class="n">types</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-1624"></a>    <span class="s">&#39;comment&#39;</span>               <span class="p">:</span><span class="mi">1</span>
<a name="cl-1625"></a>  <span class="p">,</span> <span class="s">&#39;text&#39;</span>                  <span class="p">:</span><span class="mi">1</span>
<a name="cl-1626"></a>  <span class="p">,</span> <span class="s">&#39;processing-instruction&#39;</span><span class="p">:</span><span class="mi">1</span>
<a name="cl-1627"></a>  <span class="p">,</span> <span class="s">&#39;node&#39;</span>                  <span class="p">:</span><span class="mi">1</span>
<a name="cl-1628"></a>  <span class="p">})</span>
<a name="cl-1629"></a>  
<a name="cl-1630"></a>  <span class="n">typeNums</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-1631"></a>    <span class="s">&#39;comment&#39;</span>               <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">COMMENT_NODE</span>
<a name="cl-1632"></a>  <span class="p">,</span> <span class="s">&#39;text&#39;</span>                  <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">TEXT_NODE</span>
<a name="cl-1633"></a>  <span class="p">,</span> <span class="s">&#39;processing-instruction&#39;</span><span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">PROCESSING_INSTRUCTION_NODE</span>
<a name="cl-1634"></a>  <span class="p">,</span> <span class="s">&#39;node&#39;</span>                  <span class="p">:</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ANY_NODE</span>
<a name="cl-1635"></a>  <span class="p">})</span>
<a name="cl-1636"></a>  
<a name="cl-1637"></a>  <span class="nd">@classmethod</span>
<a name="cl-1638"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1639"></a>    <span class="nb">type</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1640"></a>    <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1641"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-1642"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad nodetype&#39;</span><span class="p">)</span>
<a name="cl-1643"></a>    <span class="n">ch</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()[</span><span class="mi">0</span><span class="p">:</span><span class="mi">1</span><span class="p">]</span>
<a name="cl-1644"></a>    <span class="n">literal</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-1645"></a>    <span class="k">if</span> <span class="n">ch</span><span class="o">==</span><span class="s">&#39;&quot;&#39;</span> <span class="ow">or</span> <span class="n">ch</span><span class="o">==</span><span class="s">&quot;&#39;&quot;</span><span class="p">:</span>
<a name="cl-1646"></a>      <span class="n">literal</span><span class="o">=</span><span class="n">Literal</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-1647"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-1648"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad nodetype&#39;</span><span class="p">)</span>
<a name="cl-1649"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span><span class="o">!=</span><span class="s">&#39;)&#39;</span><span class="p">:</span>
<a name="cl-1650"></a>      <span class="n">lexer</span><span class="o">.</span><span class="n">back</span><span class="p">()</span>
<a name="cl-1651"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad token: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()))</span>
<a name="cl-1652"></a>    
<a name="cl-1653"></a>    <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="nb">type</span><span class="p">,</span><span class="n">literal</span><span class="p">)</span>
<a name="cl-1654"></a>
<a name="cl-1655"></a><span class="c">#} // end of NodeType</span>
<a name="cl-1656"></a>
<a name="cl-1657"></a>
<a name="cl-1658"></a><span class="c">#{ // NameTest</span>
<a name="cl-1659"></a><span class="k">class</span> <span class="nc">NameTest</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1660"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-1661"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<a name="cl-1662"></a>  
<a name="cl-1663"></a>  <span class="k">def</span> <span class="nf">match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">):</span>
<a name="cl-1664"></a>    <span class="nb">type</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">nodeType</span>
<a name="cl-1665"></a>    <span class="k">if</span> <span class="nb">type</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span> <span class="ow">or</span> <span class="nb">type</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span>
<a name="cl-1666"></a>      <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">==</span><span class="s">&#39;*&#39;</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">==</span><span class="n">node</span><span class="o">.</span><span class="n">nodeName</span><span class="p">:</span>
<a name="cl-1667"></a>        <span class="k">return</span> <span class="bp">True</span>
<a name="cl-1668"></a>    <span class="k">return</span> <span class="bp">False</span>
<a name="cl-1669"></a>  
<a name="cl-1670"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1671"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1672"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;nametest: &#39;</span><span class="o">+</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1673"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1674"></a>  
<a name="cl-1675"></a>  <span class="nd">@classmethod</span>
<a name="cl-1676"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1677"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span><span class="o">!=</span> <span class="s">&#39;*&#39;</span> <span class="ow">and</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;:&#39;</span> <span class="ow">and</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span><span class="o">==</span><span class="s">&#39;*&#39;</span><span class="p">:</span>
<a name="cl-1678"></a>      <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span><span class="o">+</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span><span class="o">+</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">())</span>
<a name="cl-1679"></a>    <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">())</span>
<a name="cl-1680"></a>
<a name="cl-1681"></a><span class="c">#} // end of NameTest</span>
<a name="cl-1682"></a>
<a name="cl-1683"></a>
<a name="cl-1684"></a><span class="c">#{ // VariableReference</span>
<a name="cl-1685"></a><span class="k">class</span> <span class="nc">VariableReference</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1686"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-1687"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<a name="cl-1688"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">datatype</span><span class="o">=</span><span class="s">&#39;void&#39;</span>
<a name="cl-1689"></a>  
<a name="cl-1690"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1691"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1692"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;variable: &#39;</span><span class="o">+</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1693"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1694"></a>  
<a name="cl-1695"></a>  <span class="nd">@classmethod</span>
<a name="cl-1696"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1697"></a>      <span class="n">token</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1698"></a>      <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">token</span><span class="p">)</span><span class="o">&lt;</span><span class="mi">2</span><span class="p">:</span>
<a name="cl-1699"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;unnamed variable reference&#39;</span><span class="p">)</span>
<a name="cl-1700"></a>      <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">token</span><span class="p">)</span>
<a name="cl-1701"></a>
<a name="cl-1702"></a><span class="c">#} // end of VariableReference</span>
<a name="cl-1703"></a>
<a name="cl-1704"></a>
<a name="cl-1705"></a><span class="c">#{ // Literal</span>
<a name="cl-1706"></a><span class="k">class</span> <span class="nc">Literal</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1707"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">text</span><span class="p">):</span>
<a name="cl-1708"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<a name="cl-1709"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">datatype</span><span class="o">=</span><span class="s">&#39;string&#39;</span>
<a name="cl-1710"></a>  
<a name="cl-1711"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-1712"></a>    <span class="n">result</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span>
<a name="cl-1713"></a>    <span class="k">return</span> <span class="n">result</span>
<a name="cl-1714"></a>  
<a name="cl-1715"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1716"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1717"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;literal: &#39;</span><span class="o">+</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1718"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1719"></a>  
<a name="cl-1720"></a>  <span class="nd">@classmethod</span>
<a name="cl-1721"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1722"></a>    <span class="n">token</span><span class="o">=</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-1723"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">token</span><span class="p">)</span><span class="o">&lt;</span><span class="mi">2</span><span class="p">:</span>
<a name="cl-1724"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;unclosed literal string&#39;</span><span class="p">)</span>
<a name="cl-1725"></a>    <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">token</span><span class="p">)</span>
<a name="cl-1726"></a>
<a name="cl-1727"></a><span class="c">#} // end of Literal</span>
<a name="cl-1728"></a>
<a name="cl-1729"></a>
<a name="cl-1730"></a><span class="c">#{ // Number</span>
<a name="cl-1731"></a><span class="k">class</span> <span class="nc">Number</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1732"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">digit</span><span class="p">):</span>
<a name="cl-1733"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">digit</span><span class="o">=</span><span class="n">toNumber</span><span class="p">(</span><span class="n">digit</span><span class="p">)</span>
<a name="cl-1734"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">datatype</span><span class="o">=</span><span class="s">&#39;number&#39;</span>
<a name="cl-1735"></a>  
<a name="cl-1736"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-1737"></a>    <span class="n">result</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">digit</span>
<a name="cl-1738"></a>    <span class="k">return</span> <span class="n">result</span>
<a name="cl-1739"></a>  
<a name="cl-1740"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1741"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1742"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;number: &#39;</span><span class="o">+</span><span class="n">toString</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">digit</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1743"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1744"></a>  
<a name="cl-1745"></a>  <span class="nd">@classmethod</span>
<a name="cl-1746"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-1747"></a>    <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">())</span>
<a name="cl-1748"></a>
<a name="cl-1749"></a><span class="c">#} // end of Number</span>
<a name="cl-1750"></a>
<a name="cl-1751"></a>
<a name="cl-1752"></a><span class="c">#{ // FunctionCall</span>
<a name="cl-1753"></a><span class="k">class</span> <span class="nc">FunctionCall</span><span class="p">(</span><span class="n">BaseExpr</span><span class="p">):</span>
<a name="cl-1754"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">name</span><span class="p">):</span>
<a name="cl-1755"></a>    <span class="n">info</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">funcs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
<a name="cl-1756"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">info</span><span class="p">:</span>
<a name="cl-1757"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;</span><span class="si">%s</span><span class="s"> is not a function&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">))</span>
<a name="cl-1758"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">=</span><span class="n">name</span>
<a name="cl-1759"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">func</span><span class="o">=</span><span class="n">info</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-1760"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-1761"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">datatype</span><span class="o">=</span><span class="n">info</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<a name="cl-1762"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="bp">True</span> <span class="k">if</span> <span class="n">info</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="k">else</span> <span class="bp">False</span>
<a name="cl-1763"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextNodeInfo</span><span class="o">=</span><span class="n">info</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
<a name="cl-1764"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">needContextNode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">needContextNodeInfo</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">needContextNodeInfo</span><span class="p">)</span> <span class="k">else</span> <span class="bp">False</span>
<a name="cl-1765"></a>  
<a name="cl-1766"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">ctx</span><span class="p">):</span>
<a name="cl-1767"></a>    <span class="n">result</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">func</span><span class="p">(</span><span class="n">ctx</span><span class="p">,</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
<a name="cl-1768"></a>    <span class="k">return</span> <span class="n">result</span>
<a name="cl-1769"></a>  
<a name="cl-1770"></a>  <span class="k">def</span> <span class="nf">arg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">arg</span><span class="p">):</span>
<a name="cl-1771"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
<a name="cl-1772"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span><span class="s">&#39;needContextPosition&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1773"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">needContextPosition</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-1774"></a>    <span class="n">args</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span>
<a name="cl-1775"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span><span class="s">&#39;needContextNode&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1776"></a>      <span class="c">#args.needContextNode=True</span>
<a name="cl-1777"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">needContextNode</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-1778"></a>    <span class="c">#self.needContextNode=args.needContextNode or self.needContextNodeInfo[len(args)]</span>
<a name="cl-1779"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;needContextNode&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">needContextNodeInfo</span><span class="p">):</span>
<a name="cl-1780"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">needContextNode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">needContextNodeInfo</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)]</span>
<a name="cl-1781"></a>  
<a name="cl-1782"></a>  <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">indent</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-1783"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1784"></a>    <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;function: &#39;</span><span class="o">+</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1785"></a>    <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1786"></a>    <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">):</span>
<a name="cl-1787"></a>      <span class="n">t</span><span class="o">+=</span><span class="n">indent</span><span class="o">+</span><span class="s">&#39;arguments: &#39;</span><span class="o">+</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span>
<a name="cl-1788"></a>      <span class="n">indent</span><span class="o">+=</span><span class="n">indent_space</span>
<a name="cl-1789"></a>      <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span>
<a name="cl-1790"></a>        <span class="n">t</span><span class="o">+=</span><span class="n">arg</span><span class="o">.</span><span class="n">show</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-1791"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1792"></a>  
<a name="cl-1793"></a>  <span class="c"># --- Local Functions</span>
<a name="cl-1794"></a>  <span class="k">def</span> <span class="nf">_contextNode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1795"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1796"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function context-node expects ()&#39;</span><span class="p">)</span>
<a name="cl-1797"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="n">NodeSet</span><span class="p">()</span>
<a name="cl-1798"></a>    <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1799"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1800"></a>  
<a name="cl-1801"></a>  <span class="k">def</span> <span class="nf">_rootNode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1802"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1803"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function root-node expects ()&#39;</span><span class="p">)</span>
<a name="cl-1804"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="n">NodeSet</span><span class="p">()</span>
<a name="cl-1805"></a>    <span class="n">ctxn</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span>
<a name="cl-1806"></a>    <span class="k">if</span> <span class="n">ctxn</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span><span class="p">:</span>
<a name="cl-1807"></a>      <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">ctxn</span><span class="p">)</span>
<a name="cl-1808"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1809"></a>      <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">ctxn</span><span class="o">.</span><span class="n">ownerDocument</span><span class="p">)</span>
<a name="cl-1810"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1811"></a>  
<a name="cl-1812"></a>  <span class="k">def</span> <span class="nf">_last</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1813"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1814"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function last expects ()&#39;</span><span class="p">)</span>
<a name="cl-1815"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">last</span>
<a name="cl-1816"></a>  
<a name="cl-1817"></a>  <span class="k">def</span> <span class="nf">_position</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1818"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1819"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function position expects ()&#39;</span><span class="p">)</span>
<a name="cl-1820"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">position</span>
<a name="cl-1821"></a>  
<a name="cl-1822"></a>  <span class="k">def</span> <span class="nf">_count</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1823"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-1824"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function count expects (nodeset)&#39;</span><span class="p">)</span>
<a name="cl-1825"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1826"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">nodeset</span><span class="o">.</span><span class="n">isNodeSet</span><span class="p">:</span>
<a name="cl-1827"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function count expects (nodeset)&#39;</span><span class="p">)</span>
<a name="cl-1828"></a>    <span class="k">return</span> <span class="n">nodeset</span><span class="o">.</span><span class="n">length</span>
<a name="cl-1829"></a>  
<a name="cl-1830"></a>  <span class="k">def</span> <span class="nf">_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1831"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-1832"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function id expects (object)&#39;</span><span class="p">)</span>
<a name="cl-1833"></a>    
<a name="cl-1834"></a>    <span class="n">s</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-1835"></a>    <span class="n">ctxn</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span>
<a name="cl-1836"></a>    <span class="k">if</span> <span class="n">ctxn</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span><span class="p">:</span>
<a name="cl-1837"></a>      <span class="n">doc</span><span class="o">=</span><span class="n">ctxn</span>
<a name="cl-1838"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1839"></a>      <span class="n">doc</span><span class="o">=</span><span class="n">ctxn</span><span class="o">.</span><span class="n">ownerDocument</span>
<a name="cl-1840"></a>    
<a name="cl-1841"></a>    <span class="n">s</span><span class="o">=</span><span class="n">s</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1842"></a>    <span class="n">ids</span><span class="o">=</span><span class="n">re_seqspace</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
<a name="cl-1843"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="n">NodeSet</span><span class="p">()</span>
<a name="cl-1844"></a>    <span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">ids</span><span class="p">:</span>
<a name="cl-1845"></a>      <span class="k">for</span> <span class="n">elm</span> <span class="ow">in</span> <span class="n">doc</span><span class="o">.</span><span class="n">findAll</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="nb">id</span><span class="p">):</span>
<a name="cl-1846"></a>        <span class="n">nodeset</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">elm</span><span class="p">)</span>
<a name="cl-1847"></a>    <span class="n">nodeset</span><span class="o">.</span><span class="n">isSorted</span><span class="o">=</span><span class="bp">False</span>
<a name="cl-1848"></a>    <span class="k">return</span> <span class="n">nodeset</span>
<a name="cl-1849"></a>  
<a name="cl-1850"></a>  <span class="k">def</span> <span class="nf">_localName</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1851"></a>    <span class="n">alen</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span>
<a name="cl-1852"></a>    <span class="k">if</span> <span class="n">alen</span><span class="o">&lt;</span><span class="mi">0</span> <span class="ow">or</span> <span class="mi">1</span><span class="o">&lt;</span><span class="n">alen</span><span class="p">:</span>
<a name="cl-1853"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function local-name expects (nodeset?)&#39;</span><span class="p">)</span>
<a name="cl-1854"></a>    <span class="k">if</span> <span class="n">alen</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1855"></a>      <span class="n">node</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span>
<a name="cl-1856"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1857"></a>      <span class="n">nodeset</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-1858"></a>      <span class="n">nodeset</span><span class="o">=</span><span class="n">nodeset</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1859"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-1860"></a>        <span class="n">node</span><span class="o">=</span><span class="n">nodeset</span><span class="o">.</span><span class="n">first</span><span class="p">()</span>
<a name="cl-1861"></a>    <span class="k">return</span> <span class="s">&#39;&#39;</span><span class="o">+</span><span class="n">node</span><span class="o">.</span><span class="n">nodeName</span>
<a name="cl-1862"></a>    
<a name="cl-1863"></a>  
<a name="cl-1864"></a>  <span class="k">def</span> <span class="nf">_name</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1865"></a>    <span class="c"># not implemented</span>
<a name="cl-1866"></a>    <span class="k">return</span> <span class="n">FunctionCall</span><span class="o">.</span><span class="n">funcs</span><span class="p">[</span><span class="s">&#39;local-name&#39;</span><span class="p">][</span><span class="mi">0</span><span class="p">](</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">)</span>
<a name="cl-1867"></a>  
<a name="cl-1868"></a>  <span class="k">def</span> <span class="nf">_namespaceUri</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1869"></a>    <span class="c"># not implemented</span>
<a name="cl-1870"></a>    <span class="k">return</span> <span class="s">&#39;&#39;</span>
<a name="cl-1871"></a>  
<a name="cl-1872"></a>  <span class="k">def</span> <span class="nf">_string</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1873"></a>    <span class="n">alen</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span>
<a name="cl-1874"></a>    <span class="k">if</span> <span class="n">alen</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1875"></a>      <span class="n">s</span><span class="o">=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="s">&#39;string&#39;</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1876"></a>    <span class="k">elif</span> <span class="n">alen</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-1877"></a>      <span class="n">s</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-1878"></a>      <span class="n">s</span><span class="o">=</span><span class="n">s</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1879"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1880"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function string expects (object?)&#39;</span><span class="p">)</span>
<a name="cl-1881"></a>    <span class="k">return</span> <span class="n">s</span>
<a name="cl-1882"></a>  
<a name="cl-1883"></a>  <span class="k">def</span> <span class="nf">_concat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1884"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">&lt;</span><span class="mi">2</span><span class="p">:</span>
<a name="cl-1885"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">&#39;Function concat expects (string, string[, ...])&#39;</span><span class="p">)</span>
<a name="cl-1886"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-1887"></a>    <span class="k">for</span> <span class="n">argument</span> <span class="ow">in</span> <span class="n">arguments</span><span class="p">:</span>
<a name="cl-1888"></a>      <span class="n">t</span><span class="o">+=</span><span class="n">argument</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1889"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-1890"></a>  
<a name="cl-1891"></a>  <span class="k">def</span> <span class="nf">_startsWith</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1892"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">2</span><span class="p">:</span>
<a name="cl-1893"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">&#39;Function starts-with expects (string, string)&#39;</span><span class="p">)</span>
<a name="cl-1894"></a>    <span class="p">(</span><span class="n">s1</span><span class="p">,</span><span class="n">s2</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">arguments</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<a name="cl-1895"></a>    <span class="n">s1</span><span class="o">=</span><span class="n">s1</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1896"></a>    <span class="n">s2</span><span class="o">=</span><span class="n">s2</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1897"></a>    <span class="c">#if s2 in s1 and s1.index(s2)==0:</span>
<a name="cl-1898"></a>    <span class="c">#  return True</span>
<a name="cl-1899"></a>    <span class="c">#else:</span>
<a name="cl-1900"></a>    <span class="c">#  return False</span>
<a name="cl-1901"></a>    <span class="k">if</span> <span class="n">s1</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">s2</span><span class="p">)</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1902"></a>      <span class="k">return</span> <span class="bp">True</span>
<a name="cl-1903"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1904"></a>      <span class="k">return</span> <span class="bp">False</span>
<a name="cl-1905"></a>  
<a name="cl-1906"></a>  <span class="k">def</span> <span class="nf">_contains</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1907"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">2</span><span class="p">:</span>
<a name="cl-1908"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">&#39;Function contains expects (string, string)&#39;</span><span class="p">)</span>
<a name="cl-1909"></a>    <span class="p">(</span><span class="n">s1</span><span class="p">,</span><span class="n">s2</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">arguments</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<a name="cl-1910"></a>    <span class="n">s1</span><span class="o">=</span><span class="n">s1</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1911"></a>    <span class="n">s2</span><span class="o">=</span><span class="n">s2</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1912"></a>    <span class="c">#if s2 in s1:</span>
<a name="cl-1913"></a>    <span class="c">#  return True</span>
<a name="cl-1914"></a>    <span class="c">#else:</span>
<a name="cl-1915"></a>    <span class="c">#  return False</span>
<a name="cl-1916"></a>    <span class="n">n</span><span class="o">=</span><span class="n">s1</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">s2</span><span class="p">)</span>
<a name="cl-1917"></a>    <span class="k">if</span> <span class="n">n</span><span class="o">&lt;</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1918"></a>      <span class="k">return</span> <span class="bp">False</span>
<a name="cl-1919"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1920"></a>      <span class="k">return</span> <span class="bp">True</span>
<a name="cl-1921"></a>  
<a name="cl-1922"></a>  <span class="k">def</span> <span class="nf">_substring</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1923"></a>    <span class="n">alen</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span>
<a name="cl-1924"></a>    <span class="k">if</span> <span class="n">alen</span><span class="o">&lt;</span><span class="mi">2</span> <span class="ow">or</span> <span class="mi">3</span><span class="o">&lt;</span><span class="n">alen</span><span class="p">:</span>
<a name="cl-1925"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function substring expects (string, string)&#39;</span><span class="p">)</span>
<a name="cl-1926"></a>    <span class="p">(</span><span class="n">s</span><span class="p">,</span><span class="n">n1</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">arguments</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<a name="cl-1927"></a>    <span class="n">s</span><span class="o">=</span><span class="n">s</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1928"></a>    <span class="n">n1</span><span class="o">=</span><span class="n">n1</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1929"></a>    <span class="k">if</span> <span class="n">alen</span><span class="o">==</span><span class="mi">2</span><span class="p">:</span>
<a name="cl-1930"></a>      <span class="n">n2</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span><span class="o">-</span><span class="n">n1</span><span class="o">+</span><span class="mi">1</span>
<a name="cl-1931"></a>    <span class="k">elif</span> <span class="n">alen</span><span class="o">==</span><span class="mi">3</span><span class="p">:</span>
<a name="cl-1932"></a>      <span class="n">n2</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
<a name="cl-1933"></a>      <span class="n">n2</span><span class="o">=</span><span class="n">n2</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1934"></a>    
<a name="cl-1935"></a>    <span class="k">if</span> <span class="n">n1</span><span class="o">==</span><span class="s">&#39;NaN&#39;</span> <span class="ow">or</span> <span class="n">n2</span><span class="o">==</span><span class="s">&#39;NaN&#39;</span> <span class="ow">or</span> <span class="n">n1</span><span class="o">==</span><span class="s">&#39;-Infinity&#39;</span> <span class="ow">or</span> <span class="n">n2</span><span class="o">==</span><span class="s">&#39;-Infinity&#39;</span> <span class="ow">or</span> <span class="n">n1</span><span class="o">==</span><span class="s">&#39;Infinity&#39;</span><span class="p">:</span>
<a name="cl-1936"></a>      <span class="k">return</span> <span class="s">u&#39;&#39;</span>
<a name="cl-1937"></a>    
<a name="cl-1938"></a>    <span class="c"># n1,n2:origin=1  a1,a2:origin=0</span>
<a name="cl-1939"></a>    <span class="n">n1</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">n1</span><span class="p">))</span>
<a name="cl-1940"></a>    <span class="n">a1</span><span class="o">=</span><span class="n">n1</span><span class="o">-</span><span class="mi">1</span>
<a name="cl-1941"></a>    <span class="k">if</span> <span class="n">a1</span><span class="o">&lt;</span><span class="mi">0</span><span class="p">:</span> <span class="n">a1</span><span class="o">=</span><span class="mi">0</span>
<a name="cl-1942"></a>    <span class="k">if</span> <span class="n">n2</span><span class="o">==</span><span class="s">&#39;Infinity&#39;</span><span class="p">:</span>
<a name="cl-1943"></a>      <span class="k">return</span> <span class="n">s</span><span class="p">[</span><span class="n">a1</span><span class="p">:]</span>
<a name="cl-1944"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1945"></a>      <span class="n">n2</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">n2</span><span class="p">))</span>
<a name="cl-1946"></a>      <span class="n">a2</span><span class="o">=</span><span class="n">n1</span><span class="o">+</span><span class="n">n2</span><span class="o">-</span><span class="mi">1</span>
<a name="cl-1947"></a>      <span class="k">return</span> <span class="n">s</span><span class="p">[</span><span class="n">a1</span><span class="p">:</span><span class="n">a2</span><span class="p">]</span>
<a name="cl-1948"></a>  
<a name="cl-1949"></a>  <span class="k">def</span> <span class="nf">_substringBefore</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1950"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">2</span><span class="p">:</span>
<a name="cl-1951"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">&#39;Function substring-before expects (string, string)&#39;</span><span class="p">)</span>
<a name="cl-1952"></a>    <span class="p">(</span><span class="n">s1</span><span class="p">,</span><span class="n">s2</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">arguments</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<a name="cl-1953"></a>    <span class="n">s1</span><span class="o">=</span><span class="n">s1</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1954"></a>    <span class="n">s2</span><span class="o">=</span><span class="n">s2</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1955"></a>    <span class="c">#if s2 in s1:</span>
<a name="cl-1956"></a>    <span class="c">#  n=s1.index(s2)</span>
<a name="cl-1957"></a>    <span class="c">#else:</span>
<a name="cl-1958"></a>    <span class="c">#  return &#39;&#39;</span>
<a name="cl-1959"></a>    <span class="n">n</span><span class="o">=</span><span class="n">s1</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">s2</span><span class="p">)</span>
<a name="cl-1960"></a>    <span class="k">if</span> <span class="n">n</span><span class="o">&lt;</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1961"></a>      <span class="k">return</span> <span class="s">&#39;&#39;</span>
<a name="cl-1962"></a>    <span class="k">return</span> <span class="n">s1</span><span class="p">[:</span><span class="n">n</span><span class="p">]</span>
<a name="cl-1963"></a>  
<a name="cl-1964"></a>  <span class="k">def</span> <span class="nf">_substringAfter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1965"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">2</span><span class="p">:</span>
<a name="cl-1966"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">&#39;Function substring-after expects (string, string)&#39;</span><span class="p">)</span>
<a name="cl-1967"></a>    <span class="p">(</span><span class="n">s1</span><span class="p">,</span><span class="n">s2</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">arguments</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<a name="cl-1968"></a>    <span class="n">s1</span><span class="o">=</span><span class="n">s1</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1969"></a>    <span class="n">s2</span><span class="o">=</span><span class="n">s2</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1970"></a>    <span class="c">#if s2 in s1:</span>
<a name="cl-1971"></a>    <span class="c">#  n=s1.index(s2)</span>
<a name="cl-1972"></a>    <span class="c">#else:</span>
<a name="cl-1973"></a>    <span class="c">#  return &#39;&#39;</span>
<a name="cl-1974"></a>    <span class="n">n</span><span class="o">=</span><span class="n">s1</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">s2</span><span class="p">)</span>
<a name="cl-1975"></a>    <span class="k">if</span> <span class="n">n</span><span class="o">&lt;</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1976"></a>      <span class="k">return</span> <span class="s">&#39;&#39;</span>
<a name="cl-1977"></a>    <span class="k">return</span> <span class="n">s1</span><span class="p">[</span><span class="n">n</span><span class="o">+</span><span class="nb">len</span><span class="p">(</span><span class="n">s2</span><span class="p">):]</span>
<a name="cl-1978"></a>  
<a name="cl-1979"></a>  <span class="k">def</span> <span class="nf">_substringLength</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1980"></a>    <span class="n">alen</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span>
<a name="cl-1981"></a>    <span class="k">if</span> <span class="n">alen</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1982"></a>      <span class="n">s</span><span class="o">=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="s">&#39;string&#39;</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1983"></a>    <span class="k">elif</span> <span class="n">alen</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-1984"></a>      <span class="n">s</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-1985"></a>      <span class="n">s</span><span class="o">=</span><span class="n">s</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1986"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1987"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function string-length expects (string?)&#39;</span><span class="p">)</span>
<a name="cl-1988"></a>    <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
<a name="cl-1989"></a>  
<a name="cl-1990"></a>  <span class="k">def</span> <span class="nf">_normalizeSpace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-1991"></a>    <span class="n">alen</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span>
<a name="cl-1992"></a>    <span class="k">if</span> <span class="n">alen</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-1993"></a>      <span class="n">s</span><span class="o">=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="s">&#39;string&#39;</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="p">)</span>
<a name="cl-1994"></a>    <span class="k">elif</span> <span class="n">alen</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-1995"></a>      <span class="n">s</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-1996"></a>      <span class="n">s</span><span class="o">=</span><span class="n">s</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-1997"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-1998"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function normalize-space expects (string?)&#39;</span><span class="p">)</span>
<a name="cl-1999"></a>    <span class="k">return</span> <span class="n">re_lastspace</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">,</span><span class="n">re_firstspace</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">,</span><span class="n">re_seqspace</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">,</span><span class="n">s</span><span class="p">)))</span>
<a name="cl-2000"></a>  
<a name="cl-2001"></a>  <span class="k">def</span> <span class="nf">_translate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2002"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">3</span><span class="p">:</span>
<a name="cl-2003"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">&#39;Function translate expects (string, string, string)&#39;</span><span class="p">)</span>
<a name="cl-2004"></a>    <span class="p">(</span><span class="n">s1</span><span class="p">,</span><span class="n">s2</span><span class="p">,</span><span class="n">s3</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">arguments</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span><span class="n">arguments</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
<a name="cl-2005"></a>    <span class="n">s1</span><span class="o">=</span><span class="n">s1</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2006"></a>    <span class="n">s2</span><span class="o">=</span><span class="n">s2</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2007"></a>    <span class="n">s3</span><span class="o">=</span><span class="n">s3</span><span class="o">.</span><span class="n">string</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2008"></a>    <span class="n">_map</span><span class="o">=</span><span class="p">{}</span>
<a name="cl-2009"></a>    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">s2</span><span class="p">)):</span>
<a name="cl-2010"></a>      <span class="n">ch</span><span class="o">=</span><span class="n">s2</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<a name="cl-2011"></a>      <span class="k">if</span> <span class="ow">not</span> <span class="n">_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">ch</span><span class="p">):</span>
<a name="cl-2012"></a>        <span class="n">_map</span><span class="p">[</span><span class="n">ch</span><span class="p">]</span><span class="o">=</span><span class="n">s3</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="k">if</span> <span class="n">i</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="n">s3</span><span class="p">)</span> <span class="k">else</span> <span class="s">&#39;&#39;</span>
<a name="cl-2013"></a>    <span class="n">t</span><span class="o">=</span><span class="s">&#39;&#39;</span>
<a name="cl-2014"></a>    <span class="k">for</span> <span class="n">ch</span> <span class="ow">in</span> <span class="n">s1</span><span class="p">:</span>
<a name="cl-2015"></a>      <span class="n">replace</span><span class="o">=</span><span class="n">_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">ch</span><span class="p">)</span>
<a name="cl-2016"></a>      <span class="n">t</span><span class="o">+=</span><span class="n">replace</span> <span class="k">if</span> <span class="n">replace</span><span class="o">!=</span><span class="bp">None</span> <span class="k">else</span> <span class="n">ch</span>
<a name="cl-2017"></a>    <span class="k">return</span> <span class="n">t</span>
<a name="cl-2018"></a>  
<a name="cl-2019"></a>  <span class="k">def</span> <span class="nf">_boolean</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2020"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-2021"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function not expects (object)&#39;</span><span class="p">)</span>
<a name="cl-2022"></a>    <span class="n">b</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2023"></a>    <span class="n">b</span><span class="o">=</span><span class="n">b</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2024"></a>    <span class="k">return</span> <span class="n">b</span>
<a name="cl-2025"></a>  
<a name="cl-2026"></a>  <span class="k">def</span> <span class="nf">_not</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2027"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-2028"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function not expects (object)&#39;</span><span class="p">)</span>
<a name="cl-2029"></a>    <span class="n">b</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2030"></a>    <span class="n">b</span><span class="o">=</span><span class="n">b</span><span class="o">.</span><span class="n">bool</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2031"></a>    <span class="k">return</span> <span class="ow">not</span> <span class="n">b</span>
<a name="cl-2032"></a>  
<a name="cl-2033"></a>  <span class="k">def</span> <span class="nf">_true</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2034"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-2035"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function false expects ()&#39;</span><span class="p">)</span>
<a name="cl-2036"></a>    <span class="k">return</span> <span class="bp">True</span>
<a name="cl-2037"></a>  
<a name="cl-2038"></a>  <span class="k">def</span> <span class="nf">_false</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2039"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-2040"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function false expects ()&#39;</span><span class="p">)</span>
<a name="cl-2041"></a>    <span class="k">return</span> <span class="bp">False</span>
<a name="cl-2042"></a>  
<a name="cl-2043"></a>  <span class="k">def</span> <span class="nf">_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2044"></a>    <span class="c"># not implemented</span>
<a name="cl-2045"></a>    <span class="k">return</span> <span class="bp">False</span>
<a name="cl-2046"></a>  
<a name="cl-2047"></a>  <span class="k">def</span> <span class="nf">_number</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2048"></a>    <span class="n">alen</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span>
<a name="cl-2049"></a>    <span class="k">if</span> <span class="n">alen</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-2050"></a>      <span class="n">n</span><span class="o">=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="s">&#39;number&#39;</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2051"></a>    <span class="k">elif</span> <span class="n">alen</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-2052"></a>      <span class="n">n</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2053"></a>      <span class="n">n</span><span class="o">=</span><span class="n">n</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2054"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2055"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function number expects (object?)&#39;</span><span class="p">)</span>
<a name="cl-2056"></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">n</span><span class="p">,</span><span class="nb">int</span><span class="p">):</span>
<a name="cl-2057"></a>      <span class="k">return</span> <span class="n">n</span>
<a name="cl-2058"></a>    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">n</span><span class="p">,</span><span class="nb">float</span><span class="p">):</span>
<a name="cl-2059"></a>      <span class="n">n1</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<a name="cl-2060"></a>      <span class="k">return</span> <span class="n">n1</span> <span class="k">if</span> <span class="n">n1</span><span class="o">==</span><span class="n">n</span> <span class="k">else</span> <span class="n">n</span>
<a name="cl-2061"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2062"></a>      <span class="k">return</span> <span class="s">&#39;NaN&#39;</span>
<a name="cl-2063"></a>  
<a name="cl-2064"></a>  <span class="k">def</span> <span class="nf">_sum</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2065"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-2066"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function sum expects (nodeset)&#39;</span><span class="p">)</span>
<a name="cl-2067"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2068"></a>    <span class="n">nodeset</span><span class="o">=</span><span class="n">nodeset</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2069"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2070"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function sum expects (nodeset)&#39;</span><span class="p">)</span>
<a name="cl-2071"></a>    <span class="n">nodes</span><span class="o">=</span><span class="n">nodeset</span><span class="o">.</span><span class="n">list</span><span class="p">()</span>
<a name="cl-2072"></a>    <span class="n">n</span><span class="o">=</span><span class="mi">0</span>
<a name="cl-2073"></a>    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
<a name="cl-2074"></a>      <span class="n">n</span><span class="o">+=</span><span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="s">&#39;number&#39;</span><span class="p">,</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2075"></a>    <span class="k">return</span> <span class="n">n</span>
<a name="cl-2076"></a>  
<a name="cl-2077"></a>  <span class="k">def</span> <span class="nf">_floor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2078"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-2079"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function floor expects (number)&#39;</span><span class="p">)</span>
<a name="cl-2080"></a>    <span class="n">n</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2081"></a>    <span class="n">n</span><span class="o">=</span><span class="n">n</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2082"></a>    <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">floor</span><span class="p">(</span><span class="n">n</span><span class="p">))</span>
<a name="cl-2083"></a>  
<a name="cl-2084"></a>  <span class="k">def</span> <span class="nf">_ceiling</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2085"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-2086"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function ceiling expects (number)&#39;</span><span class="p">)</span>
<a name="cl-2087"></a>    <span class="n">n</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2088"></a>    <span class="n">n</span><span class="o">=</span><span class="n">n</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2089"></a>    <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">ceil</span><span class="p">(</span><span class="n">n</span><span class="p">))</span>
<a name="cl-2090"></a>  
<a name="cl-2091"></a>  <span class="k">def</span> <span class="nf">_round</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">arguments</span><span class="p">):</span>
<a name="cl-2092"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arguments</span><span class="p">)</span><span class="o">!=</span><span class="mi">1</span><span class="p">:</span>
<a name="cl-2093"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;Function round expects (number)&#39;</span><span class="p">)</span>
<a name="cl-2094"></a>    <span class="n">n</span><span class="o">=</span><span class="n">arguments</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2095"></a>    <span class="n">n</span><span class="o">=</span><span class="n">n</span><span class="o">.</span><span class="n">number</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
<a name="cl-2096"></a>    <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">n</span><span class="p">))</span>
<a name="cl-2097"></a>  
<a name="cl-2098"></a>  <span class="n">funcs</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-2099"></a>    <span class="s">&#39;context-node&#39;</span>    <span class="p">:[</span><span class="n">_contextNode</span>    <span class="p">,</span><span class="s">&#39;nodeset&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[</span><span class="bp">True</span><span class="p">]]</span>
<a name="cl-2100"></a>  <span class="p">,</span> <span class="s">&#39;root-node&#39;</span>       <span class="p">:[</span><span class="n">_rootNode</span>       <span class="p">,</span><span class="s">&#39;nodeset&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2101"></a>  <span class="p">,</span> <span class="s">&#39;last&#39;</span>            <span class="p">:[</span><span class="n">_last</span>           <span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">True</span> <span class="p">,[]]</span>
<a name="cl-2102"></a>  <span class="p">,</span> <span class="s">&#39;position&#39;</span>        <span class="p">:[</span><span class="n">_position</span>       <span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">True</span> <span class="p">,[]]</span>
<a name="cl-2103"></a>  <span class="p">,</span> <span class="s">&#39;count&#39;</span>           <span class="p">:[</span><span class="n">_count</span>          <span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2104"></a>  <span class="p">,</span> <span class="s">&#39;id&#39;</span>              <span class="p">:[</span><span class="n">_id</span>             <span class="p">,</span><span class="s">&#39;nodeset&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2105"></a>  <span class="p">,</span> <span class="s">&#39;local-name&#39;</span>      <span class="p">:[</span><span class="n">_localName</span>      <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[</span><span class="bp">True</span> <span class="p">,</span><span class="bp">False</span><span class="p">]]</span>
<a name="cl-2106"></a>  <span class="p">,</span> <span class="s">&#39;name&#39;</span>            <span class="p">:[</span><span class="n">_name</span>           <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[</span><span class="bp">True</span> <span class="p">,</span><span class="bp">False</span><span class="p">]]</span>
<a name="cl-2107"></a>  <span class="p">,</span> <span class="s">&#39;namespace-uri&#39;</span>   <span class="p">:[</span><span class="n">_namespaceUri</span>   <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[</span><span class="bp">True</span> <span class="p">,</span><span class="bp">False</span><span class="p">]]</span>
<a name="cl-2108"></a>  <span class="p">,</span> <span class="s">&#39;string&#39;</span>          <span class="p">:[</span><span class="n">_string</span>         <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[</span><span class="bp">True</span> <span class="p">,</span><span class="bp">False</span><span class="p">]]</span>
<a name="cl-2109"></a>  <span class="p">,</span> <span class="s">&#39;concat&#39;</span>          <span class="p">:[</span><span class="n">_concat</span>         <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2110"></a>  <span class="p">,</span> <span class="s">&#39;starts-with&#39;</span>     <span class="p">:[</span><span class="n">_startsWith</span>     <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2111"></a>  <span class="p">,</span> <span class="s">&#39;contains&#39;</span>        <span class="p">:[</span><span class="n">_contains</span>       <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2112"></a>  <span class="p">,</span> <span class="s">&#39;substring&#39;</span>       <span class="p">:[</span><span class="n">_substring</span>      <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2113"></a>  <span class="p">,</span> <span class="s">&#39;substring-before&#39;</span><span class="p">:[</span><span class="n">_substringBefore</span><span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2114"></a>  <span class="p">,</span> <span class="s">&#39;substring-after&#39;</span> <span class="p">:[</span><span class="n">_substringAfter</span> <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2115"></a>  <span class="p">,</span> <span class="s">&#39;string-length&#39;</span>   <span class="p">:[</span><span class="n">_substringLength</span><span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[</span><span class="bp">True</span> <span class="p">,</span><span class="bp">False</span><span class="p">]]</span>
<a name="cl-2116"></a>  <span class="p">,</span> <span class="s">&#39;normalize-space&#39;</span> <span class="p">:[</span><span class="n">_normalizeSpace</span> <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[</span><span class="bp">True</span> <span class="p">,</span><span class="bp">False</span><span class="p">]]</span>
<a name="cl-2117"></a>  <span class="p">,</span> <span class="s">&#39;translate&#39;</span>       <span class="p">:[</span><span class="n">_translate</span>      <span class="p">,</span><span class="s">&#39;string&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2118"></a>  <span class="p">,</span> <span class="s">&#39;boolean&#39;</span>         <span class="p">:[</span><span class="n">_boolean</span>        <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2119"></a>  <span class="p">,</span> <span class="s">&#39;not&#39;</span>             <span class="p">:[</span><span class="n">_not</span>            <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2120"></a>  <span class="p">,</span> <span class="s">&#39;true&#39;</span>            <span class="p">:[</span><span class="n">_true</span>           <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2121"></a>  <span class="p">,</span> <span class="s">&#39;false&#39;</span>           <span class="p">:[</span><span class="n">_false</span>          <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2122"></a>  <span class="p">,</span> <span class="s">&#39;lang&#39;</span>            <span class="p">:[</span><span class="n">_lang</span>           <span class="p">,</span><span class="s">&#39;boolean&#39;</span><span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2123"></a>  <span class="p">,</span> <span class="s">&#39;number&#39;</span>          <span class="p">:[</span><span class="n">_number</span>         <span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[</span><span class="bp">True</span> <span class="p">,</span><span class="bp">False</span><span class="p">]]</span>
<a name="cl-2124"></a>  <span class="p">,</span> <span class="s">&#39;sum&#39;</span>             <span class="p">:[</span><span class="n">_sum</span>            <span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2125"></a>  <span class="p">,</span> <span class="s">&#39;floor&#39;</span>           <span class="p">:[</span><span class="n">_floor</span>          <span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2126"></a>  <span class="p">,</span> <span class="s">&#39;ceiling&#39;</span>         <span class="p">:[</span><span class="n">_ceiling</span>        <span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2127"></a>  <span class="p">,</span> <span class="s">&#39;round&#39;</span>           <span class="p">:[</span><span class="n">_round</span>          <span class="p">,</span><span class="s">&#39;number&#39;</span> <span class="p">,</span><span class="bp">False</span><span class="p">,[]]</span>
<a name="cl-2128"></a>  <span class="p">})</span>
<a name="cl-2129"></a>  
<a name="cl-2130"></a>  <span class="nd">@classmethod</span>
<a name="cl-2131"></a>  <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span><span class="n">lexer</span><span class="p">):</span>
<a name="cl-2132"></a>    <span class="n">func</span><span class="o">=</span><span class="n">cls</span><span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">())</span>
<a name="cl-2133"></a>    <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-2134"></a>    <span class="k">while</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span><span class="o">!=</span><span class="s">&#39;)&#39;</span><span class="p">:</span>
<a name="cl-2135"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-2136"></a>        <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;missing function argument list&#39;</span><span class="p">)</span>
<a name="cl-2137"></a>      <span class="n">expr</span><span class="o">=</span><span class="n">BinaryExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-2138"></a>      <span class="n">func</span><span class="o">.</span><span class="n">arg</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-2139"></a>      <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span><span class="o">!=</span><span class="s">&#39;,&#39;</span><span class="p">:</span>
<a name="cl-2140"></a>        <span class="k">break</span>
<a name="cl-2141"></a>      <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<a name="cl-2142"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-2143"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;unclosed function argument list&#39;</span><span class="p">)</span>
<a name="cl-2144"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()</span><span class="o">!=</span><span class="s">&#39;)&#39;</span><span class="p">:</span>
<a name="cl-2145"></a>      <span class="n">lexer</span><span class="o">.</span><span class="n">back</span><span class="p">()</span>
<a name="cl-2146"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad token: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()))</span>
<a name="cl-2147"></a>    <span class="k">return</span> <span class="n">func</span>
<a name="cl-2148"></a>
<a name="cl-2149"></a><span class="c">#} // end of FunctionCall</span>
<a name="cl-2150"></a>
<a name="cl-2151"></a>
<a name="cl-2152"></a><span class="c">#{ // NodeSet</span>
<a name="cl-2153"></a><span class="k">class</span> <span class="nc">NodeSet</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-2154"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2155"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">=</span><span class="mi">0</span>
<a name="cl-2156"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-2157"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">seen</span><span class="o">=</span><span class="p">{}</span>
<a name="cl-2158"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">idIndexMap</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2159"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">reserveDels</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-2160"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">isNodeSet</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-2161"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">isSorted</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-2162"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">sortOff</span><span class="o">=</span><span class="bp">False</span>
<a name="cl-2163"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2164"></a>  
<a name="cl-2165"></a>  <span class="k">def</span> <span class="nf">merge</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">nodeset</span><span class="p">):</span>
<a name="cl-2166"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">isSorted</span><span class="o">=</span><span class="bp">False</span>
<a name="cl-2167"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2168"></a>      <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">nodeset</span><span class="o">.</span><span class="n">only</span><span class="p">)</span>
<a name="cl-2169"></a>    
<a name="cl-2170"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2171"></a>      <span class="n">only</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">only</span>
<a name="cl-2172"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2173"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">only</span><span class="p">)</span>
<a name="cl-2174"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">-=</span><span class="mi">1</span>
<a name="cl-2175"></a>    
<a name="cl-2176"></a>    <span class="nb">map</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_add</span><span class="p">,</span><span class="n">nodeset</span><span class="o">.</span><span class="n">nodes</span><span class="p">)</span>
<a name="cl-2177"></a>  
<a name="cl-2178"></a>  <span class="k">def</span> <span class="nf">sort</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2179"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2180"></a>      <span class="k">return</span>
<a name="cl-2181"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;sortOff&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2182"></a>      <span class="k">return</span>
<a name="cl-2183"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;isSorted&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2184"></a>      <span class="k">return</span>
<a name="cl-2185"></a>    
<a name="cl-2186"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">isSorted</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-2187"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">idIndexMap</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2188"></a>    <span class="n">nodes</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes</span>
<a name="cl-2189"></a>    
<a name="cl-2190"></a>    <span class="k">def</span> <span class="nf">_comp</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">):</span>
<a name="cl-2191"></a>      <span class="k">if</span> <span class="n">a</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">a</span><span class="o">=</span><span class="n">a</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2192"></a>      <span class="k">if</span> <span class="n">b</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">b</span><span class="o">=</span><span class="n">b</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2193"></a>      <span class="k">if</span> <span class="n">a</span><span class="o">==</span><span class="n">b</span><span class="p">:</span>
<a name="cl-2194"></a>        <span class="k">return</span> <span class="mi">0</span>
<a name="cl-2195"></a>      <span class="p">(</span><span class="n">node1</span><span class="p">,</span><span class="n">node2</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">)</span>
<a name="cl-2196"></a>      <span class="p">(</span><span class="n">ancestor1</span><span class="p">,</span><span class="n">ancestor2</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">)</span>
<a name="cl-2197"></a>      <span class="p">(</span><span class="n">deep1</span><span class="p">,</span><span class="n">deep2</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">)</span>
<a name="cl-2198"></a>      
<a name="cl-2199"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-2200"></a>        <span class="n">ancestor1</span><span class="o">=</span><span class="n">ancestor1</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2201"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">ancestor1</span><span class="p">:</span>
<a name="cl-2202"></a>          <span class="k">break</span>
<a name="cl-2203"></a>        <span class="n">deep1</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2204"></a>      
<a name="cl-2205"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-2206"></a>        <span class="n">ancestor2</span><span class="o">=</span><span class="n">ancestor2</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2207"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">ancestor2</span><span class="p">:</span>
<a name="cl-2208"></a>          <span class="k">break</span>
<a name="cl-2209"></a>        <span class="n">deep2</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2210"></a>      
<a name="cl-2211"></a>      <span class="k">if</span> <span class="n">deep1</span><span class="o">&gt;</span><span class="n">deep2</span><span class="p">:</span>
<a name="cl-2212"></a>        <span class="k">while</span> <span class="n">deep1</span><span class="o">!=</span><span class="n">deep2</span><span class="p">:</span>
<a name="cl-2213"></a>          <span class="n">deep1</span><span class="o">-=</span><span class="mi">1</span>
<a name="cl-2214"></a>          <span class="n">node1</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2215"></a>          <span class="k">if</span> <span class="n">node1</span><span class="o">==</span><span class="n">node2</span><span class="p">:</span>
<a name="cl-2216"></a>            <span class="k">return</span> <span class="mi">1</span>
<a name="cl-2217"></a>      <span class="k">elif</span> <span class="n">deep2</span><span class="o">&gt;</span><span class="n">deep1</span><span class="p">:</span>
<a name="cl-2218"></a>        <span class="k">while</span> <span class="n">deep2</span><span class="o">!=</span><span class="n">deep1</span><span class="p">:</span>
<a name="cl-2219"></a>          <span class="n">deep2</span><span class="o">-=</span><span class="mi">1</span>
<a name="cl-2220"></a>          <span class="n">node2</span><span class="o">=</span><span class="n">node2</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2221"></a>          <span class="k">if</span> <span class="n">node1</span><span class="o">==</span><span class="n">node2</span><span class="p">:</span>
<a name="cl-2222"></a>            <span class="k">return</span> <span class="o">-</span><span class="mi">1</span>
<a name="cl-2223"></a>      
<a name="cl-2224"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-2225"></a>        <span class="n">ancestor1</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2226"></a>        <span class="n">ancestor2</span><span class="o">=</span><span class="n">node2</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2227"></a>        <span class="k">if</span> <span class="n">ancestor1</span><span class="o">==</span><span class="n">ancestor2</span><span class="p">:</span>
<a name="cl-2228"></a>          <span class="k">break</span>
<a name="cl-2229"></a>        <span class="n">node1</span><span class="o">=</span><span class="n">ancestor1</span>
<a name="cl-2230"></a>        <span class="n">node2</span><span class="o">=</span><span class="n">ancestor2</span>
<a name="cl-2231"></a>      
<a name="cl-2232"></a>      <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-2233"></a>        <span class="n">node1</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">nextSibling</span>
<a name="cl-2234"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">node1</span><span class="p">:</span>
<a name="cl-2235"></a>          <span class="k">break</span>
<a name="cl-2236"></a>        <span class="k">if</span> <span class="n">node1</span><span class="o">==</span><span class="n">node2</span><span class="p">:</span>
<a name="cl-2237"></a>          <span class="k">return</span> <span class="o">-</span><span class="mi">1</span>
<a name="cl-2238"></a>      
<a name="cl-2239"></a>      <span class="k">return</span> <span class="mi">1</span>
<a name="cl-2240"></a>    
<a name="cl-2241"></a>    <span class="k">def</span> <span class="nf">index_comp</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">):</span>
<a name="cl-2242"></a>      <span class="k">if</span> <span class="n">a</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">a</span><span class="o">=</span><span class="n">a</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2243"></a>      <span class="k">if</span> <span class="n">b</span><span class="o">.</span><span class="n">nodeType</span><span class="o">==</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ATTRIBUTE_NODE</span><span class="p">:</span> <span class="n">b</span><span class="o">=</span><span class="n">b</span><span class="o">.</span><span class="n">parentNode</span>
<a name="cl-2244"></a>      <span class="k">return</span> <span class="nb">cmp</span><span class="p">(</span><span class="n">a</span><span class="o">.</span><span class="n">_sortindex</span><span class="p">,</span><span class="n">b</span><span class="o">.</span><span class="n">_sortindex</span><span class="p">)</span>
<a name="cl-2245"></a>    
<a name="cl-2246"></a>    <span class="k">if</span> <span class="n">USE_NODE_INDEX</span><span class="p">:</span>
<a name="cl-2247"></a>      <span class="n">nodes</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">index_comp</span><span class="p">)</span>
<a name="cl-2248"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2249"></a>      <span class="n">nodes</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">_comp</span><span class="p">)</span>
<a name="cl-2250"></a>  
<a name="cl-2251"></a>  <span class="k">def</span> <span class="nf">reserveDelByNodeID</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="nb">id</span><span class="p">,</span><span class="n">offset</span><span class="p">,</span><span class="n">reverse</span><span class="p">):</span>
<a name="cl-2252"></a>    <span class="n">_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">createIdIndexMap</span><span class="p">()</span>
<a name="cl-2253"></a>    <span class="n">index</span><span class="o">=</span><span class="n">_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">id</span><span class="p">)</span>
<a name="cl-2254"></a>    <span class="k">if</span> <span class="n">index</span><span class="p">:</span>
<a name="cl-2255"></a>      <span class="k">if</span> <span class="n">reverse</span> <span class="ow">and</span> <span class="n">index</span><span class="o">&lt;</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">-</span><span class="n">offset</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">reverse</span> <span class="ow">and</span> <span class="n">offset</span><span class="o">&lt;</span><span class="n">index</span><span class="p">:</span>
<a name="cl-2256"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reserveDels</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
<a name="cl-2257"></a>  
<a name="cl-2258"></a>  <span class="k">def</span> <span class="nf">reserveDelByNode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">offset</span><span class="p">,</span><span class="n">reverse</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
<a name="cl-2259"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">reserveDelByNodeID</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">NodeID</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="p">),</span><span class="n">offset</span><span class="p">,</span><span class="n">reverse</span><span class="p">)</span>
<a name="cl-2260"></a>  
<a name="cl-2261"></a>  <span class="k">def</span> <span class="nf">doDel</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2262"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">reserveDels</span><span class="p">)</span><span class="o">&lt;=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-2263"></a>      <span class="k">return</span>
<a name="cl-2264"></a>    <span class="nb">map</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_del</span><span class="p">,</span><span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">reserveDels</span><span class="p">,</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">:</span><span class="nb">cmp</span><span class="p">(</span><span class="n">y</span><span class="p">,</span><span class="n">x</span><span class="p">)))</span>
<a name="cl-2265"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">reserveDels</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-2266"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">idIndexMap</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2267"></a>  
<a name="cl-2268"></a>  <span class="k">def</span> <span class="nf">createIdIndexMap</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2269"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;idIndexMap&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2270"></a>      <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">idIndexMap</span>
<a name="cl-2271"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2272"></a>      <span class="n">_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">idIndexMap</span><span class="o">=</span><span class="p">{}</span>
<a name="cl-2273"></a>      <span class="n">nodes</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes</span>
<a name="cl-2274"></a>      <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">)):</span>
<a name="cl-2275"></a>        <span class="n">node</span><span class="o">=</span><span class="n">nodes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<a name="cl-2276"></a>        <span class="nb">id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">NodeID</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2277"></a>        <span class="n">_map</span><span class="p">[</span><span class="nb">id</span><span class="p">]</span><span class="o">=</span><span class="n">i</span>
<a name="cl-2278"></a>      <span class="k">return</span> <span class="n">_map</span>
<a name="cl-2279"></a>  
<a name="cl-2280"></a>  <span class="k">def</span> <span class="nf">_del</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">index</span><span class="p">):</span>
<a name="cl-2281"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">-=</span><span class="mi">1</span>
<a name="cl-2282"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2283"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2284"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2285"></a>      <span class="n">node</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
<a name="cl-2286"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;_first&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">==</span><span class="n">node</span><span class="p">:</span>
<a name="cl-2287"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_first</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2288"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_firstSourceIndex</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2289"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_firstSubIndex</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2290"></a>      <span class="k">del</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">seen</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">NodeID</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="p">)])</span>
<a name="cl-2291"></a>      <span class="k">del</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
<a name="cl-2292"></a>  
<a name="cl-2293"></a>  <span class="k">def</span> <span class="nf">delDescendant</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">elm</span><span class="p">,</span><span class="n">offset</span><span class="p">):</span>
<a name="cl-2294"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2295"></a>      <span class="k">return</span>
<a name="cl-2296"></a>    <span class="n">nodeType</span><span class="o">=</span><span class="n">elm</span><span class="o">.</span><span class="n">nodeType</span>
<a name="cl-2297"></a>    <span class="k">if</span> <span class="n">nodeType</span><span class="o">!=</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">ELEMENT_NODE</span> <span class="ow">and</span> <span class="n">nodeType</span><span class="o">!=</span><span class="n">NodeTypeDOM</span><span class="o">.</span><span class="n">DOCUMENT_NODE</span><span class="p">:</span>
<a name="cl-2298"></a>      <span class="k">return</span>
<a name="cl-2299"></a>    
<a name="cl-2300"></a>    <span class="n">nodes</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes</span>
<a name="cl-2301"></a>    <span class="n">i</span><span class="o">=</span><span class="n">offset</span><span class="o">+</span><span class="mi">1</span>
<a name="cl-2302"></a>    <span class="k">while</span> <span class="n">i</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">):</span>
<a name="cl-2303"></a>      <span class="k">if</span> <span class="n">elm</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="n">nodes</span><span class="p">[</span><span class="n">i</span><span class="p">]):</span>
<a name="cl-2304"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_del</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<a name="cl-2305"></a>        <span class="n">i</span><span class="o">-=</span><span class="mi">1</span>
<a name="cl-2306"></a>      <span class="n">i</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2307"></a>  
<a name="cl-2308"></a>  <span class="k">def</span> <span class="nf">_add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="n">reverse</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
<a name="cl-2309"></a>    <span class="n">seen</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">seen</span>
<a name="cl-2310"></a>    <span class="nb">id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">NodeID</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2311"></a>    <span class="k">if</span> <span class="n">seen</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">id</span><span class="p">):</span>
<a name="cl-2312"></a>      <span class="k">return</span>
<a name="cl-2313"></a>    <span class="n">seen</span><span class="p">[</span><span class="nb">id</span><span class="p">]</span><span class="o">=</span><span class="bp">True</span>
<a name="cl-2314"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2315"></a>    <span class="k">if</span> <span class="n">reverse</span><span class="p">:</span>
<a name="cl-2316"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2317"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2318"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2319"></a>  
<a name="cl-2320"></a>  <span class="k">def</span> <span class="nf">unshift</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">):</span>
<a name="cl-2321"></a>    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">&lt;=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-2322"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2323"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="o">=</span><span class="n">node</span>
<a name="cl-2324"></a>      <span class="k">return</span>
<a name="cl-2325"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2326"></a>      <span class="n">only</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">only</span>
<a name="cl-2327"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2328"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">unshift</span><span class="p">(</span><span class="n">only</span><span class="p">)</span>
<a name="cl-2329"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">-=</span><span class="mi">1</span>
<a name="cl-2330"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-2331"></a>  
<a name="cl-2332"></a>  <span class="k">def</span> <span class="nf">push</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">):</span>
<a name="cl-2333"></a>    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">&lt;=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-2334"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2335"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="o">=</span><span class="n">node</span>
<a name="cl-2336"></a>      <span class="k">return</span>
<a name="cl-2337"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2338"></a>      <span class="n">only</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">only</span>
<a name="cl-2339"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2340"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="n">only</span><span class="p">)</span>
<a name="cl-2341"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="o">-=</span><span class="mi">1</span>
<a name="cl-2342"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2343"></a>  
<a name="cl-2344"></a>  <span class="k">def</span> <span class="nf">first</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2345"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2346"></a>      <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">only</span>
<a name="cl-2347"></a>    <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">):</span>
<a name="cl-2348"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
<a name="cl-2349"></a>      <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2350"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2351"></a>      <span class="k">return</span> <span class="bp">None</span>
<a name="cl-2352"></a>  
<a name="cl-2353"></a>  <span class="k">def</span> <span class="nf">list</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2354"></a>    <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2355"></a>      <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="p">]</span>
<a name="cl-2356"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
<a name="cl-2357"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span>
<a name="cl-2358"></a>  
<a name="cl-2359"></a>  <span class="k">def</span> <span class="nf">string</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2360"></a>    <span class="n">node</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">only</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">first</span><span class="p">()</span>
<a name="cl-2361"></a>    <span class="k">return</span> <span class="n">NodeUtil</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="s">&#39;string&#39;</span><span class="p">,</span><span class="n">node</span><span class="p">)</span> <span class="k">if</span> <span class="n">node</span> <span class="k">else</span> <span class="s">&#39;&#39;</span>
<a name="cl-2362"></a>  
<a name="cl-2363"></a>  <span class="k">def</span> <span class="nf">bool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2364"></a>    <span class="k">return</span> <span class="n">toBoolean</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">length</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">only</span><span class="p">)</span>
<a name="cl-2365"></a>  
<a name="cl-2366"></a>  <span class="k">def</span> <span class="nf">number</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2367"></a>    <span class="k">return</span> <span class="n">toNumber</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">string</span><span class="p">())</span>
<a name="cl-2368"></a>  
<a name="cl-2369"></a>  <span class="k">def</span> <span class="nf">iterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">reverse</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
<a name="cl-2370"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
<a name="cl-2371"></a>    <span class="n">_info</span><span class="o">=</span><span class="n">ExtDict</span><span class="p">({</span>
<a name="cl-2372"></a>      <span class="s">&#39;nodeset&#39;</span><span class="p">:</span><span class="bp">self</span>
<a name="cl-2373"></a>    <span class="p">,</span> <span class="s">&#39;count&#39;</span><span class="p">:</span><span class="mi">0</span>
<a name="cl-2374"></a>    <span class="p">})</span>
<a name="cl-2375"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">reverse</span><span class="p">:</span>
<a name="cl-2376"></a>      <span class="n">calcIndex</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">:</span><span class="n">x</span><span class="p">)</span>
<a name="cl-2377"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2378"></a>      <span class="n">calcIndex</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">:</span><span class="n">y</span><span class="o">.</span><span class="n">length</span><span class="o">-</span><span class="n">x</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-2379"></a>    <span class="k">def</span> <span class="nf">iter</span><span class="p">():</span>
<a name="cl-2380"></a>      <span class="n">nodeset</span><span class="o">=</span><span class="n">_info</span><span class="o">.</span><span class="n">nodeset</span>
<a name="cl-2381"></a>      <span class="n">index</span><span class="o">=</span><span class="n">calcIndex</span><span class="p">(</span><span class="n">_info</span><span class="o">.</span><span class="n">count</span><span class="p">,</span><span class="n">nodeset</span><span class="p">)</span>
<a name="cl-2382"></a>      <span class="n">_info</span><span class="p">[</span><span class="s">&#39;count&#39;</span><span class="p">]</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2383"></a>      <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">nodeset</span><span class="p">,</span><span class="s">&#39;only&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">and</span> <span class="n">index</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-2384"></a>        <span class="k">return</span> <span class="n">nodeset</span><span class="o">.</span><span class="n">only</span>
<a name="cl-2385"></a>      <span class="k">return</span> <span class="n">nodeset</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="k">if</span> <span class="mi">0</span><span class="o">&lt;=</span><span class="n">index</span> <span class="ow">and</span> <span class="n">index</span><span class="o">&lt;</span><span class="nb">len</span><span class="p">(</span><span class="n">nodeset</span><span class="o">.</span><span class="n">nodes</span><span class="p">)</span> <span class="k">else</span> <span class="bp">None</span>
<a name="cl-2386"></a>    <span class="k">return</span> <span class="nb">iter</span>
<a name="cl-2387"></a>
<a name="cl-2388"></a>  <span class="k">class</span> <span class="nc">nodeID</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-2389"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2390"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">uuid</span><span class="o">=</span><span class="mi">1</span>
<a name="cl-2391"></a>    
<a name="cl-2392"></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">):</span>
<a name="cl-2393"></a>      <span class="nb">id</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;__bsxpath_id__&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-2394"></a>      <span class="k">if</span> <span class="nb">id</span><span class="p">:</span>
<a name="cl-2395"></a>        <span class="k">return</span> <span class="nb">id</span>
<a name="cl-2396"></a>      <span class="nb">id</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">__bsxpath_id__</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">uuid</span>
<a name="cl-2397"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">uuid</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2398"></a>      <span class="k">return</span> <span class="nb">id</span>
<a name="cl-2399"></a>  
<a name="cl-2400"></a>  <span class="n">NodeID</span><span class="o">=</span><span class="n">nodeID</span><span class="p">()</span>
<a name="cl-2401"></a>  
<a name="cl-2402"></a><span class="c">#} // end of NodeSet</span>
<a name="cl-2403"></a>
<a name="cl-2404"></a>
<a name="cl-2405"></a><span class="c">#{ // XPathEvaluator</span>
<a name="cl-2406"></a><span class="k">class</span> <span class="nc">XPathResult</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-2407"></a>  <span class="n">ANY_TYPE</span>                    <span class="o">=</span><span class="mi">0</span>
<a name="cl-2408"></a>  <span class="n">NUMBER_TYPE</span>                 <span class="o">=</span><span class="mi">1</span>
<a name="cl-2409"></a>  <span class="n">STRING_TYPE</span>                 <span class="o">=</span><span class="mi">2</span>
<a name="cl-2410"></a>  <span class="n">BOOLEAN_TYPE</span>                <span class="o">=</span><span class="mi">3</span>
<a name="cl-2411"></a>  <span class="n">UNORDERED_NODE_ITERATOR_TYPE</span><span class="o">=</span><span class="mi">4</span>
<a name="cl-2412"></a>  <span class="n">ORDERED_NODE_ITERATOR_TYPE</span>  <span class="o">=</span><span class="mi">5</span>
<a name="cl-2413"></a>  <span class="n">UNORDERED_NODE_SNAPSHOT_TYPE</span><span class="o">=</span><span class="mi">6</span>
<a name="cl-2414"></a>  <span class="n">ORDERED_NODE_SNAPSHOT_TYPE</span>  <span class="o">=</span><span class="mi">7</span>
<a name="cl-2415"></a>  <span class="n">ANY_UNORDERED_NODE_TYPE</span>     <span class="o">=</span><span class="mi">8</span>
<a name="cl-2416"></a>  <span class="n">FIRST_ORDERED_NODE_TYPE</span>     <span class="o">=</span><span class="mi">9</span>
<a name="cl-2417"></a>  
<a name="cl-2418"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">value</span><span class="p">,</span><span class="nb">type</span><span class="p">):</span>
<a name="cl-2419"></a>    <span class="k">if</span> <span class="nb">type</span><span class="o">==</span><span class="n">XPathResult</span><span class="o">.</span><span class="n">ANY_TYPE</span><span class="p">:</span>
<a name="cl-2420"></a>      <span class="n">tov</span><span class="o">=</span><span class="n">typeof</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
<a name="cl-2421"></a>      <span class="k">if</span> <span class="n">tov</span><span class="o">==</span><span class="s">&#39;object&#39;</span> <span class="p">:</span> <span class="nb">type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">UNORDERED_NODE_ITERATOR_TYPE</span>
<a name="cl-2422"></a>      <span class="k">if</span> <span class="n">tov</span><span class="o">==</span><span class="s">&#39;boolean&#39;</span><span class="p">:</span> <span class="nb">type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">BOOLEAN_TYPE</span>
<a name="cl-2423"></a>      <span class="k">if</span> <span class="n">tov</span><span class="o">==</span><span class="s">&#39;string&#39;</span> <span class="p">:</span> <span class="nb">type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">STRING_TYPE</span>
<a name="cl-2424"></a>      <span class="k">if</span> <span class="n">tov</span><span class="o">==</span><span class="s">&#39;number&#39;</span> <span class="p">:</span> <span class="nb">type</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">NUMBER_TYPE</span>
<a name="cl-2425"></a>    
<a name="cl-2426"></a>    <span class="k">if</span> <span class="nb">type</span><span class="o">&lt;</span><span class="bp">self</span><span class="o">.</span><span class="n">NUMBER_TYPE</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">FIRST_ORDERED_NODE_TYPE</span><span class="o">&lt;</span><span class="nb">type</span><span class="p">:</span>
<a name="cl-2427"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;unknown type: </span><span class="si">%d</span><span class="s">&#39;</span> <span class="o">%</span><span class="p">(</span><span class="nb">type</span><span class="p">))</span>
<a name="cl-2428"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">resultType</span><span class="o">=</span><span class="nb">type</span>
<a name="cl-2429"></a>    
<a name="cl-2430"></a>    <span class="k">if</span> <span class="nb">type</span><span class="o">==</span><span class="bp">self</span><span class="o">.</span><span class="n">NUMBER_TYPE</span><span class="p">:</span>
<a name="cl-2431"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">numberValue</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">number</span><span class="p">()</span> <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">value</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="k">else</span> <span class="n">toNumber</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
<a name="cl-2432"></a>    <span class="k">elif</span> <span class="nb">type</span><span class="o">==</span><span class="bp">self</span><span class="o">.</span><span class="n">STRING_TYPE</span><span class="p">:</span>
<a name="cl-2433"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">stringValue</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">string</span><span class="p">()</span> <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">value</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="k">else</span> <span class="n">toString</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
<a name="cl-2434"></a>    <span class="k">elif</span> <span class="nb">type</span><span class="o">==</span><span class="bp">self</span><span class="o">.</span><span class="n">BOOLEAN_TYPE</span><span class="p">:</span>
<a name="cl-2435"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">booleanValue</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">bool</span><span class="p">()</span> <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">value</span><span class="p">,</span><span class="s">&#39;isNodeSet&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="k">else</span> <span class="n">toBoolean</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
<a name="cl-2436"></a>    <span class="k">elif</span> <span class="nb">type</span><span class="o">==</span><span class="bp">self</span><span class="o">.</span><span class="n">ANY_UNORDERED_NODE_TYPE</span> <span class="ow">or</span> <span class="nb">type</span><span class="o">==</span><span class="bp">self</span><span class="o">.</span><span class="n">FIRST_ORDERED_NODE_TYPE</span><span class="p">:</span>
<a name="cl-2437"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">singleNodeValue</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">first</span><span class="p">()</span>
<a name="cl-2438"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2439"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">list</span><span class="p">()</span>
<a name="cl-2440"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">snapshotLength</span><span class="o">=</span><span class="n">value</span><span class="o">.</span><span class="n">length</span>
<a name="cl-2441"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">=</span><span class="mi">0</span>
<a name="cl-2442"></a>      <span class="bp">self</span><span class="o">.</span><span class="n">invalidIteratorState</span><span class="o">=</span><span class="bp">False</span>
<a name="cl-2443"></a>  
<a name="cl-2444"></a>  <span class="k">def</span> <span class="nf">iterateNext</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2445"></a>    <span class="n">node</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="p">]</span>
<a name="cl-2446"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">index</span><span class="o">+=</span><span class="mi">1</span>
<a name="cl-2447"></a>    <span class="k">return</span> <span class="n">node</span>
<a name="cl-2448"></a>  
<a name="cl-2449"></a>  <span class="k">def</span> <span class="nf">snapshotItem</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">i</span><span class="p">):</span>
<a name="cl-2450"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<a name="cl-2451"></a>  
<a name="cl-2452"></a>
<a name="cl-2453"></a><span class="k">class</span> <span class="nc">XPathExpression</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-2454"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">expr</span><span class="p">,</span><span class="n">resolver</span><span class="p">):</span>
<a name="cl-2455"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span><span class="o">&lt;=</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-2456"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;no expression&#39;</span><span class="p">)</span>
<a name="cl-2457"></a>    <span class="n">lexer</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">lexer</span><span class="o">=</span><span class="n">Lexer</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-2458"></a>    
<a name="cl-2459"></a>    <span class="k">if</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-2460"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;no expression&#39;</span><span class="p">)</span>
<a name="cl-2461"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">expr</span><span class="o">=</span><span class="n">BinaryExpr</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">lexer</span><span class="p">)</span>
<a name="cl-2462"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">lexer</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
<a name="cl-2463"></a>      <span class="n">throwError</span><span class="p">(</span><span class="s">u&#39;bad token: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">lexer</span><span class="o">.</span><span class="n">next</span><span class="p">()))</span>
<a name="cl-2464"></a>  
<a name="cl-2465"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">node</span><span class="p">,</span><span class="nb">type</span><span class="p">):</span>
<a name="cl-2466"></a>    <span class="k">return</span> <span class="n">XPathResult</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">expr</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">Ctx</span><span class="p">(</span><span class="n">node</span><span class="p">)),</span><span class="nb">type</span><span class="p">)</span>
<a name="cl-2467"></a>
<a name="cl-2468"></a>
<a name="cl-2469"></a><span class="k">class</span> <span class="nc">BSXPathEvaluator</span><span class="p">(</span><span class="n">BeautifulSoup</span><span class="p">):</span>
<a name="cl-2470"></a>  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
<a name="cl-2471"></a>    <span class="n">BeautifulSoup</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
<a name="cl-2472"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">_string</span><span class="o">=</span><span class="s">u&#39;[object HTMLDocument]&#39;</span>
<a name="cl-2473"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">_fix_table</span><span class="p">()</span>
<a name="cl-2474"></a>    
<a name="cl-2475"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">_init_index</span><span class="p">()</span>
<a name="cl-2476"></a>    
<a name="cl-2477"></a>  <span class="n">SELF_CLOSING_TAGS</span><span class="o">=</span><span class="n">buildTagMap</span><span class="p">(</span><span class="bp">None</span><span class="p">,[</span><span class="s">&#39;br&#39;</span><span class="p">,</span><span class="s">&#39;hr&#39;</span><span class="p">,</span><span class="s">&#39;input&#39;</span><span class="p">,</span><span class="s">&#39;img&#39;</span><span class="p">,</span><span class="s">&#39;meta&#39;</span><span class="p">,</span><span class="s">&#39;spacer&#39;</span><span class="p">,</span><span class="s">&#39;frame&#39;</span><span class="p">,</span><span class="s">&#39;base&#39;</span><span class="p">])</span>
<a name="cl-2478"></a>  <span class="c"># exclude &#39;link&#39; for XML</span>
<a name="cl-2479"></a>  
<a name="cl-2480"></a>  <span class="k">def</span> <span class="nf">_init_index</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2481"></a>    <span class="n">idx</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_sortindex</span><span class="o">=</span><span class="mi">1</span>
<a name="cl-2482"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">_cachemap</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2483"></a>    
<a name="cl-2484"></a>    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">NodeUtilBS</span><span class="o">.</span><span class="n">it_deepNodes</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2485"></a>      <span class="n">idx</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">_sortindex</span><span class="o">=</span><span class="n">idx</span><span class="o">+</span><span class="mi">1</span>
<a name="cl-2486"></a>    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">findAll</span><span class="p">():</span>
<a name="cl-2487"></a>      <span class="n">node</span><span class="o">.</span><span class="n">attrMap</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">attrs</span><span class="p">)</span>
<a name="cl-2488"></a>  
<a name="cl-2489"></a>  <span class="k">def</span> <span class="nf">_fix_table</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2490"></a>    <span class="n">tables</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">findAll</span><span class="p">(</span><span class="s">&#39;table&#39;</span><span class="p">)</span>
<a name="cl-2491"></a>    <span class="k">for</span> <span class="n">table</span> <span class="ow">in</span> <span class="n">tables</span><span class="p">:</span>
<a name="cl-2492"></a>      <span class="n">parent</span><span class="o">=</span><span class="n">table</span><span class="o">.</span><span class="n">parent</span>
<a name="cl-2493"></a>      <span class="n">contents</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">table</span><span class="p">,</span><span class="s">&#39;contents&#39;</span><span class="p">,[])</span>
<a name="cl-2494"></a>      <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">contents</span><span class="p">)</span><span class="o">&lt;=</span><span class="mi">0</span><span class="p">:</span> <span class="k">continue</span>
<a name="cl-2495"></a>      <span class="p">(</span><span class="n">tbody</span><span class="p">,</span><span class="n">tr</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-2496"></a>      <span class="n">node</span><span class="o">=</span><span class="n">table</span><span class="o">.</span><span class="n">contents</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2497"></a>      <span class="k">while</span> <span class="n">node</span><span class="p">:</span>
<a name="cl-2498"></a>        <span class="n">_next</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">nextSibling</span>
<a name="cl-2499"></a>        <span class="n">name</span><span class="o">=</span><span class="nb">getattr</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s">&#39;name&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-2500"></a>        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;thead&#39;</span><span class="p">,</span><span class="s">&#39;tbody&#39;</span><span class="p">,</span><span class="s">&#39;tfoot&#39;</span><span class="p">,):</span>
<a name="cl-2501"></a>          <span class="p">(</span><span class="n">tbody</span><span class="p">,</span><span class="n">tr</span><span class="p">)</span><span class="o">=</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-2502"></a>        <span class="k">elif</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;tr&#39;</span><span class="p">,):</span>
<a name="cl-2503"></a>          <span class="n">tr</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2504"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">tbody</span><span class="p">:</span>
<a name="cl-2505"></a>            <span class="n">tbody</span><span class="o">=</span><span class="n">Tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;tbody&#39;</span><span class="p">)</span>
<a name="cl-2506"></a>            <span class="n">table</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">table</span><span class="o">.</span><span class="n">contents</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">node</span><span class="p">),</span><span class="n">tbody</span><span class="p">)</span>
<a name="cl-2507"></a>          <span class="n">tbody</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2508"></a>        <span class="k">elif</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;th&#39;</span><span class="p">,</span><span class="s">&#39;td&#39;</span><span class="p">,):</span>
<a name="cl-2509"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">tbody</span><span class="p">:</span>
<a name="cl-2510"></a>            <span class="n">tbody</span><span class="o">=</span><span class="n">Tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;tbody&#39;</span><span class="p">)</span>
<a name="cl-2511"></a>            <span class="n">table</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">table</span><span class="o">.</span><span class="n">contents</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">node</span><span class="p">),</span><span class="n">tbody</span><span class="p">)</span>
<a name="cl-2512"></a>          <span class="k">if</span> <span class="ow">not</span> <span class="n">tr</span><span class="p">:</span>
<a name="cl-2513"></a>            <span class="n">tr</span><span class="o">=</span><span class="n">Tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="s">&#39;tr&#39;</span><span class="p">)</span>
<a name="cl-2514"></a>            <span class="n">tbody</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tr</span><span class="p">)</span>
<a name="cl-2515"></a>          <span class="n">tr</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2516"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-2517"></a>          <span class="n">parent</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">parent</span><span class="o">.</span><span class="n">contents</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">table</span><span class="p">),</span><span class="n">node</span><span class="p">)</span>
<a name="cl-2518"></a>        <span class="n">node</span><span class="o">=</span><span class="n">_next</span>
<a name="cl-2519"></a>  
<a name="cl-2520"></a>  <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">encoding</span><span class="o">=</span><span class="n">DEFAULT_OUTPUT_ENCODING</span><span class="p">):</span>
<a name="cl-2521"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_string</span>
<a name="cl-2522"></a>  
<a name="cl-2523"></a>  <span class="k">def</span> <span class="nf">__unicode__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2524"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_string</span>
<a name="cl-2525"></a>  
<a name="cl-2526"></a>  <span class="k">def</span> <span class="nf">decode</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-2527"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_string</span>
<a name="cl-2528"></a>  
<a name="cl-2529"></a>  <span class="k">def</span> <span class="nf">createExpression</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">expr</span><span class="p">,</span><span class="n">resolver</span><span class="p">):</span>
<a name="cl-2530"></a>    <span class="k">return</span> <span class="n">XPathExpression</span><span class="p">(</span><span class="n">expr</span><span class="p">,</span><span class="n">resolver</span><span class="p">)</span>
<a name="cl-2531"></a>  
<a name="cl-2532"></a>  <span class="k">def</span> <span class="nf">createNSResolver</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">nodeResolver</span><span class="p">):</span>
<a name="cl-2533"></a>    <span class="c"># not implemented</span>
<a name="cl-2534"></a>    <span class="k">pass</span>
<a name="cl-2535"></a>  
<a name="cl-2536"></a>  <span class="k">def</span> <span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">expr</span><span class="p">,</span><span class="n">context</span><span class="p">,</span><span class="n">resolver</span><span class="p">,</span><span class="nb">type</span><span class="p">,</span><span class="n">result</span><span class="p">):</span>
<a name="cl-2537"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">context</span><span class="p">:</span>
<a name="cl-2538"></a>      <span class="n">context</span><span class="o">=</span><span class="bp">self</span>
<a name="cl-2539"></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">context</span><span class="p">,</span><span class="nb">list</span><span class="p">):</span>
<a name="cl-2540"></a>      <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-2541"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">createExpression</span><span class="p">(</span><span class="n">expr</span><span class="p">,</span><span class="n">resolver</span><span class="p">)</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">context</span><span class="p">,</span><span class="nb">type</span><span class="p">)</span>
<a name="cl-2542"></a>  
<a name="cl-2543"></a>  <span class="k">def</span> <span class="nf">getItemList</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">expr</span><span class="p">,</span><span class="n">context</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2544"></a>    <span class="n">elms</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-2545"></a>    <span class="n">result</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">expr</span><span class="p">,</span><span class="n">context</span><span class="p">,</span><span class="bp">None</span><span class="p">,</span><span class="n">XPathResult</span><span class="o">.</span><span class="n">ORDERED_NODE_SNAPSHOT_TYPE</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-2546"></a>    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">result</span><span class="o">.</span><span class="n">snapshotLength</span><span class="p">):</span>
<a name="cl-2547"></a>      <span class="n">elms</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">snapshotItem</span><span class="p">(</span><span class="n">i</span><span class="p">))</span>
<a name="cl-2548"></a>    <span class="k">return</span> <span class="n">elms</span>
<a name="cl-2549"></a>  
<a name="cl-2550"></a>  <span class="k">def</span> <span class="nf">getFirstItem</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">expr</span><span class="p">,</span><span class="n">context</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-2551"></a>    <span class="n">elm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">expr</span><span class="p">,</span><span class="n">context</span><span class="p">,</span><span class="bp">None</span><span class="p">,</span><span class="n">XPathResult</span><span class="o">.</span><span class="n">FIRST_ORDERED_NODE_TYPE</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span><span class="o">.</span><span class="n">singleNodeValue</span>
<a name="cl-2552"></a>    <span class="k">return</span> <span class="n">elm</span>
<a name="cl-2553"></a>  
<a name="cl-2554"></a>  <span class="k">def</span> <span class="nf">applyXPath</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">context</span><span class="p">,</span><span class="n">expr</span><span class="p">):</span>
<a name="cl-2555"></a>    <span class="n">start_t</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span>
<a name="cl-2556"></a>    <span class="n">expression</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">createExpression</span><span class="p">(</span><span class="n">expr</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-2557"></a>    <span class="n">result</span><span class="o">=</span><span class="n">expression</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">context</span><span class="p">,</span><span class="n">XPathResult</span><span class="o">.</span><span class="n">ANY_TYPE</span><span class="p">)</span>
<a name="cl-2558"></a>    <span class="n">time</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">-</span><span class="n">start_t</span>
<a name="cl-2559"></a>    
<a name="cl-2560"></a>    <span class="n">resultType</span><span class="o">=</span><span class="n">result</span><span class="o">.</span><span class="n">resultType</span>
<a name="cl-2561"></a>    <span class="k">if</span> <span class="n">XPathResult</span><span class="o">.</span><span class="n">BOOLEAN_TYPE</span><span class="o">&lt;</span><span class="n">resultType</span><span class="p">:</span>
<a name="cl-2562"></a>      <span class="n">result</span><span class="o">=</span><span class="n">expression</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">context</span><span class="p">,</span><span class="n">XPathResult</span><span class="o">.</span><span class="n">ORDERED_NODE_SNAPSHOT_TYPE</span><span class="p">)</span>
<a name="cl-2563"></a>      <span class="n">array</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-2564"></a>      <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">result</span><span class="o">.</span><span class="n">snapshotLength</span><span class="p">):</span>
<a name="cl-2565"></a>        <span class="n">array</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">snapshotItem</span><span class="p">(</span><span class="n">i</span><span class="p">))</span>
<a name="cl-2566"></a>      <span class="n">resultItems</span><span class="o">=</span><span class="n">array</span>
<a name="cl-2567"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2568"></a>      <span class="k">if</span> <span class="n">resultType</span><span class="o">==</span><span class="n">XPathResult</span><span class="o">.</span><span class="n">NUMBER_TYPE</span><span class="p">:</span>
<a name="cl-2569"></a>        <span class="n">resultItems</span><span class="o">=</span><span class="n">result</span><span class="o">.</span><span class="n">numberValue</span>
<a name="cl-2570"></a>      <span class="k">elif</span> <span class="n">resultType</span><span class="o">==</span><span class="n">XPathResult</span><span class="o">.</span><span class="n">STRING_TYPE</span><span class="p">:</span>
<a name="cl-2571"></a>        <span class="n">resultItems</span><span class="o">=</span><span class="n">result</span><span class="o">.</span><span class="n">stringValue</span>
<a name="cl-2572"></a>      <span class="k">elif</span> <span class="n">resultType</span><span class="o">==</span><span class="n">XPathResult</span><span class="o">.</span><span class="n">BOOLEAN_TYPE</span><span class="p">:</span>
<a name="cl-2573"></a>        <span class="n">resultItems</span><span class="o">=</span><span class="n">result</span><span class="o">.</span><span class="n">booleanValue</span>
<a name="cl-2574"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-2575"></a>        <span class="n">resultItems</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2576"></a>    
<a name="cl-2577"></a>    <span class="k">return</span> <span class="p">(</span><span class="n">resultItems</span><span class="p">,</span><span class="n">time</span><span class="p">,</span><span class="n">resultType</span><span class="p">)</span>
<a name="cl-2578"></a>  
<a name="cl-2579"></a>
<a name="cl-2580"></a><span class="c">#} // end of XPathEvaluator</span>
<a name="cl-2581"></a>
<a name="cl-2582"></a>
<a name="cl-2583"></a>
<a name="cl-2584"></a><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
<a name="cl-2585"></a>  <span class="kn">import</span> <span class="nn">sys</span>
<a name="cl-2586"></a>  <span class="kn">import</span> <span class="nn">optparse</span>
<a name="cl-2587"></a>  <span class="kn">import</span> <span class="nn">pdb</span>
<a name="cl-2588"></a>  
<a name="cl-2589"></a>  <span class="n">options</span><span class="o">=</span><span class="bp">None</span>
<a name="cl-2590"></a>  
<a name="cl-2591"></a>  <span class="k">def</span> <span class="nf">prn</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
<a name="cl-2592"></a>    <span class="k">def</span> <span class="nf">prn_sub</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="n">indent</span><span class="p">):</span>
<a name="cl-2593"></a>      <span class="n">indent</span><span class="o">+=</span><span class="s">u&#39;  &#39;</span>
<a name="cl-2594"></a>      <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">list</span><span class="p">):</span>
<a name="cl-2595"></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">obj</span><span class="p">)):</span>
<a name="cl-2596"></a>          <span class="k">print</span> <span class="s">u&#39;[</span><span class="si">%d</span><span class="s">]&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">i</span><span class="p">)</span>
<a name="cl-2597"></a>          <span class="n">prn_sub</span><span class="p">(</span><span class="n">obj</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-2598"></a>      <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">dict</span><span class="p">):</span>
<a name="cl-2599"></a>        <span class="k">for</span> <span class="n">mem</span> <span class="ow">in</span> <span class="n">obj</span><span class="p">:</span>
<a name="cl-2600"></a>          <span class="k">print</span> <span class="s">u&#39;[</span><span class="si">%s</span><span class="s">]&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">mem</span><span class="p">)</span>
<a name="cl-2601"></a>          <span class="n">prn_sub</span><span class="p">(</span><span class="n">obj</span><span class="p">[</span><span class="n">mem</span><span class="p">],</span><span class="n">indent</span><span class="p">)</span>
<a name="cl-2602"></a>      <span class="k">elif</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="s">&#39;nodeType&#39;</span><span class="p">,</span><span class="bp">None</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="nb">basestring</span><span class="p">):</span>
<a name="cl-2603"></a>        <span class="nb">str</span><span class="o">=</span><span class="n">indent</span><span class="o">+</span><span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">r&#39;([\r?\n])&#39;</span><span class="p">,</span><span class="s">r&#39;\1&#39;</span><span class="o">+</span><span class="n">indent</span><span class="p">,</span><span class="nb">unicode</span><span class="p">(</span><span class="n">obj</span><span class="p">))</span>
<a name="cl-2604"></a>        <span class="k">print</span> <span class="nb">str</span>
<a name="cl-2605"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-2606"></a>        <span class="k">print</span> <span class="n">obj</span>
<a name="cl-2607"></a>    <span class="n">prn_sub</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span><span class="s">u&#39;&#39;</span><span class="p">)</span>
<a name="cl-2608"></a>  
<a name="cl-2609"></a>  <span class="k">def</span> <span class="nf">test</span><span class="p">():</span>
<a name="cl-2610"></a>    <span class="k">global</span> <span class="n">options</span>
<a name="cl-2611"></a>    
<a name="cl-2612"></a>    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">expr</span><span class="p">:</span>
<a name="cl-2613"></a>      <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">html</span><span class="p">:</span>
<a name="cl-2614"></a>        <span class="n">document</span><span class="o">=</span><span class="n">BSXPathEvaluator</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">html</span><span class="p">)</span>
<a name="cl-2615"></a>      <span class="k">elif</span> <span class="n">options</span><span class="o">.</span><span class="n">file</span><span class="p">:</span>
<a name="cl-2616"></a>        <span class="n">fp</span><span class="o">=</span><span class="nb">open</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">file</span><span class="p">)</span>
<a name="cl-2617"></a>        <span class="n">document</span><span class="o">=</span><span class="n">BSXPathEvaluator</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
<a name="cl-2618"></a>        <span class="n">fp</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
<a name="cl-2619"></a>      <span class="k">else</span><span class="p">:</span>
<a name="cl-2620"></a>        <span class="n">document</span><span class="o">=</span><span class="n">BSXPathEvaluator</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
<a name="cl-2621"></a>      
<a name="cl-2622"></a>      <span class="p">(</span><span class="n">result</span><span class="p">,</span><span class="n">time</span><span class="p">,</span><span class="n">resultType</span><span class="p">)</span><span class="o">=</span><span class="n">document</span><span class="o">.</span><span class="n">applyXPath</span><span class="p">(</span><span class="n">document</span><span class="p">,</span><span class="n">options</span><span class="o">.</span><span class="n">expr</span><span class="p">)</span>
<a name="cl-2623"></a>      
<a name="cl-2624"></a>      <span class="n">prn</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
<a name="cl-2625"></a>      
<a name="cl-2626"></a>    <span class="k">else</span><span class="p">:</span>
<a name="cl-2627"></a>      <span class="n">optparser</span><span class="o">.</span><span class="n">print_help</span><span class="p">()</span>
<a name="cl-2628"></a>  
<a name="cl-2629"></a>  <span class="n">optparser</span><span class="o">=</span><span class="n">optparse</span><span class="o">.</span><span class="n">OptionParser</span><span class="p">()</span>
<a name="cl-2630"></a>  <span class="n">optparser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span>
<a name="cl-2631"></a>    <span class="s">&#39;-e&#39;</span><span class="p">,</span><span class="s">&#39;--expr&#39;</span>
<a name="cl-2632"></a>  <span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store&#39;</span>
<a name="cl-2633"></a>  <span class="p">,</span> <span class="n">metavar</span><span class="o">=</span><span class="s">&#39;&lt;expression&gt;&#39;</span>
<a name="cl-2634"></a>  <span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">u&#39;expression: XPATH expression&#39;</span>
<a name="cl-2635"></a>  <span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;expr&#39;</span>
<a name="cl-2636"></a>  <span class="p">)</span>
<a name="cl-2637"></a>  <span class="n">optparser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span>
<a name="cl-2638"></a>    <span class="s">&#39;-t&#39;</span><span class="p">,</span><span class="s">&#39;--html&#39;</span>
<a name="cl-2639"></a>  <span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store&#39;</span>
<a name="cl-2640"></a>  <span class="p">,</span> <span class="n">metavar</span><span class="o">=</span><span class="s">&#39;&lt;text&gt;&#39;</span>
<a name="cl-2641"></a>  <span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">u&#39;text: HTML text&#39;</span>
<a name="cl-2642"></a>  <span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;html&#39;</span>
<a name="cl-2643"></a>  <span class="p">)</span>
<a name="cl-2644"></a>  <span class="n">optparser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span>
<a name="cl-2645"></a>    <span class="s">&#39;-f&#39;</span><span class="p">,</span><span class="s">&#39;--file&#39;</span>
<a name="cl-2646"></a>  <span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store&#39;</span>
<a name="cl-2647"></a>  <span class="p">,</span> <span class="n">metavar</span><span class="o">=</span><span class="s">&#39;&lt;filename&gt;&#39;</span>
<a name="cl-2648"></a>  <span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">u&#39;filename: HTML filename&#39;</span>
<a name="cl-2649"></a>  <span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;file&#39;</span>
<a name="cl-2650"></a>  <span class="p">)</span>
<a name="cl-2651"></a>  <span class="n">optparser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span>
<a name="cl-2652"></a>    <span class="s">&#39;-d&#39;</span><span class="p">,</span><span class="s">&#39;--debug&#39;</span>
<a name="cl-2653"></a>  <span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span>
<a name="cl-2654"></a>  <span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">u&#39;use pdb&#39;</span>
<a name="cl-2655"></a>  <span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;debug&#39;</span>
<a name="cl-2656"></a>  <span class="p">)</span>
<a name="cl-2657"></a>  <span class="p">(</span><span class="n">options</span><span class="p">,</span><span class="n">args</span><span class="p">)</span><span class="o">=</span><span class="n">optparser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<a name="cl-2658"></a>  
<a name="cl-2659"></a>  <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">debug</span><span class="p">:</span>
<a name="cl-2660"></a>    <span class="n">pdb</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="s">&#39;test()&#39;</span><span class="p">)</span> 
<a name="cl-2661"></a>  <span class="k">else</span><span class="p">:</span>
<a name="cl-2662"></a>    <span class="n">test</span><span class="p">()</span>
<a name="cl-2663"></a>  
<a name="cl-2664"></a><span class="c">#[History]</span>
<a name="cl-2665"></a><span class="c">#</span>
<a name="cl-2666"></a><span class="c">#  0.01e: 2009-04-12</span>
<a name="cl-2667"></a><span class="c">#    - exclude &#39;link&#39; tag from SELF_CLOSING_TAGS (for XML)</span>
<a name="cl-2668"></a><span class="c">#    - add __str__() and __unicode__() to AttributeWrapper class</span>
<a name="cl-2669"></a><span class="c">#  </span>
<a name="cl-2670"></a><span class="c">#  0.01d: 2009-03-28</span>
<a name="cl-2671"></a><span class="c">#    - performance improvement: node searching(make attrMap in advance)</span>
<a name="cl-2672"></a><span class="c">#  </span>
<a name="cl-2673"></a><span class="c">#  0.01c: 2009-03-28</span>
<a name="cl-2674"></a><span class="c">#    - performance improvement: node sorting(indexing) and node search(caching)</span>
<a name="cl-2675"></a><span class="c"># </span>
<a name="cl-2676"></a><span class="c">#  0.01b: 2009-03-27</span>
<a name="cl-2677"></a><span class="c">#    - fixed &#39;singleNodeValue&#39; bug</span>
<a name="cl-2678"></a><span class="c">#      result = document.evaluate(&#39;//title[1]&#39;,document,None,XPathResult.FIRST_ORDERED_NODE_TYPE,None).singleNodeValue</span>
<a name="cl-2679"></a><span class="c">#      # returnd &#39;None&#39;, even though first-value exists</span>
<a name="cl-2680"></a><span class="c"># </span>
<a name="cl-2681"></a><span class="c">#  0.01a: 2009-03-27</span>
<a name="cl-2682"></a><span class="c">#    - fixed string() bug</span>
<a name="cl-2683"></a><span class="c">#      BSXPath.py -e &quot;boolean(//p[contains(string(),\&quot;br\&quot;)])&quot; -t &quot;&lt;html&gt;&lt;head&gt;&lt;/head&gt;&lt;body&gt;&lt;p&gt;text before&lt;br /&gt;text after&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;&quot;</span>
<a name="cl-2684"></a><span class="c">#      # returned &#39;True&#39;, even though &#39;False&#39; is right</span>
<a name="cl-2685"></a><span class="c">#    - cope with &lt;table&gt; problems on malformed HTML</span>
<a name="cl-2686"></a><span class="c">#      may convert &#39;&lt;table&gt;&lt;th&gt;&lt;/th&gt;&lt;td&gt;&lt;/td&gt;&lt;/table&gt;&#39; to &#39;&lt;table&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th&gt;&lt;/th&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&#39; automatically</span>
<a name="cl-2687"></a><span class="c"># </span>
<a name="cl-2688"></a><span class="c">#  0.01 : 2009-03-25</span>
<a name="cl-2689"></a><span class="c">#    first release</span>
<a name="cl-2690"></a><span class="c">#</span>
<a name="cl-2691"></a><span class="c">#■ End of BSXPath.py </span>
</pre></div>
</td></tr></table>
    </div>
  
  </div>
  



      </div>
    </div>

  </div>

  <div id="footer">
    <ul id="footer-nav">
      <li>Copyright © 2011 <a href="http://atlassian.com">Atlassian</a></li>
      <li><a href="http://www.atlassian.com/hosted/terms.jsp">Terms of Service</a></li>
      <li><a href="http://www.atlassian.com/about/privacy.jsp">Privacy</a></li>
      <li><a href="//bitbucket.org/site/master/issues/new">Report a Bug to Bitbucket</a></li>
      <li><a href="http://confluence.atlassian.com/x/IYBGDQ">API</a></li>
      <li><a href="http://status.bitbucket.org/">Server Status</a></li>
    </ul>
    <ul id="social-nav">
      <li class="blog"><a href="http://blog.bitbucket.org">Bitbucket Blog</a></li>
      <li class="twitter"><a href="http://www.twitter.com/bitbucket">Twitter</a></li>
    </ul>
    <h5>We run</h5>
    <ul id="technologies">
      <li><a href="http://www.djangoproject.com/">Django 1.3.0</a></li>
      <li><a href="//bitbucket.org/jespern/django-piston/">Piston 0.3dev</a></li>
      <li><a href="http://www.selenic.com/mercurial/">Hg 1.9.2</a></li>
      <li><a href="http://www.python.org">Python 2.7.2</a></li>
      <li>r13626:5578616a91c2 | bitbucket03</li>
    </ul>
  </div>

  <script src="https://dwz7u9t8u8usb.cloudfront.net/m/957a2f59c221/js/lib/global.js"></script>






  <script>
    BB.gaqPush(['_trackPageview']);
  
    BB.gaqPush(['atl._trackPageview']);

    

    

    (function () {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
    }());
  </script>

</body>
</html>
