<!DOCTYPE html>
<!-- saved from url=(0073)https://colab.research.google.com/drive/1e6dcDo4Ce7F16rYq84tmNkkuTZccM5ze -->
<html lang="en" theme="adaptive" style="--colab-code-font-family: monospace;" editor="Default Dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="Az520Inasey3TAyqLyojQa8MnmCALSEU29yQFW8dePZ7xQTvSt73pHazLFTK5f7SyLUJSo2uKLesEtEa9aUYcgMAAACPeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0="><meta http-equiv="origin-trial" content="Az520Inasey3TAyqLyojQa8MnmCALSEU29yQFW8dePZ7xQTvSt73pHazLFTK5f7SyLUJSo2uKLesEtEa9aUYcgMAAACPeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0="><style>body {transition: opacity ease-in 0.2s; } 
body[unresolved] {opacity: 0; display: block; overflow: hidden; position: relative; } 
</style><script type="text/javascript" async="" src="./titanic_survival_prediction_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-Q2b2vpMf3C0QrZfpTM4geXRY0PN3J9i8lz2SqOz69O++i1f8q41utGLlxcNBhzyi" nonce=""></script><script type="text/javascript" async="" src="./titanic_survival_prediction_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-Q2b2vpMf3C0QrZfpTM4geXRY0PN3J9i8lz2SqOz69O++i1f8q41utGLlxcNBhzyi" nonce=""></script><script type="text/javascript" async="" src="./titanic_survival_prediction_files/js" nonce=""></script><script src="./titanic_survival_prediction_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./titanic_survival_prediction_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./titanic_survival_prediction_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Untitled0.ipynb - Colaboratory</title><link href="./titanic_survival_prediction_files/css2" rel="stylesheet"><link href="./titanic_survival_prediction_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colaboratory"><style>.gb_gb:not(.gb_id){font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_xa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_xa:hover:after,a.gb_xa:focus:after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_xa:hover,a.gb_xa:focus{text-decoration:none}a.gb_xa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_ya{background-color:#4285f4;color:#fff}a.gb_ya:active{background-color:#0043b2}.gb_za{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_xa,.gb_ya,.gb_Aa,.gb_Ba{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Aa{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ba{background:#f8f8f8}.gb_Aa,#gb a.gb_Aa.gb_Aa,.gb_Ba{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ba{cursor:default;text-decoration:none}.gb_Ba{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ba{color:#fff}.gb_Ba:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ba:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Ca{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Ca:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Ca:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Ca:active,#gb .gb_Ca:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Ca.gb_i{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Ca.gb_i:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Ca.gb_i:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Ca.gb_i:active,#gb .gb_Ca.gb_i:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_p{display:none!important}.gb_1a{visibility:hidden}.gb_w{display:inline-block;vertical-align:middle}.gb_Rd .gb_o{bottom:-3px;right:-5px}.gb_f{position:relative}.gb_d{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_d{cursor:pointer;text-decoration:none}.gb_d,a.gb_d{color:#000}.gb_hf{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_if{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_if{border-bottom-color:#ccc}.gb_5{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_w.gb_La .gb_hf,.gb_w.gb_La .gb_if,.gb_w.gb_La .gb_5,.gb_La.gb_5{display:block}.gb_w.gb_La.gb_jf .gb_hf,.gb_w.gb_La.gb_jf .gb_if{display:none}.gb_Sd{position:absolute;right:8px;top:62px;z-index:-1}.gb_7a .gb_hf,.gb_7a .gb_if,.gb_7a .gb_5{margin-top:-10px}.gb_w:first-child,#gbsfw:first-child+.gb_w{padding-left:4px}.gb_Pa.gb_Td .gb_w:first-child{padding-left:0}.gb_Ud{position:relative}.gb_t.gb_Bd.gb_eb.gb_qd{margin:0 12px;padding:0}.gb_t .gb_d{position:relative}.gb_t .gb_w{margin:0 4px;padding:4px}.gb_t .gb_Vd{display:inline-block}.gb_t a.gb_md{-webkit-box-align:center;-webkit-align-items:center;-webkit-align-items:center;align-items:center;-webkit-border-radius:100px;border-radius:100px;border:0;background:#0b57d0;color:#fff;display:-webkit-inline-box;display:-webkit-inline-flex;display:-webkit-inline-box;display:-webkit-inline-flex;display:inline-flex;font-size:14px;font-weight:500;height:40px;white-space:nowrap;width:auto}.gb_t a.gb_d.gb_md{margin:0 4px;padding:4px 24px 4px 24px}.gb_t a.gb_md.gb_Wd{padding:9px 12px 9px 16px}.gb_t a.gb_md.gb_Xd{background:transparent;border:1px solid #747775;color:#0b57d0;outline:0}.gb_t .gb_s{fill:#0b57d0}.gb_t .gb_Zd{fill:#0b57d0;margin-left:8px}.gb_t .gb_Zd circle{fill:#fff}.gb_t .gb_md .gb_Kd{-webkit-box-flex:1;-webkit-flex-grow:1;-webkit-box-flex:1;box-flex:1;-webkit-flex-grow:1;flex-grow:1;text-align:center}.gb_t .gb_md:hover{background:#3763cd}.gb_t .gb_md:hover .gb_Zd{fill:#3763cd}.gb_t .gb_md:focus,.gb_t .gb_md:active,.gb_t .gb_md:focus:hover,.gb_t .gb_md[aria-expanded=true],.gb_t .gb_md:hover[aria-expanded=true]{background:#416acf}.gb_t .gb_md:focus .gb_Zd,.gb_t .gb_md:active .gb_Zd,.gb_t .gb_md:focus:hover .gb_Zd,.gb_t .gb_md[aria-expanded=true] .gb_Zd,.gb_t .gb_md:hover[aria-expanded=true] .gb_Zd{fill:#416acf}.gb_t .gb_md:focus,.gb_t .gb_md:active,.gb_t .gb_md[aria-expanded=true]{-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_t .gb_md:focus-visible{outline:1px solid #416acf;outline-offset:2px}.gb_t .gb_Fa:focus-visible{outline:1px solid #416acf}.gb_t .gb_i.gb_md{background:#a8c7fa;color:#062e6f}.gb_t .gb_i.gb_md .gb_Zd{fill:#a8c7fa}.gb_t .gb_i.gb_md .gb_Zd circle{fill:#062e6f}.gb_t .gb_i.gb_md:hover{background:#b4cbf6}.gb_t .gb_i.gb_md:hover .gb_Zd{fill:#b4cbf6}.gb_t .gb_i.gb_md:focus,.gb_t .gb_i.gb_md:focus:hover,.gb_t .gb_i.gb_md:active,.gb_t .gb_i.gb_md[aria-expanded=true],.gb_t .gb_i.gb_md:hover[aria-expanded=true]{background:#b8cdf7}.gb_t .gb_i.gb_md:focus .gb_Zd,.gb_t .gb_i.gb_md:focus:hover .gb_Zd,.gb_t .gb_i.gb_md:active .gb_Zd,.gb_t .gb_i.gb_md[aria-expanded=true] .gb_Zd,.gb_t .gb_i.gb_md:hover[aria-expanded=true] .gb_Zd{fill:#b8cdf7}.gb_t .gb_i.gb_md:focus-visible{outline-color:#b8cdf7}.gb_t .gb_i.gb_md:focus,.gb_t .gb_i.gb_md:active,.gb_t .gb_i.gb_md[aria-expanded=true]{-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_t .gb_md.gb_Xd:hover,.gb_t .gb_md.gb_Xd:focus,.gb_t .gb_md.gb_Xd[aria-expanded=true],.gb_t .gb_md.gb_Xd:hover[aria-expanded=true]{background:rgba(11,87,208,.08);-webkit-box-shadow:none;box-shadow:none}.gb_t .gb_md.gb_Xd:active{background:rgba(11,87,208,.12);-webkit-box-shadow:none;box-shadow:none}.gb_t .gb_md.gb_Xd:focus-visible{border-color:#0b57d0;outline:0}.gb_t .gb_i.gb_md.gb_Xd{background:transparent;color:#a8c7fa}.gb_t .gb_i.gb_md.gb_Xd:hover,.gb_t .gb_i.gb_md.gb_Xd:focus,.gb_t .gb_i.gb_md.gb_Xd[aria-expanded=true],.gb_t .gb_i.gb_md.gb_Xd:hover[aria-expanded=true]{background:rgba(168,199,250,.08);-webkit-box-shadow:none;box-shadow:none}.gb_t .gb_i.gb_md.gb_Xd:active{background:rgba(168,199,250,.12);-webkit-box-shadow:none;box-shadow:none}.gb_t .gb_i.gb_md.gb_Xd:focus-visible{border-color:#a8c7fa;outline:0}.gb_i .gb_t .gb_s{fill:#a8c7fa}.gb_i .gb_t .gb_Fa:focus-visible{outline-color:#a8c7fa}.gb_5c .gb_Ud,.gb_ld .gb_Ud{float:right}.gb_d{padding:8px;cursor:pointer}.gb_d:after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Pa .gb_me:not(.gb_xa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_0d button svg,.gb_d{-webkit-border-radius:50%;border-radius:50%}.gb_0d button:focus:not(:focus-visible) svg,.gb_0d button:hover svg,.gb_0d button:active svg,.gb_d:focus:not(:focus-visible),.gb_d:hover,.gb_d:active,.gb_d[aria-expanded=true]{outline:none}.gb_Oc .gb_0d.gb_ve button:focus-visible svg,.gb_0d button:focus-visible svg,.gb_d:focus-visible{outline:1px solid #202124}.gb_Oc .gb_0d button:focus-visible svg,.gb_Oc .gb_d:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Oc .gb_0d.gb_ve button:focus-visible svg,.gb_0d button:focus-visible svg,.gb_Oc .gb_0d button:focus-visible svg{outline:1px solid currentcolor}}.gb_Oc .gb_0d.gb_ve button:focus svg,.gb_Oc .gb_0d.gb_ve button:focus:hover svg,.gb_0d button:focus svg,.gb_0d button:focus:hover svg,.gb_d:focus,.gb_d:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Oc .gb_0d.gb_ve button:active svg,.gb_0d button:active svg,.gb_d:active{background-color:rgba(60,64,67,.12)}.gb_Oc .gb_0d.gb_ve button:hover svg,.gb_0d button:hover svg,.gb_d:hover{background-color:rgba(60,64,67,.08)}.gb_Da .gb_d.gb_Fa:hover{background-color:transparent}.gb_d[aria-expanded=true],.gb_d:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_d[aria-expanded=true] .gb_h{fill:#5f6368;opacity:1}.gb_Oc .gb_0d button:hover svg,.gb_Oc .gb_d:hover{background-color:rgba(232,234,237,.08)}.gb_Oc .gb_0d button:focus svg,.gb_Oc .gb_0d button:focus:hover svg,.gb_Oc .gb_d:focus,.gb_Oc .gb_d:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Oc .gb_0d button:active svg,.gb_Oc .gb_d:active{background-color:rgba(232,234,237,.12)}.gb_Oc .gb_d[aria-expanded=true],.gb_Oc .gb_d:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Oc .gb_d[aria-expanded=true] .gb_h{fill:#fff;opacity:1}.gb_w{padding:4px}.gb_Pa.gb_Td .gb_w{padding:4px 2px}.gb_Pa.gb_Td .gb_b.gb_w{padding-left:6px}.gb_5{z-index:991;line-height:normal}.gb_5.gb_1d{left:0;right:auto}@media (max-width:350px){.gb_5.gb_1d{left:0}}.gb_2d .gb_5{top:56px}.gb_k .gb_d,.gb_4 .gb_k .gb_d{background-position:-64px -29px}.gb_K .gb_k .gb_d{background-position:-29px -29px;opacity:1}.gb_k .gb_d,.gb_k .gb_d:hover,.gb_k .gb_d:focus{opacity:1}.gb_jd{display:none}@media screen and (max-width:319px){.gb_rd:not(.gb_wd) .gb_k{display:none;visibility:hidden}}.gb_o{display:none}.gb_dd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_dd.gb_ed{color:#3c4043}.gb_Pa.gb_Qa .gb_dd{margin-bottom:0}.gb_fd.gb_gd .gb_dd{padding-left:4px}.gb_Pa.gb_Qa .gb_hd{position:relative;top:-2px}.gb_Pa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Pa.gb_Wc{min-width:120px}.gb_Pa.gb_pd .gb_qd{display:none}.gb_Pa.gb_pd .gb_rd{height:56px}header.gb_Pa{display:block}.gb_Pa svg{fill:currentColor}.gb_sd{position:fixed;top:0;width:100%}.gb_td{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_ud{height:64px}.gb_rd{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Pa:not(.gb_Qa) .gb_rd{padding:8px}.gb_Pa.gb_vd .gb_rd{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Pa .gb_rd.gb_wd.gb_xd{min-width:0}.gb_Pa.gb_Qa .gb_rd{padding:4px;padding-left:8px;min-width:0}.gb_qd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_zd>.gb_qd{display:table-cell;width:100%}.gb_fd{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Pa.gb_Qa .gb_fd{padding-right:14px}.gb_Ad{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Ad>:only-child{display:inline-block}.gb_Bd.gb_6c{padding-left:4px}.gb_Bd.gb_Cd,.gb_Pa.gb_vd .gb_Bd,.gb_Pa.gb_Qa:not(.gb_ld) .gb_Bd{padding-left:0}.gb_Pa.gb_Qa .gb_Bd.gb_Cd{padding-right:0}.gb_Pa.gb_Qa .gb_Bd.gb_Cd .gb_Da{margin-left:10px}.gb_6c{display:inline}.gb_Pa.gb_0c .gb_Bd.gb_Dd,.gb_Pa.gb_ld .gb_Bd.gb_Dd{padding-left:2px}.gb_dd{display:inline-block}.gb_Bd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_ld{height:48px}.gb_Pa.gb_ld{min-width:auto}.gb_ld .gb_Bd{float:right;padding-left:32px}.gb_ld .gb_Bd.gb_Ed{padding-left:0}.gb_Fd{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_kd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Md{color:black}.gb_Oc{color:white}.gb_Pa a,.gb_Tc a{color:inherit}.gb_U{color:rgba(0,0,0,.87)}.gb_Pa svg,.gb_Tc svg,.gb_fd .gb_od,.gb_5c .gb_od{color:#5f6368;opacity:1}.gb_Oc svg,.gb_Tc.gb_Xc svg,.gb_Oc .gb_fd .gb_od,.gb_Oc .gb_fd .gb_Nc,.gb_Oc .gb_fd .gb_hd,.gb_Tc.gb_Xc .gb_od{color:rgba(255,255,255,.87)}.gb_Oc .gb_fd .gb_Mc:not(.gb_Nd){opacity:.87}.gb_ed{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Oc .gb_ed,.gb_Md .gb_ed{opacity:1}.gb_Hd{position:relative}.gb_Id{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_H,span.gb_H{color:rgba(0,0,0,.87);text-decoration:none}.gb_Oc a.gb_H,.gb_Oc span.gb_H{color:white}a.gb_H:focus{outline-offset:2px}a.gb_H:hover{text-decoration:underline}.gb_I{display:inline-block;padding-left:15px}.gb_I .gb_H{display:inline-block;line-height:24px;vertical-align:middle}.gb_Od{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Pa.gb_ld .gb_Od{margin-left:8px}#gb a.gb_Ba.gb_Od{cursor:pointer}.gb_Ba.gb_Od:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ba.gb_Od:focus,.gb_Ba.gb_Od:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ba.gb_Od:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Od{background:#1a73e8;border:1px solid transparent}.gb_Pa.gb_Qa .gb_Od{padding:9px 15px;min-width:80px}.gb_Jd{text-align:left}#gb .gb_Oc a.gb_Od:not(.gb_i),#gb.gb_Oc a.gb_Od:not(.gb_Pd){background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ba.gb_i.gb_Od{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Oc a.gb_Od:hover:not(.gb_i),#gb.gb_Oc a.gb_Od:not(.gb_Pd):hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ba.gb_i.gb_Od:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Oc a.gb_Od:focus:not(.gb_i),#gb .gb_Oc a.gb_Od:focus:hover:not(.gb_i),#gb.gb_Oc a.gb_Od:focus:not(.gb_i),#gb.gb_Oc a.gb_Od:focus:hover:not(.gb_i){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ba.gb_i.gb_Od:focus,#gb a.gb_Ba.gb_i.gb_Od:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Oc a.gb_Od:active:not(.gb_i),#gb.gb_Oc a.gb_Od:not(.gb_Pd):active{background:#ecf3fe}#gb a.gb_Ba.gb_i.gb_Od:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_l{display:none}@media screen and (max-width:319px){.gb_rd:not(.gb_wd) .gb_k{display:none;visibility:hidden}}.gb_Da{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Da.gb_i{background-color:transparent;border:1px solid #5f6368}.gb_Ka{display:inherit}.gb_Da.gb_i .gb_Ka{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Da:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Da.gb_i:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Da:focus-visible,.gb_Da:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Da.gb_i:focus-visible,.gb_Da.gb_i:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Da.gb_i:active,.gb_Da.gb_La.gb_i:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_Ma{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Da.gb_i .gb_Ma{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_Ma.gb_Na{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_Ma.gb_Na .gb_Oa{vertical-align:middle}.gb_Pa:not(.gb_Qa) .gb_Da{margin-left:10px;margin-right:4px}.gb_Ra{max-height:32px;width:78px}.gb_Da.gb_i .gb_Ra{max-height:26px;width:72px}.gb_n{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_2a{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_2a.gb_n{height:30px;width:30px}.gb_2a.gb_n:hover,.gb_2a.gb_n:active{-webkit-box-shadow:none;box-shadow:none}.gb_3a{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_4a{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_n::before,.gb_5a::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_M .gb_5a::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_n:hover,.gb_n:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_n:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_n:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_6a{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_d.gb_6a{width:auto}.gb_6a:hover,.gb_6a:focus{opacity:.85}.gb_7a .gb_6a,.gb_7a .gb_8a{line-height:26px}#gb#gb.gb_7a a.gb_6a,.gb_7a .gb_8a{font-size:11px;height:auto}.gb_9a{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Fa:hover .gb_9a{opacity:.85}.gb_Da>.gb_b{padding:3px 3px 3px 4px}.gb_ab.gb_1a{color:#fff}.gb_K .gb_6a,.gb_K .gb_9a{opacity:1}#gb#gb.gb_K.gb_K a.gb_6a,#gb#gb .gb_K.gb_K a.gb_6a{color:#fff}.gb_K.gb_K .gb_9a{border-top-color:#fff;opacity:1}.gb_4 .gb_n:hover,.gb_K .gb_n:hover,.gb_4 .gb_n:focus,.gb_K .gb_n:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_bb .gb_b,.gb_cb .gb_b{position:absolute;right:1px}.gb_b.gb_J,.gb_db.gb_J,.gb_Fa.gb_J{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_eb.gb_fb .gb_6a{width:30px!important}.gb_m{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_gb .gb_m,.gb_hb .gb_m{right:0;top:0}.gb_b .gb_d{padding:4px}.gb_q{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.u8Ti_iwBwEs.2019.O","co.in","en-GB","425",0,[4,2,"","","","606105313","0"],null,"jAPOZY-PG_mwp84PzdCnkA4",null,0,"og.qtm.zz20CdIDKVg.L.W.O","AA2YrTsL4HiE1bvJV-MS9_mgAxWPHzXqxw","AA2YrTvwL5uXLldqnwtu49O3C0adR0c4Jg","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","harshabadisepu@gmail.com","","ANc_yygjtTQ_pZUp1j5RzazSdvXIyLOUHZaALZ7BuLbnwCf0ELUTXA89ss70BBY8_FGJ9xy93ikX6srJiUecnzpE1VJxLOGcMA",0,0,0],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,1,0,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en-GB"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.GsbA68hXs80.O/d=1/rs=AHpOoo899t-H8Lxb3OqzMDuPn6TV_i36ag/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20231128.0_p1","en-GB",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0,null,null,["5061451","google\\.(com|ru|ca|by|kz|com\\.mx|com\\.tr)$",1]],[1,1,null,40400,425,"IND","en-GB","606105313.0",8,0.009999999776482582,1,0,null,null,null,null,"3701180,3701182",null,null,null,"jAPOZY-PG_mwp84PzdCnkA4",0,0,0,null,2,5,"nn",93,0,0,1,1,1,114591953,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.u8Ti_iwBwEs.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTsL4HiE1bvJV-MS9_mgAxWPHzXqxw"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.zz20CdIDKVg.L.W.O/m=qcwid/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTvwL5uXLldqnwtu49O3C0adR0c4Jg"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?amb=1\u0026sea=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert"],0,1,null,1,1,0,0]],null,null,"425","425",1,0,null,"en-GB",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026timeStmp=1708000140\u0026secTok=.AG5fkS_lMaoM0w58l0PK_lYxZl8hw7k0CA\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",0,0],0,0,0,null,0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,3701180,0]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){("undefined"!==typeof globalThis?globalThis:"undefined"!==typeof self?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ea,ka,na,oa,xa,ya,za,Ba,Ca,Da,Ga,Va,Ua,Xa,Za,Ya,$a,ab,hb,mb,nb,ob,pb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));void 0!==b&&(this.cause=b)};_.ba=function(){var a=_.q.navigator;return a&&(a=a.userAgent)?a:""};ea=function(a){return ca?da?da.brands.some(({brand:b})=>b&&-1!=b.indexOf(a)):!1:!1};_.u=function(a){return-1!=_.ba().indexOf(a)};
_.fa=function(){return ca?!!da&&0<da.brands.length:!1};_.ha=function(){return _.fa()?!1:_.u("Opera")};_.ia=function(){return _.fa()?!1:_.u("Trident")||_.u("MSIE")};_.ja=function(){return _.u("Firefox")||_.u("FxiOS")};_.la=function(){return _.u("Safari")&&!(ka()||(_.fa()?0:_.u("Coast"))||_.ha()||(_.fa()?0:_.u("Edge"))||(_.fa()?ea("Microsoft Edge"):_.u("Edg/"))||(_.fa()?ea("Opera"):_.u("OPR"))||_.ja()||_.u("Silk")||_.u("Android"))};
ka=function(){return _.fa()?ea("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(_.fa()?0:_.u("Edge"))||_.u("Silk")};_.ma=function(){return _.u("Android")&&!(ka()||_.ja()||_.ha()||_.u("Silk"))};na=function(){return ca?!!da&&!!da.platform:!1};oa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.pa=function(){return oa()||_.u("iPad")||_.u("iPod")};_.qa=function(){return na()?"macOS"===da.platform:_.u("Macintosh")};_.sa=function(a,b){return 0<=_.ra(a,b)};
_.ta=function(a){let b="",c=0;const d=a.length-10240;for(;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)};_.ua=function(a){return null!=a&&a instanceof Uint8Array};_.va=function(a){return Array.prototype.slice.call(a)};xa=function(a,b){_.wa(b,(a|0)&-14591)};ya=function(a,b){_.wa(b,(a|34)&-14557)};za=function(a){a=a>>14&1023;return 0===a?536870912:a};Ba=function(a){return!(!a||"object"!==typeof a||a.i!==Aa)};
Ca=function(a){return null!==a&&"object"===typeof a&&!Array.isArray(a)&&a.constructor===Object};Da=function(a,b,c){if(!Array.isArray(a)||a.length)return!1;const d=a[_.v]|0;if(d&1)return!0;if(!(b&&(Array.isArray(b)?b.includes(c):b.has(c))))return!1;_.wa(a,d|1);return!0};_.Ea=function(a){if(a&2)throw Error();};Ga=function(a,b){(b=_.Fa?b[_.Fa]:void 0)&&(a[_.Fa]=_.va(b))};
_.Ha=function(a){a=Error(a);a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity="warning";return a};_.Ka=function(a){if("boolean"!==typeof a)throw Error("r`"+_.Ia(a)+"`"+a);return a};_.La=function(a){if(!Number.isFinite(a))throw _.Ha("enum");return a|0};_.Ma=function(a){if("number"!==typeof a)throw _.Ha("int32");if(!Number.isFinite(a))throw _.Ha("int32");return a|0};
_.Na=function(a){if(null!=a&&"string"!==typeof a)throw Error();return a};_.Oa=function(a){return null==a||"string"===typeof a?a:void 0};_.Qa=function(a,b,c){if(null!=a&&"object"===typeof a&&a.Qd===_.Pa)return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;0===e&&(e|=c&32);e|=c&2;e!==d&&_.wa(a,e);return new b(a)}};_.Sa=function(a,b){Ra=b;a=new a(b);Ra=void 0;return a};
_.Ta=function(a,b,c){null==a&&(a=Ra);Ra=void 0;if(null==a){var d=96;c?(a=[c],d|=512):a=[];b&&(d=d&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error();d=a[_.v]|0;if(d&64)return a;d|=64;if(c&&(d|=512,c!==a[0]))throw Error();a:{c=a;const e=c.length;if(e){const f=e-1;if(Ca(c[f])){d|=256;b=f-(+!!(d&512)-1);if(1024<=b)throw Error();d=d&-16760833|(b&1023)<<14;break a}}if(b){b=Math.max(b,e-(+!!(d&512)-1));if(1024<b)throw Error();d=d&-16760833|(b&1023)<<14}}}_.wa(a,d);return a};Va=function(a,b){return Ua(b)};
Ua=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(Da(a,void 0,0))return}else{if(_.ua(a))return _.ta(a);if("function"==typeof _.Wa&&a instanceof _.Wa)return a.j()}}return a};Xa=function(a,b,c){const d=_.va(a);var e=d.length;const f=b&256?d[e-1]:void 0;e+=f?-1:0;for(b=b&512?1:0;b<e;b++)d[b]=c(d[b]);if(f){b=d[b]={};for(const g in f)b[g]=c(f[g])}Ga(d,a);return d};
Za=function(a,b,c,d,e){if(null!=a){if(Array.isArray(a))a=Da(a,void 0,0)?void 0:e&&(a[_.v]|0)&2?a:Ya(a,b,c,void 0!==d,e);else if(Ca(a)){const f={};for(let g in a)f[g]=Za(a[g],b,c,d,e);a=f}else a=b(a,d);return a}};Ya=function(a,b,c,d,e){const f=d||c?a[_.v]|0:0;d=d?!!(f&32):void 0;const g=_.va(a);for(let h=0;h<g.length;h++)g[h]=Za(g[h],b,c,d,e);c&&(Ga(g,a),c(f,g));return g};$a=function(a){return a.Qd===_.Pa?a.toJSON():Ua(a)};
ab=function(a,b,c=ya){if(null!=a){if(a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=a[_.v]|0;if(d&2)return a;b&&(b=0===d||!!(d&32)&&!(d&64||!(d&16)));return b?_.wa(a,(d|34)&-12293):Ya(a,ab,d&4?ya:c,!0,!0)}a.Qd===_.Pa&&(c=a.qa,d=c[_.v],a=d&2?a:_.Sa(a.constructor,_.bb(c,d,!0)));return a}};_.bb=function(a,b,c){const d=c||b&2?ya:xa,e=!!(b&32);a=Xa(a,b,f=>ab(f,e,d));a[_.v]=a[_.v]|32|(c?2:0);return a};
_.cb=function(a){const b=a.qa,c=b[_.v];return c&2?_.Sa(a.constructor,_.bb(b,c,!1)):a};_.db=function(a,b,c,d,e){const f=za(b);if(c>=f||e){let g=b;if(b&256)e=a[a.length-1];else{if(null==d)return g;e=a[f+(+!!(b&512)-1)]={};g|=256}e[c]=d;c<f&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&_.wa(a,g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b};_.fb=function(a,b,c,d){a=a.qa;let e=a[_.v];const f=_.eb(a,e,c,d);b=_.Qa(f,b,e);b!==f&&null!=b&&_.db(a,e,c,b,d);return b};
_.gb=function(a,b){return null!=a?a:b};
hb=function(a,b,c){const d=a.constructor.ta,e=(c?a.qa:b)[_.v];a=b.length;if(!a)return b;let f,g;if(Ca(c=b[a-1])){a:{var h=c;let p={},n=!1;for(var k in h){let t=h[k];if(Array.isArray(t)){let r=t;if(Da(t,d,+k)||Ba(t)&&0===t.size)t=null;t!=r&&(n=!0)}null!=t?p[k]=t:n=!0}if(n){for(var l in p){h=p;break a}h=null}}h!=c&&(f=!0);a--}for(k=+!!(e&512)-1;0<a;a--){l=a-1;c=b[l];l-=k;if(!(null==c||Da(c,d,l)||Ba(c)&&0===c.size))break;g=!0}if(!f&&!g)return b;b=Array.prototype.slice.call(b,0,a);h&&b.push(h);return b};
_.w=function(a,b){return null!=a?!!a:!!b};_.x=function(a,b){void 0==b&&(b="");return null!=a?a:b};_.ib=function(a,b){void 0==b&&(b=0);return null!=a?a:b};_.jb=function(a){for(const b in a)return!1;return!0};_.lb=function(a,b){let c,d;for(let e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(let f=0;f<kb.length;f++)c=kb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}};
mb="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};nb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};ob=nb(this);
pb=function(a,b){if(b)a:{var c=ob;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&mb(c,a,{configurable:!0,writable:!0,value:b})}};pb("globalThis",function(a){return a||ob});var rb,vb,wb;_.qb=_.qb||{};_.q=this||self;rb=_.q._F_toggles||[];_.sb=function(a,b){a=a.split(".");b=b||_.q;for(var c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b};_.Ia=function(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"};_.tb=function(a){var b=typeof a;return"object"==b&&null!=a||"function"==b};_.ub="closure_uid_"+(1E9*Math.random()>>>0);vb=function(a,b,c){return a.call.apply(a.bind,arguments)};
wb=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}};_.y=function(a,b,c){_.y=Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?vb:wb;return _.y.apply(null,arguments)};
_.z=function(a,b){a=a.split(".");var c=_.q;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.A=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.dj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.A(_.aa,Error);_.aa.prototype.name="CustomError";_.xb=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};var yb=!!(rb[0]&128);var zb;if(rb[0]&64)zb=yb;else{var Ab=_.sb("WIZ_global_data.oxN3nb"),Bb=Ab&&Ab[610401301];zb=null!=Bb?Bb:!1}var ca=zb;var da,Cb=_.q.navigator;da=Cb?Cb.userAgentData||null:null;_.ra=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.Db=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.Eb=function(a){_.Eb[" "](a);return a};_.Eb[" "]=function(){};var Rb,Sb,Xb;_.Fb=_.ha();_.B=_.ia();_.Gb=_.u("Edge");_.Hb=_.Gb||_.B;_.Ib=_.u("Gecko")&&!(-1!=_.ba().toLowerCase().indexOf("webkit")&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.Jb=-1!=_.ba().toLowerCase().indexOf("webkit")&&!_.u("Edge");_.Kb=_.qa();_.Lb=na()?"Windows"===da.platform:_.u("Windows");_.Mb=na()?"Android"===da.platform:_.u("Android");_.Nb=oa();_.Ob=_.u("iPad");_.Pb=_.u("iPod");_.Qb=_.pa();Rb=function(){var a=_.q.document;return a?a.documentMode:void 0};
a:{var Tb="",Ub=function(){var a=_.ba();if(_.Ib)return/rv:([^\);]+)(\)|;)/.exec(a);if(_.Gb)return/Edge\/([\d\.]+)/.exec(a);if(_.B)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(_.Jb)return/WebKit\/(\S+)/.exec(a);if(_.Fb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();Ub&&(Tb=Ub?Ub[1]:"");if(_.B){var Vb=Rb();if(null!=Vb&&Vb>parseFloat(Tb)){Sb=String(Vb);break a}}Sb=Tb}_.Wb=Sb;if(_.q.document&&_.B){var Yb=Rb();Xb=Yb?Yb:parseInt(_.Wb,10)||void 0}else Xb=void 0;_.Zb=Xb;_.ac=_.ja();_.bc=oa()||_.u("iPod");_.cc=_.u("iPad");_.dc=_.ma();_.ec=ka();_.fc=_.la()&&!_.pa();_.gc="undefined"!==typeof TextDecoder;_.hc="undefined"!==typeof TextEncoder;_.v=Symbol();_.wa=(a,b)=>{a[_.v]=b;return a};var Aa,ic,kc,lc,mc;_.Pa={};Aa={};kc=[];_.wa(kc,55);_.jc=Object.freeze(kc);lc=class{};mc=class{};Object.freeze(new lc);Object.freeze(new mc);var Ra;_.nc=function(a,b){a=a.qa;return _.eb(a,a[_.v],b)};_.eb=function(a,b,c,d){if(-1===c)return null;if(c>=za(b)){if(b&256)return a[a.length-1][c]}else{var e=a.length;if(d&&b&256&&(d=a[e-1][c],null!=d))return d;b=c+(+!!(b&512)-1);if(b<e)return a[b]}};_.oc=function(a,b,c){const d=a.qa;let e=d[_.v];_.Ea(e);_.db(d,e,b,c);return a};_.D=function(a,b){a=_.nc(a,b);return null==a||"boolean"===typeof a?a:"number"===typeof a?!!a:void 0};
_.E=function(a,b,c,d=!1){b=_.fb(a,b,c,d);if(null==b)return b;a=a.qa;let e=a[_.v];if(!(e&2)){const f=_.cb(b);f!==b&&(b=f,_.db(a,e,c,b,d))}return b};_.F=function(a,b,c){null==c&&(c=void 0);return _.oc(a,b,c)};_.G=function(a,b){return _.Oa(_.nc(a,b))};_.I=function(a,b){return _.gb(_.D(a,b),!1)};_.pc=function(a,b,c=0){a=a.qa;let d=a[_.v];const e=_.eb(a,d,b);var f=null==e||"number"===typeof e?e:"NaN"===e||"Infinity"===e||"-Infinity"===e?Number(e):void 0;null!=f&&f!==e&&_.db(a,d,b,f);return _.gb(f,c)};
_.J=function(a,b){return _.gb(_.G(a,b),"")};_.K=function(a,b,c){return _.oc(a,b,null==c?c:_.Ka(c))};_.L=function(a,b,c){return _.oc(a,b,null==c?c:_.Ma(c))};_.M=function(a,b,c){return _.oc(a,b,_.Na(c))};_.N=function(a,b,c){return _.oc(a,b,null==c?c:_.La(c))};_.Q=class{constructor(a,b,c){this.qa=_.Ta(a,b,c)}toJSON(){return ic?hb(this,this.qa,!1):hb(this,Ya(this.qa,$a,void 0,void 0,!1),!0)}Ia(){ic=!0;try{return JSON.stringify(this.toJSON(),Va)}finally{ic=!1}}Bc(){return!!((this.qa[_.v]|0)&2)}};_.Q.prototype.Qd=_.Pa;_.Q.prototype.toString=function(){return hb(this,this.qa,!1).toString()};_.qc=Symbol();_.rc=Symbol();_.sc=Symbol();_.uc=Symbol();_.vc=Symbol();var wc=class extends _.Q{constructor(){super()}};_.xc=class extends _.Q{constructor(){super()}B(a){return _.L(this,3,a)}};var yc=class extends _.Q{constructor(a){super(a)}};var zc=class extends _.Q{constructor(a){super(a)}Uc(a){return _.M(this,24,a)}};_.Ac=class extends _.Q{constructor(a){super(a)}};_.Bc=function(){this.Ga=this.Ga;this.oa=this.oa};_.Bc.prototype.Ga=!1;_.Bc.prototype.isDisposed=function(){return this.Ga};_.Bc.prototype.ka=function(){this.Ga||(this.Ga=!0,this.O())};_.Bc.prototype.O=function(){if(this.oa)for(;this.oa.length;)this.oa.shift()()};var Cc=class extends _.Bc{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){var b=this.o;a=a.split(".");for(var c=a.length,d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}Hb(){for(var a=this.i.length,b=this.i,c=[],d=0;d<a;++d){var e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].Hb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Ec=class extends _.Bc{constructor(){var a=_.Dc;super();this.o=a;this.A=this.i=null;this.v=0;this.C={};this.j=!1;a=window.navigator.userAgent;0<=a.indexOf("MSIE")&&0<=a.indexOf("Trident")&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&9>parseFloat(a[1])&&(this.j=!0)}B(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Fc=class extends _.Q{constructor(a){super(a)}};var Gc=class extends _.Q{constructor(a){super(a)}};var Ic;_.Hc=function(a,b,c=98){if(a.i){const d=new wc;_.M(d,1,b.message);_.M(d,2,b.stack);_.L(d,3,b.lineNumber);_.N(d,5,1);b=new _.xc;_.F(b,40,d);a.i.log(c,b)}};Ic=class{constructor(){this.i=null}log(a){_.Hc(this,a)}};var Jc,Mc,Lc;_.Kc=function(a){let b;b=window.google&&window.google.logUrl?"":"https://www.google.com";b+="/gen_204?use_corp=on&";b+=a.Ia(2040-b.length);Jc(b)};Jc=function(a){var b=new Image,c=Lc;b.onerror=b.onload=b.onabort=function(){c in Mc&&delete Mc[c]};Mc[Lc++]=b;b.src=a};Mc=[];Lc=0;_.Nc=class{constructor(){this.data={}}Ia(a){var b=[],c;for(c in this.data)b.push(encodeURIComponent(c)+"="+encodeURIComponent(String(this.data[c])));return("atyp=i&zx="+(new Date).getTime()+"&"+b.join("&")).substr(0,a)}};var Oc=class extends _.Nc{constructor(a){super();var b=_.E(a,yc,8)||new yc;window.google&&window.google.kEI&&(this.data.ei=window.google.kEI);this.data.sei=_.x(_.G(a,10));this.data.ogf=_.x(_.G(b,3));this.data.ogrp=(window.google&&window.google.sn?!/.*hp$/.test(window.google.sn):_.w(_.D(a,7)))?"1":"";this.data.ogv=_.x(_.G(b,6))+"."+_.x(_.G(b,7));this.data.ogd=_.x(_.G(a,21));this.data.ogc=_.x(_.G(a,20));this.data.ogl=_.x(_.G(a,5));this.data.oggv="quantum:gapiBuildLabel"}};var kb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");var Pc=[1,2,3,4,5,6,9,10,11,13,14,28,29,30,34,35,37,38,39,40,42,43,48,49,50,51,52,53,62,500],Rc=function(a){if(!Qc){Qc={};for(var b=0;b<Pc.length;b++)Qc[Pc[b]]=!0}return!!Qc[a]},Sc=function(a){a=String(a);return a.replace(".","%2E").replace(",","%2C")},Tc=class extends Oc{constructor(a,b,c,d,e){super(a);_.lb(this.data,{oge:c,ogex:_.x(_.G(a,9)),ogp:_.x(_.G(a,6)),ogsr:Math.round(1/(Rc(c)?_.ib(_.pc(b,3,1)):_.ib(_.pc(b,2,1E-4)))),ogus:d});if(e){"ogw"in e&&(this.data.ogw=e.ogw,delete e.ogw);"ved"in e&&
(this.data.ved=e.ved,delete e.ved);a=[];for(var f in e)0!=a.length&&a.push(","),a.push(Sc(f)),a.push("."),a.push(Sc(e[f]));e=a.join("");""!=e&&(this.data.ogad=e)}}},Qc=null;var Uc=class extends _.Q{constructor(a){super(a)}};var Yc=class{constructor(){var a=Vc,b=Wc,c=Xc;this.i=a;this.v=b;this.o=_.ib(_.pc(a,2,1E-4),1E-4);this.C=_.ib(_.pc(a,3,1),1);b=Math.random();this.j=_.w(_.D(a,1))&&b<this.o;this.A=_.w(_.D(a,1))&&b<this.C;a=0;_.w(_.D(c,1))&&(a|=1);_.w(_.D(c,2))&&(a|=2);_.w(_.D(c,3))&&(a|=4);this.B=a}log(a,b){try{if(Rc(a)?this.A:this.j){const c=new Tc(this.v,this.i,a,this.B,b);_.Kc(c)}}catch(c){}}};var $c;_.Zc=function(a){if(0<a.o.length){var b=void 0!==a.i,c=void 0!==a.j;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.Db(c,b,a)}catch(d){console.error(d)}}}};_.ad=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new $c(a,b,c));_.Zc(this)}resolve(a){if(void 0!==this.i||void 0!==this.j)throw Error("v");this.i=a;_.Zc(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};$c=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.bd=a=>{var b="zc";if(a.zc&&a.hasOwnProperty(b))return a.zc;b=new a;return a.zc=b};_.cd=class{constructor(){this.v=new _.ad;this.i=new _.ad;this.D=new _.ad;this.C=new _.ad;this.B=new _.ad;this.A=new _.ad;this.o=new _.ad;this.j=new _.ad;this.H=new _.ad}K(){return this.v}M(){return this.i}N(){return this.D}L(){return this.C}Ga(){return this.B}oa(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.bd(_.cd)}};var hd;_.ed=function(){return _.E(_.dd,zc,1)};_.fd=function(){return _.E(_.dd,_.Ac,5)};hd=class extends _.Q{constructor(){super(gd)}};var gd;window.gbar_&&window.gbar_.CONFIG?gd=window.gbar_.CONFIG[0]||{}:gd=[];_.dd=new hd;var Wc,Xc,Vc;_.E(_.dd,Gc,3)||new Gc;_.ed()||new zc;_.Dc=new Ic;Wc=_.ed()||new zc;Xc=_.fd()||new _.Ac;Vc=_.E(_.dd,Uc,4)||new Uc;new Yc;_.z("gbar_._DumpException",function(a){_.Dc?_.Dc.log(a):console.error(a)});_.id=new Ec;var kd;_.ld=function(a,b){var c=_.jd.i();if(a in c.i){if(c.i[a]!=b)throw new kd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.jb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.jd=class{constructor(){this.i={};this.j={}}static i(){return _.bd(_.jd)}};_.md=class extends _.aa{constructor(){super()}};kd=class extends _.md{};_.z("gbar.A",_.ad);_.ad.prototype.aa=_.ad.prototype.then;_.z("gbar.B",_.cd);_.cd.prototype.ba=_.cd.prototype.M;_.cd.prototype.bb=_.cd.prototype.N;_.cd.prototype.bd=_.cd.prototype.Ga;_.cd.prototype.bf=_.cd.prototype.K;_.cd.prototype.bg=_.cd.prototype.L;_.cd.prototype.bh=_.cd.prototype.oa;_.cd.prototype.bj=_.cd.prototype.J;_.cd.prototype.bk=_.cd.prototype.G;_.z("gbar.a",_.cd.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var nd=new Cc;_.ld("api",nd);var od=_.fd()||new _.Ac;
window.__PVT=_.x(_.G(od,8));_.ld("eq",_.id);
}catch(e){_._DumpException(e)}
try{
_.pd=class extends _.Q{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var qd=class extends _.Q{constructor(){super()}};var rd=class extends _.Bc{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b})}init(a,b,c){window.gapi={};var d=window.___jsl={};d.h=_.x(_.G(a,1));null!=_.D(a,12)&&(d.dpo=_.w(_.I(a,12)));d.ms=_.x(_.G(a,2));d.m=_.x(_.G(a,3));d.l=[];_.J(b,1)&&(a=_.G(b,3))&&this.i.push(a);_.J(c,1)&&(c=_.G(c,2))&&this.i.push(c);_.z("gapi.load",(0,_.y)(this.o,this));return this}};var sd=_.E(_.dd,_.Fc,14);if(sd){var td=_.E(_.dd,_.pd,9)||new _.pd,ud=new qd,vd=new rd;vd.init(sd,td,ud);_.ld("gs",vd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_harshabadisepu@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><script src="./titanic_survival_prediction_files/common_webcomponentsjs_webcomponents-lite.js.download" nonce=""></script><script src="./titanic_survival_prediction_files/common_webanimationsjs_web-animations-next-lite.min.js.download" nonce=""></script><script nonce="">var colabVersionTag = 'colab_20240213-060133_RC00_606561754'; var colabScsVersion = 'd90d0c23ac690132d9ebfa4fb7960f3c'; var hl = 'en-GB'; var colabExperiments = JSON.parse('\x7b\x22ai_unsubscribed_warning\x22: true, \x22aida_cell_button\x22: false, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22aida_in_editor\x22: false, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22bq_tid\x22: true, \x22cell_tags\x22: false, \x22chat\x22: true, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: false, \x22client_trim_completion_text\x22: 100, \x22cloud_origin\x22: \x22\x22, \x22commands_in_toolbar\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22compose_skip_suffix_check\x22: false, \x22converse_temp\x22: \x22\x22, \x22crawler\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22development\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22\x22, \x22embedded_connection_poll\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_more_reprs\x22: true, \x22explain_cell\x22: false, \x22explain_error\x22: true, \x22explain_error_prompt_next\x22: false, \x22explain_error_trim_traceback\x22: false, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs\x22, \x22filter_repetitive_suggestions\x22: true, \x22first_party_auth\x22: true, \x22generate_code\x22: true, \x22generate_code_prompt\x22: true, \x22generate_df\x22: true, \x22generate_fix\x22: true, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22import_data\x22: false, \x22internal_schedule\x22: false, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22log_hover_type\x22: false, \x22lsp_diagnostic_threshold_b312769838\x22: 0, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22lsp_rename\x22: false, \x22lsrp\x22: 0, \x22ml_banner\x22: false, \x22ml_enabled\x22: true, \x22mlpp\x22: false, \x22mlpp_multiline\x22: false, \x22mlpp_on_by_default\x22: true, \x22mlpp_trim_completion_text\x22: 100, \x22mobile\x22: false, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22og_dark\x22: true, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22output_menu\x22: false, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22quickchart_button\x22: true, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr\x22: false, \x22rp_lsp\x22: false, \x22rp_serve_kernel_port\x22: false, \x22rp_term\x22: false, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22session_resume_coalesce\x22: true, \x22sheets_paste\x22: true, \x22show_payments_interstitial\x22: false, \x22show_pip_warning_dialog\x22: false, \x22show_relnotes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22AmUpB2+Hlwk73pYiEMbnkef\/dprJi1I9rClec33apyFsbVOaCIRN29Rk9M4ht5Otgbp+thCc3MMD73GyCNfEWAkAAAB3eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OX0\x3d\x22, \x22suspicious_code_matches\x22: \x22\x22, \x22suspicious_code_regexs\x22: \x22\x22, \x22term4all\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_vm\x22: false, \x22unified_compose\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22use_corplogin\x22: true, \x22use_dm_sql_lsp\x22: false, \x22uxr_survey\x22: false, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22waffle\x22: false, \x22workstations\x22: false, \x22ids\x22: \x5b20730186, 20730150, 20730159, 20730177, 20730129, 20730183\x5d, \x22flag_ids\x22: \x7b\x22ai_unsubscribed_warning\x22: 45504730, \x22aida_cell_button\x22: 45425510, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_in_editor\x22: 45425507, \x22allowed_public_url_domains\x22: 45425558, \x22backend_version\x22: 45425541, \x22bq_tid\x22: 45425617, \x22cell_tags\x22: 45425779, \x22chat\x22: 45425490, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22compose_skip_suffix_check\x22: 45615470, \x22converse_temp\x22: 45425509, \x22crawler\x22: 45425491, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22development\x22: 45425544, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22embedded_connection_poll\x22: 45491618, \x22enable_adhoc_backends\x22: 45425506, \x22enable_more_reprs\x22: 45613354, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_prompt_next\x22: 45615229, \x22explain_error_trim_traceback\x22: 45618831, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22generate_code\x22: 45425492, \x22generate_code_prompt\x22: 45425488, \x22generate_df\x22: 45425503, \x22generate_fix\x22: 45425504, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22import_data\x22: 45430411, \x22internal_schedule\x22: 45425578, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22log_hover_type\x22: 45425602, \x22lsp_diagnostic_threshold_b312769838\x22: 45618432, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22lsp_rename\x22: 45618248, \x22lsrp\x22: 45425612, \x22ml_banner\x22: 45425631, \x22ml_enabled\x22: 45425493, \x22mlpp\x22: 45425608, \x22mlpp_multiline\x22: 45425623, \x22mlpp_on_by_default\x22: 45425609, \x22mlpp_trim_completion_text\x22: 45425622, \x22mobile\x22: 45425562, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22og_dark\x22: 45459627, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22output_menu\x22: 45617054, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22quickchart_button\x22: 45425501, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr\x22: 45491686, \x22rp_lsp\x22: 45462965, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_term\x22: 45426219, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt\x22: 45425624, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22session_resume_coalesce\x22: 45425603, \x22sheets_paste\x22: 45428502, \x22show_payments_interstitial\x22: 45425543, \x22show_pip_warning_dialog\x22: 45616404, \x22show_relnotes_on_open\x22: 45428128, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22suspicious_code_matches\x22: 45425615, \x22suspicious_code_regexs\x22: 45425616, \x22term4all\x22: 45425542, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_vm\x22: 45614812, \x22unified_compose\x22: 45425627, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22use_corplogin\x22: 45425606, \x22use_dm_sql_lsp\x22: 45425610, \x22uxr_survey\x22: 45425618, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22waffle\x22: 45446491, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'harshabadisepu@gmail.com'; var colabRenderDataToken = 'AFWLbD1YCDVC_UmrJjvEIGMqB2MtI5s5LPrD97Onj7GUYDTGpuMnD5jpsOW2PegsSY47pAJd2Acebqzpb0yfSgxccz8d2QqhmBJX46_T'; var colabConfig = '\x5b\x5b\x22harshabadisepu@gmail.com\x22,\x5b1,\x22AHXL0D2TT1dgB1WlvIx4bszeh+DTw\/+A0DHgKmJXJvQCjT4B1JCS5bvJn3NfSsIsgd3yADIKVThf53uSzDGvBHwhVXaJzhyxuO6bz6oyGyWwsb9pQ1rVKHJ8+EPdyGkcyy6pQ7fdbZtWZn00BzVrKnnurroM0YgaKFjy+d4vQQPmcuR8CXGhCfkg9Q1a52kgoNBWtCV27yyXo+w4OiFthVQvLWn9n6EIDzP1VHcN8sZqdSPftyKI6qiEi51MyJhGmS6fnfxa8u6Qmz7wM5YRxstb3hGMM3CuByq\/tLkQ+XNuIu2lnbGEH4lGxynNXrKvNJyOaebkR\/Ip1Ig8trfgQRfrqIj5SPDXNke+dWPweY4koXDorvVFdo4zJYqcyU74rkxqIdMvUiu\/FGk81ouD+j15HV1X\/I1tU6hV8ryHaoaUn6Tn+IETRkxbjc8yHpd\/DUIqokfpG1EfVmjIazZV1ayIhDhHv2QQmYjE9tbs9hedepiWkGkkXcwRjZ2CykyWTNYsHk06lIl7n4OmRVzYFjYSablRWwg0p5F3X39+3zIr2q32ROPhJCIJ9kh9CxQ7zJJ\/EqjyQ5iRTvJduzhj40v44MKcKHWFQ2lafRihhofXO\/RrE2TCRSfA2IgHkj+RD3qHULfg+1vir84WHUcIfb+CFthrq+hQttfViEYS7n\/47+PiBQeAGziS+YsHjD3Xsl7fR7Xg0rnTzBdasoGO7ltu8iMpVFFeNTweH83o8WpcRhrOxjfITnBpuUEMWmXw\/JSxfh8NWqi5AMWEvFi7c3Ek5p2uzeythhYlJQpspCVMCGgzMTC5BnDMJgK7nBAHuADFdq3uP7n+c3yULTAS45HnvdFRWNWonOSDDKFY4FaviRq58n0MdfKWl2c1RcHhEzGW\/kzJKNuQd4Y\/0o0mA5JKx5DptWE4+9nlyeGrxCt8nxw+VAiSTxQNe\/wGCP2Xx6wdL3lhS3BNt7fcm2CfE+zqTxqm7S48lg4vqsWmQsfg7gc0A6wNirqBMq4fe+0VEeaLoaatMbP0mlGj9HugTDzLl6eqzphWwuLRrTcZvaz0EiQULxU\/23N6r7g7vqRR0jg4oPhzq+d1LjhLFdFKYWn7+Gz3U1jAXc3P86x8Hyozdhz4D5XCPbRjUbBKs\/oJLsLtOkuCHmrB\/P0m0OWasjHMUrtpx06HLQ\/cLkKJMhLYyDS9sWR7zLBhEWbM8AWycQf4TC0iBTudEOM+zS\/oko5svYNzoTGywrSn4AKRsSBCHDe9zENrHpIu2lKqIlFWrCYaERX641cusvSWvTvMrqtFIJJqV6H\/tULkmzoh0fisuqh3i\/XGCg7ygcx9MVwMYyzgPw4iCUl6BlWnEIM1CEngLq3XzfKyx4N2Pv6KVREJiySAGVTdok01q6v+n0onRyZRk0Uggc0DIaHlj1FQ3M8abjweClfiPQ1i5kEIILz4QxoVXSJO0vTzqVV8E5B3fBKQByQ7HBCqvLii1VbZMdqHz0ZFqzLJ7rkq0DjrWu57052QNn2lD5gNFkACK3Pg7hEEk9KdeIKMwmgV7CKi2C5\/WYq1Mw2oK9MBbjaiu26G7Z6LntBe0apFXAXY8RHTHu1dmEulXjmgcMwbP3CjnAWKJQ5+OjSEJ\/vT0zRaq6d+SV0nguxR1so4sbFVGIuwSCzJb+6NdGGEvx78k2dqVzMq+Ug19YkHj+atx+Zh0RmEcHiS2ppGvYIpD9MCFHNiijd6Cqrz+WFZeh+hG50Qww6AGgrXZamAR6ra634RMc0Wu\/4UZG2mz\/+mHZeuaFUUgSfC8V\/xs4eiymkqXh8cMA30qADBJjtdtErJ\/J09r0Xb3oTpeilB1yvpaMswlitGsq+4DiYd5JDcu17SsHmY2rP7tJliSkK4XdObmfFAoz\/vyfoEgqtGIV8\x3d\x22,\x22AJ9oCCy1\/AKWJGpg2eQrrEnSdpXSnNr8yswVSrhW7+o2bEHjaSFCZ2ZuvpmPQOb9IZpM+onMWfpbMkZZBJhZRzRuQalC6J3zO4D\/HXTZIaPCwfNL4AvwOrtGthbeazaHUcXR3xwM1X8l\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22\x5d,\x5b1,4\x5d,\x22IN\x22\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/d90d0c23ac690132d9ebfa4fb7960f3c/img/favicon.ico"><link rel="stylesheet" href="./titanic_survival_prediction_files/bundle.css"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="-wL8iYJTC7X0zF9qBNDQUAd-P1ZkQUK-OhSgv4Wkf1M"><meta name="google-site-verification" content="o-EECwEDQeUpZv0jTmoGfCDX7dUI8Kul4ESepXmDnO0"><meta name="google-site-verification" content="KD0T7LOCCaCHCECvO9oHcfvqtPmvpMnFU6vogWZ6FnQ"><meta name="google-site-verification" content="X_e11vbgvEHdHuaRpMld_RK9XHaPSwlBXKAWbIbJxxs"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Osw7QcOK045GmOYJI2MM2_7AaL-s4q6pdn8gIv6JNxA"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colaboratory"><meta http-equiv="origin-trial" content="AmUpB2+Hlwk73pYiEMbnkef/dprJi1I9rClec33apyFsbVOaCIRN29Rk9M4ht5Otgbp+thCc3MMD73GyCNfEWAkAAAB3eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OX0="><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./titanic_survival_prediction_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style>
<custom-style>
  <style is="custom-style">[hidden] {
  display: none !important;
}

</style>
</custom-style>
<custom-style>
  <style is="custom-style">html {
  --layout_-_display:  flex;;

      --layout-inline_-_display:  inline-flex;;

      --layout-horizontal_-_display:  var(--layout_-_display); --layout-horizontal_-_-ms-flex-direction:  row; --layout-horizontal_-_-webkit-flex-direction:  row; --layout-horizontal_-_flex-direction:  row;;

      --layout-horizontal-reverse_-_display:  var(--layout_-_display); --layout-horizontal-reverse_-_-ms-flex-direction:  row-reverse; --layout-horizontal-reverse_-_-webkit-flex-direction:  row-reverse; --layout-horizontal-reverse_-_flex-direction:  row-reverse;;

      --layout-vertical_-_display:  var(--layout_-_display); --layout-vertical_-_-ms-flex-direction:  column; --layout-vertical_-_-webkit-flex-direction:  column; --layout-vertical_-_flex-direction:  column;;

      --layout-vertical-reverse_-_display:  var(--layout_-_display); --layout-vertical-reverse_-_-ms-flex-direction:  column-reverse; --layout-vertical-reverse_-_-webkit-flex-direction:  column-reverse; --layout-vertical-reverse_-_flex-direction:  column-reverse;;

      --layout-wrap_-_-ms-flex-wrap:  wrap; --layout-wrap_-_-webkit-flex-wrap:  wrap; --layout-wrap_-_flex-wrap:  wrap;;

      --layout-wrap-reverse_-_-ms-flex-wrap:  wrap-reverse; --layout-wrap-reverse_-_-webkit-flex-wrap:  wrap-reverse; --layout-wrap-reverse_-_flex-wrap:  wrap-reverse;;

      --layout-flex-auto_-_-ms-flex:  1 1 auto; --layout-flex-auto_-_-webkit-flex:  1 1 auto; --layout-flex-auto_-_flex:  1 1 auto;;

      --layout-flex-none_-_-ms-flex:  none; --layout-flex-none_-_-webkit-flex:  none; --layout-flex-none_-_flex:  none;;

      --layout-flex_-_-ms-flex:  1 1 0.000000001px; --layout-flex_-_-webkit-flex:  1; --layout-flex_-_flex:  1; --layout-flex_-_-webkit-flex-basis:  0.000000001px; --layout-flex_-_flex-basis:  0.000000001px;;

      --layout-flex-2_-_-ms-flex:  2; --layout-flex-2_-_-webkit-flex:  2; --layout-flex-2_-_flex:  2;;

      --layout-flex-3_-_-ms-flex:  3; --layout-flex-3_-_-webkit-flex:  3; --layout-flex-3_-_flex:  3;;

      --layout-flex-4_-_-ms-flex:  4; --layout-flex-4_-_-webkit-flex:  4; --layout-flex-4_-_flex:  4;;

      --layout-flex-5_-_-ms-flex:  5; --layout-flex-5_-_-webkit-flex:  5; --layout-flex-5_-_flex:  5;;

      --layout-flex-6_-_-ms-flex:  6; --layout-flex-6_-_-webkit-flex:  6; --layout-flex-6_-_flex:  6;;

      --layout-flex-7_-_-ms-flex:  7; --layout-flex-7_-_-webkit-flex:  7; --layout-flex-7_-_flex:  7;;

      --layout-flex-8_-_-ms-flex:  8; --layout-flex-8_-_-webkit-flex:  8; --layout-flex-8_-_flex:  8;;

      --layout-flex-9_-_-ms-flex:  9; --layout-flex-9_-_-webkit-flex:  9; --layout-flex-9_-_flex:  9;;

      --layout-flex-10_-_-ms-flex:  10; --layout-flex-10_-_-webkit-flex:  10; --layout-flex-10_-_flex:  10;;

      --layout-flex-11_-_-ms-flex:  11; --layout-flex-11_-_-webkit-flex:  11; --layout-flex-11_-_flex:  11;;

      --layout-flex-12_-_-ms-flex:  12; --layout-flex-12_-_-webkit-flex:  12; --layout-flex-12_-_flex:  12;;

      

      --layout-start_-_-ms-flex-align:  start; --layout-start_-_-webkit-align-items:  flex-start; --layout-start_-_align-items:  flex-start;;

      --layout-center_-_-ms-flex-align:  center; --layout-center_-_-webkit-align-items:  center; --layout-center_-_align-items:  center;;

      --layout-end_-_-ms-flex-align:  end; --layout-end_-_-webkit-align-items:  flex-end; --layout-end_-_align-items:  flex-end;;

      --layout-baseline_-_-ms-flex-align:  baseline; --layout-baseline_-_-webkit-align-items:  baseline; --layout-baseline_-_align-items:  baseline;;

      

      --layout-start-justified_-_-ms-flex-pack:  start; --layout-start-justified_-_-webkit-justify-content:  flex-start; --layout-start-justified_-_justify-content:  flex-start;;

      --layout-center-justified_-_-ms-flex-pack:  center; --layout-center-justified_-_-webkit-justify-content:  center; --layout-center-justified_-_justify-content:  center;;

      --layout-end-justified_-_-ms-flex-pack:  end; --layout-end-justified_-_-webkit-justify-content:  flex-end; --layout-end-justified_-_justify-content:  flex-end;;

      --layout-around-justified_-_-ms-flex-pack:  distribute; --layout-around-justified_-_-webkit-justify-content:  space-around; --layout-around-justified_-_justify-content:  space-around;;

      --layout-justified_-_-ms-flex-pack:  justify; --layout-justified_-_-webkit-justify-content:  space-between; --layout-justified_-_justify-content:  space-between;;

      --layout-center-center_-_-ms-flex-align:  var(--layout-center_-_-ms-flex-align); --layout-center-center_-_-webkit-align-items:  var(--layout-center_-_-webkit-align-items); --layout-center-center_-_align-items:  var(--layout-center_-_align-items); --layout-center-center_-_-ms-flex-pack:  var(--layout-center-justified_-_-ms-flex-pack); --layout-center-center_-_-webkit-justify-content:  var(--layout-center-justified_-_-webkit-justify-content); --layout-center-center_-_justify-content:  var(--layout-center-justified_-_justify-content);;

      

      --layout-self-start_-_-ms-align-self:  flex-start; --layout-self-start_-_-webkit-align-self:  flex-start; --layout-self-start_-_align-self:  flex-start;;

      --layout-self-center_-_-ms-align-self:  center; --layout-self-center_-_-webkit-align-self:  center; --layout-self-center_-_align-self:  center;;

      --layout-self-end_-_-ms-align-self:  flex-end; --layout-self-end_-_-webkit-align-self:  flex-end; --layout-self-end_-_align-self:  flex-end;;

      --layout-self-stretch_-_-ms-align-self:  stretch; --layout-self-stretch_-_-webkit-align-self:  stretch; --layout-self-stretch_-_align-self:  stretch;;

      --layout-self-baseline_-_-ms-align-self:  baseline; --layout-self-baseline_-_-webkit-align-self:  baseline; --layout-self-baseline_-_align-self:  baseline;;

      

      --layout-start-aligned_-_-ms-flex-line-pack:  start; --layout-start-aligned_-_-ms-align-content:  flex-start; --layout-start-aligned_-_-webkit-align-content:  flex-start; --layout-start-aligned_-_align-content:  flex-start;;

      --layout-end-aligned_-_-ms-flex-line-pack:  end; --layout-end-aligned_-_-ms-align-content:  flex-end; --layout-end-aligned_-_-webkit-align-content:  flex-end; --layout-end-aligned_-_align-content:  flex-end;;

      --layout-center-aligned_-_-ms-flex-line-pack:  center; --layout-center-aligned_-_-ms-align-content:  center; --layout-center-aligned_-_-webkit-align-content:  center; --layout-center-aligned_-_align-content:  center;;

      --layout-between-aligned_-_-ms-flex-line-pack:  justify; --layout-between-aligned_-_-ms-align-content:  space-between; --layout-between-aligned_-_-webkit-align-content:  space-between; --layout-between-aligned_-_align-content:  space-between;;

      --layout-around-aligned_-_-ms-flex-line-pack:  distribute; --layout-around-aligned_-_-ms-align-content:  space-around; --layout-around-aligned_-_-webkit-align-content:  space-around; --layout-around-aligned_-_align-content:  space-around;;

      

      --layout-block_-_display:  block;;

      --layout-invisible_-_visibility:  hidden !important;;

      --layout-relative_-_position:  relative;;

      --layout-fit_-_position:  absolute; --layout-fit_-_top:  0; --layout-fit_-_right:  0; --layout-fit_-_bottom:  0; --layout-fit_-_left:  0;;

      --layout-scroll_-_-webkit-overflow-scrolling:  touch; --layout-scroll_-_overflow:  auto;;

      --layout-fullbleed_-_margin:  0; --layout-fullbleed_-_height:  100vh;;

      

      --layout-fixed-top_-_position:  fixed; --layout-fixed-top_-_top:  0; --layout-fixed-top_-_left:  0; --layout-fixed-top_-_right:  0;;

      --layout-fixed-right_-_position:  fixed; --layout-fixed-right_-_top:  0; --layout-fixed-right_-_right:  0; --layout-fixed-right_-_bottom:  0;;

      --layout-fixed-bottom_-_position:  fixed; --layout-fixed-bottom_-_right:  0; --layout-fixed-bottom_-_bottom:  0; --layout-fixed-bottom_-_left:  0;;

      --layout-fixed-left_-_position:  fixed; --layout-fixed-left_-_top:  0; --layout-fixed-left_-_bottom:  0; --layout-fixed-left_-_left:  0;;
}

</style>
</custom-style><style>[hidden] { display: none !important; }</style><link rel="stylesheet" href="./titanic_survival_prediction_files/css(1)"><link rel="stylesheet" href="./titanic_survival_prediction_files/css(2)"><custom-style>
  <style is="custom-style">html {
  --paper-font-common-base_-_font-family:  'Roboto', 'Noto', sans-serif; --paper-font-common-base_-_-webkit-font-smoothing:  antialiased;;

      --paper-font-common-code_-_font-family:  'Roboto Mono', 'Consolas', 'Menlo', monospace; --paper-font-common-code_-_-webkit-font-smoothing:  antialiased;;

      --paper-font-common-expensive-kerning_-_text-rendering:  optimizeLegibility;;

      --paper-font-common-nowrap_-_white-space:  nowrap; --paper-font-common-nowrap_-_overflow:  hidden; --paper-font-common-nowrap_-_text-overflow:  ellipsis;;

      

      --paper-font-display4_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-display4_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-display4_-_white-space:  var(--paper-font-common-nowrap_-_white-space); --paper-font-display4_-_overflow:  var(--paper-font-common-nowrap_-_overflow); --paper-font-display4_-_text-overflow:  var(--paper-font-common-nowrap_-_text-overflow); --paper-font-display4_-_font-size:  112px; --paper-font-display4_-_font-weight:  300; --paper-font-display4_-_letter-spacing:  -.044em; --paper-font-display4_-_line-height:  120px;;

      --paper-font-display3_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-display3_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-display3_-_white-space:  var(--paper-font-common-nowrap_-_white-space); --paper-font-display3_-_overflow:  var(--paper-font-common-nowrap_-_overflow); --paper-font-display3_-_text-overflow:  var(--paper-font-common-nowrap_-_text-overflow); --paper-font-display3_-_font-size:  56px; --paper-font-display3_-_font-weight:  400; --paper-font-display3_-_letter-spacing:  -.026em; --paper-font-display3_-_line-height:  60px;;

      --paper-font-display2_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-display2_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-display2_-_font-size:  45px; --paper-font-display2_-_font-weight:  400; --paper-font-display2_-_letter-spacing:  -.018em; --paper-font-display2_-_line-height:  48px;;

      --paper-font-display1_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-display1_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-display1_-_font-size:  34px; --paper-font-display1_-_font-weight:  400; --paper-font-display1_-_letter-spacing:  -.01em; --paper-font-display1_-_line-height:  40px;;

      --paper-font-headline_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-headline_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-headline_-_font-size:  24px; --paper-font-headline_-_font-weight:  400; --paper-font-headline_-_letter-spacing:  -.012em; --paper-font-headline_-_line-height:  32px;;

      --paper-font-title_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-title_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-title_-_white-space:  var(--paper-font-common-nowrap_-_white-space); --paper-font-title_-_overflow:  var(--paper-font-common-nowrap_-_overflow); --paper-font-title_-_text-overflow:  var(--paper-font-common-nowrap_-_text-overflow); --paper-font-title_-_font-size:  20px; --paper-font-title_-_font-weight:  500; --paper-font-title_-_line-height:  28px;;

      --paper-font-subhead_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-subhead_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-subhead_-_font-size:  16px; --paper-font-subhead_-_font-weight:  400; --paper-font-subhead_-_line-height:  24px;;

      --paper-font-body2_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-body2_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-body2_-_font-size:  14px; --paper-font-body2_-_font-weight:  500; --paper-font-body2_-_line-height:  24px;;

      --paper-font-body1_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-body1_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-body1_-_font-size:  14px; --paper-font-body1_-_font-weight:  400; --paper-font-body1_-_line-height:  20px;;

      --paper-font-caption_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-caption_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-caption_-_white-space:  var(--paper-font-common-nowrap_-_white-space); --paper-font-caption_-_overflow:  var(--paper-font-common-nowrap_-_overflow); --paper-font-caption_-_text-overflow:  var(--paper-font-common-nowrap_-_text-overflow); --paper-font-caption_-_font-size:  12px; --paper-font-caption_-_font-weight:  400; --paper-font-caption_-_letter-spacing:  0.011em; --paper-font-caption_-_line-height:  20px;;

      --paper-font-menu_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-menu_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-menu_-_white-space:  var(--paper-font-common-nowrap_-_white-space); --paper-font-menu_-_overflow:  var(--paper-font-common-nowrap_-_overflow); --paper-font-menu_-_text-overflow:  var(--paper-font-common-nowrap_-_text-overflow); --paper-font-menu_-_font-size:  13px; --paper-font-menu_-_font-weight:  500; --paper-font-menu_-_line-height:  24px;;

      --paper-font-button_-_font-family:  var(--paper-font-common-base_-_font-family); --paper-font-button_-_-webkit-font-smoothing:  var(--paper-font-common-base_-_-webkit-font-smoothing); --paper-font-button_-_white-space:  var(--paper-font-common-nowrap_-_white-space); --paper-font-button_-_overflow:  var(--paper-font-common-nowrap_-_overflow); --paper-font-button_-_text-overflow:  var(--paper-font-common-nowrap_-_text-overflow); --paper-font-button_-_font-size:  14px; --paper-font-button_-_font-weight:  500; --paper-font-button_-_letter-spacing:  0.018em; --paper-font-button_-_line-height:  24px; --paper-font-button_-_text-transform:  uppercase;;

      --paper-font-code2_-_font-family:  var(--paper-font-common-code_-_font-family); --paper-font-code2_-_-webkit-font-smoothing:  var(--paper-font-common-code_-_-webkit-font-smoothing); --paper-font-code2_-_font-size:  14px; --paper-font-code2_-_font-weight:  700; --paper-font-code2_-_line-height:  20px;;

      --paper-font-code1_-_font-family:  var(--paper-font-common-code_-_font-family); --paper-font-code1_-_-webkit-font-smoothing:  var(--paper-font-common-code_-_-webkit-font-smoothing); --paper-font-code1_-_font-size:  14px; --paper-font-code1_-_font-weight:  500; --paper-font-code1_-_line-height:  20px;;
}

</style>
</custom-style><custom-style>
  <style is="custom-style">html {
  --google-red-100: #f4c7c3;
      --google-red-300: #e67c73;
      --google-red-500: #db4437;
      --google-red-700: #c53929;

      --google-blue-100: #c6dafc;
      --google-blue-300: #7baaf7;
      --google-blue-500: #4285f4;
      --google-blue-700: #3367d6;

      --google-green-100: #b7e1cd;
      --google-green-300: #57bb8a;
      --google-green-500: #0f9d58;
      --google-green-700: #0b8043;

      --google-yellow-100: #fce8b2;
      --google-yellow-300: #f7cb4d;
      --google-yellow-500: #f4b400;
      --google-yellow-700: #f09300;

      --google-grey-100: #f5f5f5;
      --google-grey-300: #e0e0e0;
      --google-grey-500: #9e9e9e;
      --google-grey-700: #616161;

      

      --paper-red-50: #ffebee;
      --paper-red-100: #ffcdd2;
      --paper-red-200: #ef9a9a;
      --paper-red-300: #e57373;
      --paper-red-400: #ef5350;
      --paper-red-500: #f44336;
      --paper-red-600: #e53935;
      --paper-red-700: #d32f2f;
      --paper-red-800: #c62828;
      --paper-red-900: #b71c1c;
      --paper-red-a100: #ff8a80;
      --paper-red-a200: #ff5252;
      --paper-red-a400: #ff1744;
      --paper-red-a700: #d50000;

      --paper-pink-50: #fce4ec;
      --paper-pink-100: #f8bbd0;
      --paper-pink-200: #f48fb1;
      --paper-pink-300: #f06292;
      --paper-pink-400: #ec407a;
      --paper-pink-500: #e91e63;
      --paper-pink-600: #d81b60;
      --paper-pink-700: #c2185b;
      --paper-pink-800: #ad1457;
      --paper-pink-900: #880e4f;
      --paper-pink-a100: #ff80ab;
      --paper-pink-a200: #ff4081;
      --paper-pink-a400: #f50057;
      --paper-pink-a700: #c51162;

      --paper-purple-50: #f3e5f5;
      --paper-purple-100: #e1bee7;
      --paper-purple-200: #ce93d8;
      --paper-purple-300: #ba68c8;
      --paper-purple-400: #ab47bc;
      --paper-purple-500: #9c27b0;
      --paper-purple-600: #8e24aa;
      --paper-purple-700: #7b1fa2;
      --paper-purple-800: #6a1b9a;
      --paper-purple-900: #4a148c;
      --paper-purple-a100: #ea80fc;
      --paper-purple-a200: #e040fb;
      --paper-purple-a400: #d500f9;
      --paper-purple-a700: #aa00ff;

      --paper-deep-purple-50: #ede7f6;
      --paper-deep-purple-100: #d1c4e9;
      --paper-deep-purple-200: #b39ddb;
      --paper-deep-purple-300: #9575cd;
      --paper-deep-purple-400: #7e57c2;
      --paper-deep-purple-500: #673ab7;
      --paper-deep-purple-600: #5e35b1;
      --paper-deep-purple-700: #512da8;
      --paper-deep-purple-800: #4527a0;
      --paper-deep-purple-900: #311b92;
      --paper-deep-purple-a100: #b388ff;
      --paper-deep-purple-a200: #7c4dff;
      --paper-deep-purple-a400: #651fff;
      --paper-deep-purple-a700: #6200ea;

      --paper-indigo-50: #e8eaf6;
      --paper-indigo-100: #c5cae9;
      --paper-indigo-200: #9fa8da;
      --paper-indigo-300: #7986cb;
      --paper-indigo-400: #5c6bc0;
      --paper-indigo-500: #3f51b5;
      --paper-indigo-600: #3949ab;
      --paper-indigo-700: #303f9f;
      --paper-indigo-800: #283593;
      --paper-indigo-900: #1a237e;
      --paper-indigo-a100: #8c9eff;
      --paper-indigo-a200: #536dfe;
      --paper-indigo-a400: #3d5afe;
      --paper-indigo-a700: #304ffe;

      --paper-blue-50: #e3f2fd;
      --paper-blue-100: #bbdefb;
      --paper-blue-200: #90caf9;
      --paper-blue-300: #64b5f6;
      --paper-blue-400: #42a5f5;
      --paper-blue-500: #2196f3;
      --paper-blue-600: #1e88e5;
      --paper-blue-700: #1976d2;
      --paper-blue-800: #1565c0;
      --paper-blue-900: #0d47a1;
      --paper-blue-a100: #82b1ff;
      --paper-blue-a200: #448aff;
      --paper-blue-a400: #2979ff;
      --paper-blue-a700: #2962ff;

      --paper-light-blue-50: #e1f5fe;
      --paper-light-blue-100: #b3e5fc;
      --paper-light-blue-200: #81d4fa;
      --paper-light-blue-300: #4fc3f7;
      --paper-light-blue-400: #29b6f6;
      --paper-light-blue-500: #03a9f4;
      --paper-light-blue-600: #039be5;
      --paper-light-blue-700: #0288d1;
      --paper-light-blue-800: #0277bd;
      --paper-light-blue-900: #01579b;
      --paper-light-blue-a100: #80d8ff;
      --paper-light-blue-a200: #40c4ff;
      --paper-light-blue-a400: #00b0ff;
      --paper-light-blue-a700: #0091ea;

      --paper-cyan-50: #e0f7fa;
      --paper-cyan-100: #b2ebf2;
      --paper-cyan-200: #80deea;
      --paper-cyan-300: #4dd0e1;
      --paper-cyan-400: #26c6da;
      --paper-cyan-500: #00bcd4;
      --paper-cyan-600: #00acc1;
      --paper-cyan-700: #0097a7;
      --paper-cyan-800: #00838f;
      --paper-cyan-900: #006064;
      --paper-cyan-a100: #84ffff;
      --paper-cyan-a200: #18ffff;
      --paper-cyan-a400: #00e5ff;
      --paper-cyan-a700: #00b8d4;

      --paper-teal-50: #e0f2f1;
      --paper-teal-100: #b2dfdb;
      --paper-teal-200: #80cbc4;
      --paper-teal-300: #4db6ac;
      --paper-teal-400: #26a69a;
      --paper-teal-500: #009688;
      --paper-teal-600: #00897b;
      --paper-teal-700: #00796b;
      --paper-teal-800: #00695c;
      --paper-teal-900: #004d40;
      --paper-teal-a100: #a7ffeb;
      --paper-teal-a200: #64ffda;
      --paper-teal-a400: #1de9b6;
      --paper-teal-a700: #00bfa5;

      --paper-green-50: #e8f5e9;
      --paper-green-100: #c8e6c9;
      --paper-green-200: #a5d6a7;
      --paper-green-300: #81c784;
      --paper-green-400: #66bb6a;
      --paper-green-500: #4caf50;
      --paper-green-600: #43a047;
      --paper-green-700: #388e3c;
      --paper-green-800: #2e7d32;
      --paper-green-900: #1b5e20;
      --paper-green-a100: #b9f6ca;
      --paper-green-a200: #69f0ae;
      --paper-green-a400: #00e676;
      --paper-green-a700: #00c853;

      --paper-light-green-50: #f1f8e9;
      --paper-light-green-100: #dcedc8;
      --paper-light-green-200: #c5e1a5;
      --paper-light-green-300: #aed581;
      --paper-light-green-400: #9ccc65;
      --paper-light-green-500: #8bc34a;
      --paper-light-green-600: #7cb342;
      --paper-light-green-700: #689f38;
      --paper-light-green-800: #558b2f;
      --paper-light-green-900: #33691e;
      --paper-light-green-a100: #ccff90;
      --paper-light-green-a200: #b2ff59;
      --paper-light-green-a400: #76ff03;
      --paper-light-green-a700: #64dd17;

      --paper-lime-50: #f9fbe7;
      --paper-lime-100: #f0f4c3;
      --paper-lime-200: #e6ee9c;
      --paper-lime-300: #dce775;
      --paper-lime-400: #d4e157;
      --paper-lime-500: #cddc39;
      --paper-lime-600: #c0ca33;
      --paper-lime-700: #afb42b;
      --paper-lime-800: #9e9d24;
      --paper-lime-900: #827717;
      --paper-lime-a100: #f4ff81;
      --paper-lime-a200: #eeff41;
      --paper-lime-a400: #c6ff00;
      --paper-lime-a700: #aeea00;

      --paper-yellow-50: #fffde7;
      --paper-yellow-100: #fff9c4;
      --paper-yellow-200: #fff59d;
      --paper-yellow-300: #fff176;
      --paper-yellow-400: #ffee58;
      --paper-yellow-500: #ffeb3b;
      --paper-yellow-600: #fdd835;
      --paper-yellow-700: #fbc02d;
      --paper-yellow-800: #f9a825;
      --paper-yellow-900: #f57f17;
      --paper-yellow-a100: #ffff8d;
      --paper-yellow-a200: #ffff00;
      --paper-yellow-a400: #ffea00;
      --paper-yellow-a700: #ffd600;

      --paper-amber-50: #fff8e1;
      --paper-amber-100: #ffecb3;
      --paper-amber-200: #ffe082;
      --paper-amber-300: #ffd54f;
      --paper-amber-400: #ffca28;
      --paper-amber-500: #ffc107;
      --paper-amber-600: #ffb300;
      --paper-amber-700: #ffa000;
      --paper-amber-800: #ff8f00;
      --paper-amber-900: #ff6f00;
      --paper-amber-a100: #ffe57f;
      --paper-amber-a200: #ffd740;
      --paper-amber-a400: #ffc400;
      --paper-amber-a700: #ffab00;

      --paper-orange-50: #fff3e0;
      --paper-orange-100: #ffe0b2;
      --paper-orange-200: #ffcc80;
      --paper-orange-300: #ffb74d;
      --paper-orange-400: #ffa726;
      --paper-orange-500: #ff9800;
      --paper-orange-600: #fb8c00;
      --paper-orange-700: #f57c00;
      --paper-orange-800: #ef6c00;
      --paper-orange-900: #e65100;
      --paper-orange-a100: #ffd180;
      --paper-orange-a200: #ffab40;
      --paper-orange-a400: #ff9100;
      --paper-orange-a700: #ff6500;

      --paper-deep-orange-50: #fbe9e7;
      --paper-deep-orange-100: #ffccbc;
      --paper-deep-orange-200: #ffab91;
      --paper-deep-orange-300: #ff8a65;
      --paper-deep-orange-400: #ff7043;
      --paper-deep-orange-500: #ff5722;
      --paper-deep-orange-600: #f4511e;
      --paper-deep-orange-700: #e64a19;
      --paper-deep-orange-800: #d84315;
      --paper-deep-orange-900: #bf360c;
      --paper-deep-orange-a100: #ff9e80;
      --paper-deep-orange-a200: #ff6e40;
      --paper-deep-orange-a400: #ff3d00;
      --paper-deep-orange-a700: #dd2c00;

      --paper-brown-50: #efebe9;
      --paper-brown-100: #d7ccc8;
      --paper-brown-200: #bcaaa4;
      --paper-brown-300: #a1887f;
      --paper-brown-400: #8d6e63;
      --paper-brown-500: #795548;
      --paper-brown-600: #6d4c41;
      --paper-brown-700: #5d4037;
      --paper-brown-800: #4e342e;
      --paper-brown-900: #3e2723;

      --paper-grey-50: #fafafa;
      --paper-grey-100: #f5f5f5;
      --paper-grey-200: #eeeeee;
      --paper-grey-300: #e0e0e0;
      --paper-grey-400: #bdbdbd;
      --paper-grey-500: #9e9e9e;
      --paper-grey-600: #757575;
      --paper-grey-700: #616161;
      --paper-grey-800: #424242;
      --paper-grey-900: #212121;

      --paper-blue-grey-50: #eceff1;
      --paper-blue-grey-100: #cfd8dc;
      --paper-blue-grey-200: #b0bec5;
      --paper-blue-grey-300: #90a4ae;
      --paper-blue-grey-400: #78909c;
      --paper-blue-grey-500: #607d8b;
      --paper-blue-grey-600: #546e7a;
      --paper-blue-grey-700: #455a64;
      --paper-blue-grey-800: #37474f;
      --paper-blue-grey-900: #263238;

      
      --dark-divider-opacity: 0.12;
      --dark-disabled-opacity: 0.38; 
      --dark-secondary-opacity: 0.54;
      --dark-primary-opacity: 0.87;

      
      --light-divider-opacity: 0.12;
      --light-disabled-opacity: 0.3; 
      --light-secondary-opacity: 0.7;
      --light-primary-opacity: 1.0;
}

</style>
</custom-style><custom-style>
  <style is="custom-style">html {
  --primary-text-color: var(--light-theme-text-color);
      --primary-background-color: var(--light-theme-background-color);
      --secondary-text-color: var(--light-theme-secondary-color);
      --disabled-text-color: var(--light-theme-disabled-color);
      --divider-color: var(--light-theme-divider-color);
      --error-color: var(--paper-deep-orange-a700);

      
      --primary-color: var(--paper-indigo-500);
      --light-primary-color: var(--paper-indigo-100);
      --dark-primary-color: var(--paper-indigo-700);

      --accent-color: var(--paper-pink-a200);
      --light-accent-color: var(--paper-pink-a100);
      --dark-accent-color: var(--paper-pink-a400);


      
      --light-theme-background-color: #ffffff;
      --light-theme-base-color: #000000;
      --light-theme-text-color: var(--paper-grey-900);
      --light-theme-secondary-color: #737373;  
      --light-theme-disabled-color: #9b9b9b;  
      --light-theme-divider-color: #dbdbdb;

      
      --dark-theme-background-color: var(--paper-grey-900);
      --dark-theme-base-color: #ffffff;
      --dark-theme-text-color: #ffffff;
      --dark-theme-secondary-color: #bcbcbc;  
      --dark-theme-disabled-color: #646464;  
      --dark-theme-divider-color: #3c3c3c;

      
      --text-primary-color: var(--dark-theme-text-color);
      --default-primary-color: var(--primary-color);
}

</style>
</custom-style>
<custom-style>
  <style is="custom-style">html {
  --paper-input-container-shared-input-style_-_position:  relative; --paper-input-container-shared-input-style_-_outline:  none; --paper-input-container-shared-input-style_-_box-shadow:  none; --paper-input-container-shared-input-style_-_padding:  0; --paper-input-container-shared-input-style_-_margin:  0; --paper-input-container-shared-input-style_-_width:  100%; --paper-input-container-shared-input-style_-_max-width:  100%; --paper-input-container-shared-input-style_-_background:  transparent; --paper-input-container-shared-input-style_-_border:  none; --paper-input-container-shared-input-style_-_color:  var(--paper-input-container-input-color, var(--primary-text-color)); --paper-input-container-shared-input-style_-_-webkit-appearance:  none; --paper-input-container-shared-input-style_-_text-align: apply-shim-inherit; --paper-input-container-shared-input-style_-_vertical-align:  var(--paper-input-container-input-align, bottom); --paper-input-container-shared-input-style_-_font-family:  var(--paper-font-subhead_-_font-family); --paper-input-container-shared-input-style_-_-webkit-font-smoothing:  var(--paper-font-subhead_-_-webkit-font-smoothing); --paper-input-container-shared-input-style_-_font-size:  var(--paper-font-subhead_-_font-size); --paper-input-container-shared-input-style_-_font-weight:  var(--paper-font-subhead_-_font-weight); --paper-input-container-shared-input-style_-_line-height:  var(--paper-font-subhead_-_line-height);;
}

</style>
</custom-style>
<!----> <iron-iconset-svg name="colab" size="24" style="display: none;">
    <!--?lit$939691256$-->
<svg>
  <defs>
    <g id="monochrome-drive-logo">
      <path d="m8.83,2.66l6.66,0l5.83,10l-6.66,0l-5.83,-10z">
      </path>
      <path d="m11,10l-5.83,10l-3.33,-5.83l5.83,-10l3.33,5.83z">
      </path>
      <path d="m10.33,14.16l11.66,0l-3.33,5.83l-11.66,0l3.33,-5.83z">
      </path>
    </g>
    <g id="files-up-one-level">
      <path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2zM11 13v4h-4v-4H4l5-5 5 5h-3z">
      </path>
    </g>
    <!--?lit$939691256$-->
    <g id="experiment">
      <path d="M20.72 17.71L15 9.82V5.08h2v-2H7v2h2v4.73L3.14 17.9c-.44.61-.5 1.41-.16 2.08.34.67 1.03 1.09 1.78 1.09h14.5c1.1 0 2-.9 2-2 0-.52-.21-1-.54-1.36z"></path>
    </g>
    <g id="edit-disabled">
      <path d="M20.7,7c0.4-0.4,0.4-1,0-1.4l-2.3-2.3c-0.4-0.4-1-0.4-1.4,0l-1.8,1.8l3.8,3.8L20.7,7z"></path>
      <polygon points="18.2,9.6 14.4,5.8 10.9,9.3 14.7,13.1 "></polygon>
      <polygon points="10.3,10 3.3,3 2,4.3 4.3,6.6 9,11.3 3,17.2 3,21 6.8,21 12.7,15 16.8,19.1 19.7,22 21,20.7 14,13.7 "></polygon>
    </g>
    <g id="copy-to-scratch">
      <!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <path d="M18,21H4V7H2V21a2,2,0,0,0,2,2H18Z"></path>
      <path d="M18,15V13h2v2ZM6,13v2H8.59L5,18.59,6.41,20,10,16.41V19h2V13Zm8,4v2h2V17ZM6,9v2H8V9ZM18,5V7h2V5ZM10,1V3h2V1ZM6,3H8V1A2,2,0,0,0,6,3ZM20,17H18v2A2,2,0,0,0,20,17ZM18,9v2h2V9ZM6,5V7H8V5Zm8-4V3h2V1Zm4,0V3h2A2,2,0,0,0,18,1Z"></path></svg>
    </g>
    <g id="mirror-cell">
      <!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg>
    </g>
    <g id="folder-refresh">
      <path d="M4,18V8H20v3h2V8a2,2,0,0,0-2-2H12L10,4H4A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2h9l-1-2Z"></path>
      <path d="M18,12.25A4.75,4.75,0,1,0,22.64,18H21.08a3.26,3.26,0,1,1-.76-3.25H18.5v1.5h4.25V12h-1.5v1.56A4.74,4.74,0,0,0,18,12.25Z"></path>
    </g>
    <!--?lit$939691256$-->
    <g id="file-upload">
      <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm4 18H6V4h7v5h5v11zM8 15.01l1.41 1.41L11 14.84V19h2v-4.16l1.59 1.59L16 15.01 12.01 11z"></path>
    </g>
    <!--?lit$939691256$-->
    <g id="drive-folder">
      <path d="M20,6H12L10,4H4A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H20a2,2,0,0,0,2-2V8A2,2,0,0,0,20,6ZM13.57,9.32,13,8.4l.34-.6h3.11l3.69,6.5H16.38M12.11,17l-.67,1.2h-1L9,15.42,12.72,9l2,3.46h0M19.3,18.2H12.09l.67-1.2,1.15-2h6.64l.34.6Z"></path>
    </g>
    <g id="detach-drive">
      <path d="M12.72,9l2,3.46h0l-.26.47,2,2h4.1l.34.6L19.45,18l1.69,1.69A2,2,0,0,0,22,18V8a2,2,0,0,0-2-2H12L10,4H5.5l6.4,6.4Zm.66-1.17h3.11l3.69,6.5H16.38l-2.81-5L13,8.4Z"></path>
      <path d="M22.19,22.19,1.81,1.81.4,3.22,2.25,5.07A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H17.17l3.61,3.61Zm-11.73-4L9,15.42l1.3-2.26,2.35,2.36.17.17L12.11,17l-.67,1.2Zm1.63,0,.67-1.2.51-.9,2.1,2.1Z"></path>
    </g>
    <g id="command-palette">
      <!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <path d="M21,3H3A2,2,0,0,0,1,5V17a2,2,0,0,0,2,2H21a2,2,0,0,0,2-2V5A2,2,0,0,0,21,3Zm0,2V17H3V5"></path>
      <rect x="5" y="12" width="11" height="2"></rect>
      <rect x="5" y="8" width="11" height="2"></rect>
      <rect x="17" y="8" width="2" height="2"></rect>
      <rect x="17" y="12" width="2" height="2"></rect></svg>
    </g>
    <g id="pen_spark">
      <!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <path d="M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z"></path></svg>
    </g>
    <g id="info_spark">
      <path d="M11,17V11h2v6Zm1-7a1,1,0,1,1,.71-.29A1,1,0,0,1,12,10Zm7.85.5L21.5,8.85a9.62,9.62,0,0,1,.38,1.54A10.27,10.27,0,0,1,22,12a9.74,9.74,0,0,1-.79,3.9,10,10,0,0,1-5.31,5.31A9.74,9.74,0,0,1,12,22a9.74,9.74,0,0,1-3.9-.79A10,10,0,0,1,2.79,15.9,9.74,9.74,0,0,1,2,12a9.74,9.74,0,0,1,.79-3.9A10,10,0,0,1,8.1,2.79,9.74,9.74,0,0,1,12,2a10.27,10.27,0,0,1,1.61.13,9.62,9.62,0,0,1,1.54.38L13.5,4.15q-.37-.08-.74-.11A7.42,7.42,0,0,0,12,4,7.72,7.72,0,0,0,6.33,6.33,7.72,7.72,0,0,0,4,12a7.72,7.72,0,0,0,2.33,5.68A7.72,7.72,0,0,0,12,20a7.72,7.72,0,0,0,5.68-2.33A7.72,7.72,0,0,0,20,12a7.42,7.42,0,0,0,0-.76Q19.93,10.87,19.85,10.5ZM17.5,12A5.46,5.46,0,0,0,12,6.5a5.31,5.31,0,0,0,3.9-1.6A5.31,5.31,0,0,0,17.5,1a5.31,5.31,0,0,0,1.6,3.9A5.31,5.31,0,0,0,23,6.5,5.46,5.46,0,0,0,17.5,12Z"></path>
    </g>
    <g id="supervised_user_circle">
      <!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <path d="M 9.9582499,21.35987 C 10.842594,19.382021 12.606506,17.817985 14.716516,17.279566 16.41989,16.686126 18.317872,16.656934 20.03281,17.22182 22.44796,13.614773 22.030038,8.3464205 18.90388,5.2829204 15.571823,1.7178775 9.420202,1.3974701 5.769982,4.6587762 3.3377473,6.6864955 2.0387092,9.9509867 2.4603251,13.095093 c 0.1463132,1.333314 0.5764246,2.646122 1.3212592,3.766896 2.6970808,-1.363945 5.949002,-1.659216 8.8152407,-0.659689 -1.241623,0.378685 -1.898774,2.052201 -3.36112,1.793886 -1.3568211,-0.0051 -2.7332571,0.237474 -3.9549301,0.844871 1.267179,1.273083 2.9115843,2.175024 4.677475,2.518813 z m 2.0388991,2.638757 C 6.6511222,24.107652 1.5826283,20.137336 0.35384605,14.940954 -0.87900818,10.201889 1.1156845,4.8167637 5.2106158,2.1027623 9.1389196,-0.63068336 14.72247,-0.71788883 18.666809,2.0315664 c 3.770731,2.4797903 5.923366,7.1940181 5.205845,11.6657356 -0.561363,4.25325 -3.592409,8.039095 -7.614261,9.524313 -1.356179,0.518542 -2.808321,0.792183 -4.261244,0.777012 z M 8.9987675,13.80343 C 6.3557134,13.92683 4.1587181,11.059046 4.9242904,8.5324696 5.5067387,6.0598075 8.5843425,4.6198007 10.844905,5.8135307 c 2.251036,1.0498371 3.121931,4.2263483 1.586973,6.2196153 -0.777226,1.086407 -2.083619,1.810868 -3.4331105,1.770284 z m 0,-2.39887 C 10.82036,11.536018 11.503688,8.682573 9.8022883,7.9757151 8.3387516,7.206114 6.5439498,8.9550798 7.3889517,10.413062 c 0.2986856,0.592673 0.9351214,1.021277 1.6098158,0.991498 z m 8.3954675,3.598305 c -2.036107,0.118847 -3.612999,-2.238286 -2.81499,-4.095085 0.678013,-1.9105614 3.4227,-2.5652777 4.869242,-1.1247834 1.400594,1.2764214 1.220774,3.8379454 -0.469812,4.7846484 -0.472701,0.291047 -1.028762,0.44763 -1.58444,0.43522 z"></path></svg>
    </g>
  </defs>
</svg>
  </iron-iconset-svg><iron-iconset-svg name="icons" size="24" style="display: none;">
<svg><defs>
<g id="3d-rotation"><path d="M7.52 21.48C4.25 19.94 1.91 16.76 1.55 13H.05C.56 19.16 5.71 24 12 24l.66-.03-3.81-3.81-1.33 1.32zm.89-6.52c-.19 0-.37-.03-.52-.08-.16-.06-.29-.13-.4-.24-.11-.1-.2-.22-.26-.37-.06-.14-.09-.3-.09-.47h-1.3c0 .36.07.68.21.95.14.27.33.5.56.69.24.18.51.32.82.41.3.1.62.15.96.15.37 0 .72-.05 1.03-.15.32-.1.6-.25.83-.44s.42-.43.55-.72c.13-.29.2-.61.2-.97 0-.19-.02-.38-.07-.56-.05-.18-.12-.35-.23-.51-.1-.16-.24-.3-.4-.43-.17-.13-.37-.23-.61-.31.2-.09.37-.2.52-.33.15-.13.27-.27.37-.42.1-.15.17-.3.22-.46.05-.16.07-.32.07-.48 0-.36-.06-.68-.18-.96-.12-.28-.29-.51-.51-.69-.2-.19-.47-.33-.77-.43C9.1 8.05 8.76 8 8.39 8c-.36 0-.69.05-1 .16-.3.11-.57.26-.79.45-.21.19-.38.41-.51.67-.12.26-.18.54-.18.85h1.3c0-.17.03-.32.09-.45s.14-.25.25-.34c.11-.09.23-.17.38-.22.15-.05.3-.08.48-.08.4 0 .7.1.89.31.19.2.29.49.29.86 0 .18-.03.34-.08.49-.05.15-.14.27-.25.37-.11.1-.25.18-.41.24-.16.06-.36.09-.58.09H7.5v1.03h.77c.22 0 .42.02.6.07s.33.13.45.23c.12.11.22.24.29.4.07.16.1.35.1.57 0 .41-.12.72-.35.93-.23.23-.55.33-.95.33zm8.55-5.92c-.32-.33-.7-.59-1.14-.77-.43-.18-.92-.27-1.46-.27H12v8h2.3c.55 0 1.06-.09 1.51-.27.45-.18.84-.43 1.16-.76.32-.33.57-.73.74-1.19.17-.47.26-.99.26-1.57v-.4c0-.58-.09-1.1-.26-1.57-.18-.47-.43-.87-.75-1.2zm-.39 3.16c0 .42-.05.79-.14 1.13-.1.33-.24.62-.43.85-.19.23-.43.41-.71.53-.29.12-.62.18-.99.18h-.91V9.12h.97c.72 0 1.27.23 1.64.69.38.46.57 1.12.57 1.99v.4zM12 0l-.66.03 3.81 3.81 1.33-1.33c3.27 1.55 5.61 4.72 5.96 8.48h1.5C23.44 4.84 18.29 0 12 0z"></path></g>
<g id="accessibility"><path d="M12 2c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 7h-6v13h-2v-6h-2v6H9V9H3V7h18v2z"></path></g>
<g id="accessible"><circle cx="12" cy="4" r="2"></circle><path d="M19 13v-2c-1.54.02-3.09-.75-4.07-1.83l-1.29-1.43c-.17-.19-.38-.34-.61-.45-.01 0-.01-.01-.02-.01H13c-.35-.2-.75-.3-1.19-.26C10.76 7.11 10 8.04 10 9.09V15c0 1.1.9 2 2 2h5v5h2v-5.5c0-1.1-.9-2-2-2h-3v-3.45c1.29 1.07 3.25 1.94 5 1.95zm-6.17 5c-.41 1.16-1.52 2-2.83 2-1.66 0-3-1.34-3-3 0-1.31.84-2.41 2-2.83V12.1c-2.28.46-4 2.48-4 4.9 0 2.76 2.24 5 5 5 2.42 0 4.44-1.72 4.9-4h-2.07z"></path></g>
<g id="account-balance"><path d="M4 10v7h3v-7H4zm6 0v7h3v-7h-3zM2 22h19v-3H2v3zm14-12v7h3v-7h-3zm-4.5-9L2 6v2h19V6l-9.5-5z"></path></g>
<g id="account-balance-wallet"><path d="M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"></path></g>
<g id="account-box"><path d="M3 5v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2H5c-1.11 0-2 .9-2 2zm12 4c0 1.66-1.34 3-3 3s-3-1.34-3-3 1.34-3 3-3 3 1.34 3 3zm-9 8c0-2 4-3.1 6-3.1s6 1.1 6 3.1v1H6v-1z"></path></g>
<g id="account-circle"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"></path></g>
<g id="add"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g>
<g id="add-alert"><path d="M10.01 21.01c0 1.1.89 1.99 1.99 1.99s1.99-.89 1.99-1.99h-3.98zm8.87-4.19V11c0-3.25-2.25-5.97-5.29-6.69v-.72C13.59 2.71 12.88 2 12 2s-1.59.71-1.59 1.59v.72C7.37 5.03 5.12 7.75 5.12 11v5.82L3 18.94V20h18v-1.06l-2.12-2.12zM16 13.01h-3v3h-2v-3H8V11h3V8h2v3h3v2.01z"></path></g>
<g id="add-box"><path d="M19 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"></path></g>
<g id="add-circle"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"></path></g>
<g id="add-circle-outline"><path d="M13 7h-2v4H7v2h4v4h2v-4h4v-2h-4V7zm-1-5C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></g>
<g id="add-shopping-cart"><path d="M11 9h2V6h3V4h-3V1h-2v3H8v2h3v3zm-4 9c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zm10 0c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2zm-9.83-3.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.86-7.01L19.42 4h-.01l-1.1 2-2.76 5H8.53l-.13-.27L6.16 6l-.95-2-.94-2H1v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.13 0-.25-.11-.25-.25z"></path></g>
<g id="alarm"><path d="M22 5.72l-4.6-3.86-1.29 1.53 4.6 3.86L22 5.72zM7.88 3.39L6.6 1.86 2 5.71l1.29 1.53 4.59-3.85zM12.5 8H11v6l4.75 2.85.75-1.23-4-2.37V8zM12 4c-4.97 0-9 4.03-9 9s4.02 9 9 9c4.97 0 9-4.03 9-9s-4.03-9-9-9zm0 16c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7z"></path></g>
<g id="alarm-add"><path d="M7.88 3.39L6.6 1.86 2 5.71l1.29 1.53 4.59-3.85zM22 5.72l-4.6-3.86-1.29 1.53 4.6 3.86L22 5.72zM12 4c-4.97 0-9 4.03-9 9s4.02 9 9 9c4.97 0 9-4.03 9-9s-4.03-9-9-9zm0 16c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7zm1-11h-2v3H8v2h3v3h2v-3h3v-2h-3V9z"></path></g>
<g id="alarm-off"><path d="M12 6c3.87 0 7 3.13 7 7 0 .84-.16 1.65-.43 2.4l1.52 1.52c.58-1.19.91-2.51.91-3.92 0-4.97-4.03-9-9-9-1.41 0-2.73.33-3.92.91L9.6 6.43C10.35 6.16 11.16 6 12 6zm10-.28l-4.6-3.86-1.29 1.53 4.6 3.86L22 5.72zM2.92 2.29L1.65 3.57 2.98 4.9l-1.11.93 1.42 1.42 1.11-.94.8.8C3.83 8.69 3 10.75 3 13c0 4.97 4.02 9 9 9 2.25 0 4.31-.83 5.89-2.2l2.2 2.2 1.27-1.27L3.89 3.27l-.97-.98zm13.55 16.1C15.26 19.39 13.7 20 12 20c-3.87 0-7-3.13-7-7 0-1.7.61-3.26 1.61-4.47l9.86 9.86zM8.02 3.28L6.6 1.86l-.86.71 1.42 1.42.86-.71z"></path></g>
<g id="alarm-on"><path d="M22 5.72l-4.6-3.86-1.29 1.53 4.6 3.86L22 5.72zM7.88 3.39L6.6 1.86 2 5.71l1.29 1.53 4.59-3.85zM12 4c-4.97 0-9 4.03-9 9s4.02 9 9 9c4.97 0 9-4.03 9-9s-4.03-9-9-9zm0 16c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7zm-1.46-5.47L8.41 12.4l-1.06 1.06 3.18 3.18 6-6-1.06-1.06-4.93 4.95z"></path></g>
<g id="all-out"><path d="M16.21 4.16l4 4v-4zm4 12l-4 4h4zm-12 4l-4-4v4zm-4-12l4-4h-4zm12.95-.95c-2.73-2.73-7.17-2.73-9.9 0s-2.73 7.17 0 9.9 7.17 2.73 9.9 0 2.73-7.16 0-9.9zm-1.1 8.8c-2.13 2.13-5.57 2.13-7.7 0s-2.13-5.57 0-7.7 5.57-2.13 7.7 0 2.13 5.57 0 7.7z"></path></g>
<g id="android"><path d="M6 18c0 .55.45 1 1 1h1v3.5c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5V19h2v3.5c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5V19h1c.55 0 1-.45 1-1V8H6v10zM3.5 8C2.67 8 2 8.67 2 9.5v7c0 .83.67 1.5 1.5 1.5S5 17.33 5 16.5v-7C5 8.67 4.33 8 3.5 8zm17 0c-.83 0-1.5.67-1.5 1.5v7c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5v-7c0-.83-.67-1.5-1.5-1.5zm-4.97-5.84l1.3-1.3c.2-.2.2-.51 0-.71-.2-.2-.51-.2-.71 0l-1.48 1.48C13.85 1.23 12.95 1 12 1c-.96 0-1.86.23-2.66.63L7.85.15c-.2-.2-.51-.2-.71 0-.2.2-.2.51 0 .71l1.31 1.31C6.97 3.26 6 5.01 6 7h12c0-1.99-.97-3.75-2.47-4.84zM10 5H9V4h1v1zm5 0h-1V4h1v1z"></path></g>
<g id="announcement"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-7 9h-2V5h2v6zm0 4h-2v-2h2v2z"></path></g>
<g id="apps"><path d="M4 8h4V4H4v4zm6 12h4v-4h-4v4zm-6 0h4v-4H4v4zm0-6h4v-4H4v4zm6 0h4v-4h-4v4zm6-10v4h4V4h-4zm-6 4h4V4h-4v4zm6 6h4v-4h-4v4zm0 6h4v-4h-4v4z"></path></g>
<g id="archive"><path d="M20.54 5.23l-1.39-1.68C18.88 3.21 18.47 3 18 3H6c-.47 0-.88.21-1.16.55L3.46 5.23C3.17 5.57 3 6.02 3 6.5V19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V6.5c0-.48-.17-.93-.46-1.27zM12 17.5L6.5 12H10v-2h4v2h3.5L12 17.5zM5.12 5l.81-1h12l.94 1H5.12z"></path></g>
<g id="arrow-back"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></g>
<g id="arrow-downward"><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></g>
<g id="arrow-drop-down"><path d="M7 10l5 5 5-5z"></path></g>
<g id="arrow-drop-down-circle"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 12l-4-4h8l-4 4z"></path></g>
<g id="arrow-drop-up"><path d="M7 14l5-5 5 5z"></path></g>
<g id="arrow-forward"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"></path></g>
<g id="arrow-upward"><path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z"></path></g>
<g id="aspect-ratio"><path d="M19 12h-2v3h-3v2h5v-5zM7 9h3V7H5v5h2V9zm14-6H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16.01H3V4.99h18v14.02z"></path></g>
<g id="assessment"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"></path></g>
<g id="assignment"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm2 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"></path></g>
<g id="assignment-ind"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm0 4c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6 12H6v-1.4c0-2 4-3.1 6-3.1s6 1.1 6 3.1V19z"></path></g>
<g id="assignment-late"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-6 15h-2v-2h2v2zm0-4h-2V8h2v6zm-1-9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z"></path></g>
<g id="assignment-return"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm4 12h-4v3l-5-5 5-5v3h4v4z"></path></g>
<g id="assignment-returned"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm0 15l-5-5h3V9h4v4h3l-5 5z"></path></g>
<g id="assignment-turned-in"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm-2 14l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"></path></g>
<g id="attachment"><path d="M2 12.5C2 9.46 4.46 7 7.5 7H18c2.21 0 4 1.79 4 4s-1.79 4-4 4H9.5C8.12 15 7 13.88 7 12.5S8.12 10 9.5 10H17v2H9.41c-.55 0-.55 1 0 1H18c1.1 0 2-.9 2-2s-.9-2-2-2H7.5C5.57 9 4 10.57 4 12.5S5.57 16 7.5 16H17v2H7.5C4.46 18 2 15.54 2 12.5z"></path></g>
<g id="autorenew"><path d="M12 6v3l4-4-4-4v3c-4.42 0-8 3.58-8 8 0 1.57.46 3.03 1.24 4.26L6.7 14.8c-.45-.83-.7-1.79-.7-2.8 0-3.31 2.69-6 6-6zm6.76 1.74L17.3 9.2c.44.84.7 1.79.7 2.8 0 3.31-2.69 6-6 6v-3l-4 4 4 4v-3c4.42 0 8-3.58 8-8 0-1.57-.46-3.03-1.24-4.26z"></path></g>
<g id="backspace"><path d="M22 3H7c-.69 0-1.23.35-1.59.88L0 12l5.41 8.11c.36.53.9.89 1.59.89h15c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-3 12.59L17.59 17 14 13.41 10.41 17 9 15.59 12.59 12 9 8.41 10.41 7 14 10.59 17.59 7 19 8.41 15.41 12 19 15.59z"></path></g>
<g id="backup"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z"></path></g>
<g id="block"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zM4 12c0-4.42 3.58-8 8-8 1.85 0 3.55.63 4.9 1.69L5.69 16.9C4.63 15.55 4 13.85 4 12zm8 8c-1.85 0-3.55-.63-4.9-1.69L18.31 7.1C19.37 8.45 20 10.15 20 12c0 4.42-3.58 8-8 8z"></path></g>
<g id="book"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"></path></g>
<g id="bookmark"><path d="M17 3H7c-1.1 0-1.99.9-1.99 2L5 21l7-3 7 3V5c0-1.1-.9-2-2-2z"></path></g>
<g id="bookmark-border"><path d="M17 3H7c-1.1 0-1.99.9-1.99 2L5 21l7-3 7 3V5c0-1.1-.9-2-2-2zm0 15l-5-2.18L7 18V5h10v13z"></path></g>
<g id="bug-report"><path d="M20 8h-2.81c-.45-.78-1.07-1.45-1.82-1.96L17 4.41 15.59 3l-2.17 2.17C12.96 5.06 12.49 5 12 5c-.49 0-.96.06-1.41.17L8.41 3 7 4.41l1.62 1.63C7.88 6.55 7.26 7.22 6.81 8H4v2h2.09c-.05.33-.09.66-.09 1v1H4v2h2v1c0 .34.04.67.09 1H4v2h2.81c1.04 1.79 2.97 3 5.19 3s4.15-1.21 5.19-3H20v-2h-2.09c.05-.33.09-.66.09-1v-1h2v-2h-2v-1c0-.34-.04-.67-.09-1H20V8zm-6 8h-4v-2h4v2zm0-4h-4v-2h4v2z"></path></g>
<g id="build"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"></path></g>
<g id="cached"><path d="M19 8l-4 4h3c0 3.31-2.69 6-6 6-1.01 0-1.97-.25-2.8-.7l-1.46 1.46C8.97 19.54 10.43 20 12 20c4.42 0 8-3.58 8-8h3l-4-4zM6 12c0-3.31 2.69-6 6-6 1.01 0 1.97.25 2.8.7l1.46-1.46C15.03 4.46 13.57 4 12 4c-4.42 0-8 3.58-8 8H1l4 4 4-4H6z"></path></g>
<g id="camera-enhance"><path d="M9 3L7.17 5H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2h-3.17L15 3H9zm3 15c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-1l1.25-2.75L16 13l-2.75-1.25L12 9l-1.25 2.75L8 13l2.75 1.25z"></path></g>
<g id="cancel"><path d="M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm5 13.59L15.59 17 12 13.41 8.41 17 7 15.59 10.59 12 7 8.41 8.41 7 12 10.59 15.59 7 17 8.41 13.41 12 17 15.59z"></path></g>
<g id="card-giftcard"><path d="M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v6z"></path></g>
<g id="card-membership"><path d="M20 2H4c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h4v5l4-2 4 2v-5h4c1.11 0 2-.89 2-2V4c0-1.11-.89-2-2-2zm0 13H4v-2h16v2zm0-5H4V4h16v6z"></path></g>
<g id="card-travel"><path d="M20 6h-3V4c0-1.11-.89-2-2-2H9c-1.11 0-2 .89-2 2v2H4c-1.11 0-2 .89-2 2v11c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zM9 4h6v2H9V4zm11 15H4v-2h16v2zm0-5H4V8h3v2h2V8h6v2h2V8h3v6z"></path></g>
<g id="change-history"><path d="M12 7.77L18.39 18H5.61L12 7.77M12 4L2 20h20L12 4z"></path></g>
<g id="check"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g>
<g id="check-box"><path d="M19 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.11 0 2-.9 2-2V5c0-1.1-.89-2-2-2zm-9 14l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></g>
<g id="check-box-outline-blank"><path d="M19 5v14H5V5h14m0-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"></path></g>
<g id="check-circle"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></g>
<g id="chevron-left"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></g>
<g id="chevron-right"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></g>
<g id="chrome-reader-mode"><path d="M13 12h7v1.5h-7zm0-2.5h7V11h-7zm0 5h7V16h-7zM21 4H3c-1.1 0-2 .9-2 2v13c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 15h-9V6h9v13z"></path></g>
<g id="class"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"></path></g>
<g id="clear"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g>
<g id="close"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g>
<g id="cloud"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"></path></g>
<g id="cloud-circle"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.5 14H8c-1.66 0-3-1.34-3-3s1.34-3 3-3l.14.01C8.58 8.28 10.13 7 12 7c2.21 0 4 1.79 4 4h.5c1.38 0 2.5 1.12 2.5 2.5S17.88 16 16.5 16z"></path></g>
<g id="cloud-done"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM10 17l-3.5-3.5 1.41-1.41L10 14.17 15.18 9l1.41 1.41L10 17z"></path></g>
<g id="cloud-download"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"></path></g>
<g id="cloud-off"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4c-1.48 0-2.85.43-4.01 1.17l1.46 1.46C10.21 6.23 11.08 6 12 6c3.04 0 5.5 2.46 5.5 5.5v.5H19c1.66 0 3 1.34 3 3 0 1.13-.64 2.11-1.56 2.62l1.45 1.45C23.16 18.16 24 16.68 24 15c0-2.64-2.05-4.78-4.65-4.96zM3 5.27l2.75 2.74C2.56 8.15 0 10.77 0 14c0 3.31 2.69 6 6 6h11.73l2 2L21 20.73 4.27 4 3 5.27zM7.73 10l8 8H6c-2.21 0-4-1.79-4-4s1.79-4 4-4h1.73z"></path></g>
<g id="cloud-queue"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM19 18H6c-2.21 0-4-1.79-4-4s1.79-4 4-4h.71C7.37 7.69 9.48 6 12 6c3.04 0 5.5 2.46 5.5 5.5v.5H19c1.66 0 3 1.34 3 3s-1.34 3-3 3z"></path></g>
<g id="cloud-upload"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z"></path></g>
<g id="code"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"></path></g>
<g id="compare-arrows"><path d="M9.01 14H2v2h7.01v3L13 15l-3.99-4v3zm5.98-1v-3H22V8h-7.01V5L11 9l3.99 4z"></path></g>
<g id="content-copy"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"></path></g>
<g id="content-cut"><path d="M9.64 7.64c.23-.5.36-1.05.36-1.64 0-2.21-1.79-4-4-4S2 3.79 2 6s1.79 4 4 4c.59 0 1.14-.13 1.64-.36L10 12l-2.36 2.36C7.14 14.13 6.59 14 6 14c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4c0-.59-.13-1.14-.36-1.64L12 14l7 7h3v-1L9.64 7.64zM6 8c-1.1 0-2-.89-2-2s.9-2 2-2 2 .89 2 2-.9 2-2 2zm0 12c-1.1 0-2-.89-2-2s.9-2 2-2 2 .89 2 2-.9 2-2 2zm6-7.5c-.28 0-.5-.22-.5-.5s.22-.5.5-.5.5.22.5.5-.22.5-.5.5zM19 3l-6 6 2 2 7-7V3z"></path></g>
<g id="content-paste"><path d="M19 2h-4.18C14.4.84 13.3 0 12 0c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm7 18H5V4h2v3h10V4h2v16z"></path></g>
<g id="copyright"><path d="M10.08 10.86c.05-.33.16-.62.3-.87s.34-.46.59-.62c.24-.15.54-.22.91-.23.23.01.44.05.63.13.2.09.38.21.52.36s.25.33.34.53.13.42.14.64h1.79c-.02-.47-.11-.9-.28-1.29s-.4-.73-.7-1.01-.66-.5-1.08-.66-.88-.23-1.39-.23c-.65 0-1.22.11-1.7.34s-.88.53-1.2.92-.56.84-.71 1.36S8 11.29 8 11.87v.27c0 .58.08 1.12.23 1.64s.39.97.71 1.35.72.69 1.2.91 1.05.34 1.7.34c.47 0 .91-.08 1.32-.23s.77-.36 1.08-.63.56-.58.74-.94.29-.74.3-1.15h-1.79c-.01.21-.06.4-.15.58s-.21.33-.36.46-.32.23-.52.3c-.19.07-.39.09-.6.1-.36-.01-.66-.08-.89-.23-.25-.16-.45-.37-.59-.62s-.25-.55-.3-.88-.08-.67-.08-1v-.27c0-.35.03-.68.08-1.01zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></g>
<g id="create"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"></path></g>
<g id="create-new-folder"><path d="M20 6h-8l-2-2H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-1 8h-3v3h-2v-3h-3v-2h3V9h2v3h3v2z"></path></g>
<g id="credit-card"><path d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"></path></g>
<g id="dashboard"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"></path></g>
<g id="date-range"><path d="M9 11H7v2h2v-2zm4 0h-2v2h2v-2zm4 0h-2v2h2v-2zm2-7h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V9h14v11z"></path></g>
<g id="delete"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"></path></g>
<g id="delete-forever"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zm2.46-7.12l1.41-1.41L12 12.59l2.12-2.12 1.41 1.41L13.41 14l2.12 2.12-1.41 1.41L12 15.41l-2.12 2.12-1.41-1.41L10.59 14l-2.13-2.12zM15.5 4l-1-1h-5l-1 1H5v2h14V4z"></path></g>
<g id="delete-sweep"><path d="M15 16h4v2h-4zm0-8h7v2h-7zm0 4h6v2h-6zM3 18c0 1.1.9 2 2 2h6c1.1 0 2-.9 2-2V8H3v10zM14 5h-3l-1-1H6L5 5H2v2h12z"></path></g>
<g id="description"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"></path></g>
<g id="dns"><path d="M20 13H4c-.55 0-1 .45-1 1v6c0 .55.45 1 1 1h16c.55 0 1-.45 1-1v-6c0-.55-.45-1-1-1zM7 19c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zM20 3H4c-.55 0-1 .45-1 1v6c0 .55.45 1 1 1h16c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1zM7 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"></path></g>
<g id="done"><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"></path></g>
<g id="done-all"><path d="M18 7l-1.41-1.41-6.34 6.34 1.41 1.41L18 7zm4.24-1.41L11.66 16.17 7.48 12l-1.41 1.41L11.66 19l12-12-1.42-1.41zM.41 13.41L6 19l1.41-1.41L1.83 12 .41 13.41z"></path></g>
<g id="donut-large"><path d="M11 5.08V2c-5 .5-9 4.81-9 10s4 9.5 9 10v-3.08c-3-.48-6-3.4-6-6.92s3-6.44 6-6.92zM18.97 11H22c-.47-5-4-8.53-9-9v3.08C16 5.51 18.54 8 18.97 11zM13 18.92V22c5-.47 8.53-4 9-9h-3.03c-.43 3-2.97 5.49-5.97 5.92z"></path></g>
<g id="donut-small"><path d="M11 9.16V2c-5 .5-9 4.79-9 10s4 9.5 9 10v-7.16c-1-.41-2-1.52-2-2.84s1-2.43 2-2.84zM14.86 11H22c-.48-4.75-4-8.53-9-9v7.16c1 .3 1.52.98 1.86 1.84zM13 14.84V22c5-.47 8.52-4.25 9-9h-7.14c-.34.86-.86 1.54-1.86 1.84z"></path></g>
<g id="drafts"><path d="M21.99 8c0-.72-.37-1.35-.94-1.7L12 1 2.95 6.3C2.38 6.65 2 7.28 2 8v10c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2l-.01-10zM12 13L3.74 7.84 12 3l8.26 4.84L12 13z"></path></g>
<g id="eject"><path d="M5 17h14v2H5zm7-12L5.33 15h13.34z"></path></g>
<g id="error"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"></path></g>
<g id="error-outline"><path d="M11 15h2v2h-2zm0-8h2v6h-2zm.99-5C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"></path></g>
<g id="euro-symbol"><path d="M15 18.5c-2.51 0-4.68-1.42-5.76-3.5H15v-2H8.58c-.05-.33-.08-.66-.08-1s.03-.67.08-1H15V9H9.24C10.32 6.92 12.5 5.5 15 5.5c1.61 0 3.09.59 4.23 1.57L21 5.3C19.41 3.87 17.3 3 15 3c-3.92 0-7.24 2.51-8.48 6H3v2h3.06c-.04.33-.06.66-.06 1 0 .34.02.67.06 1H3v2h3.52c1.24 3.49 4.56 6 8.48 6 2.31 0 4.41-.87 6-2.3l-1.78-1.77c-1.13.98-2.6 1.57-4.22 1.57z"></path></g>
<g id="event"><path d="M17 12h-5v5h5v-5zM16 1v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-1V1h-2zm3 18H5V8h14v11z"></path></g>
<g id="event-seat"><path d="M4 18v3h3v-3h10v3h3v-6H4zm15-8h3v3h-3zM2 10h3v3H2zm15 3H7V5c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2v8z"></path></g>
<g id="exit-to-app"><path d="M10.09 15.59L11.5 17l5-5-5-5-1.41 1.41L12.67 11H3v2h9.67l-2.58 2.59zM19 3H5c-1.11 0-2 .9-2 2v4h2V5h14v14H5v-4H3v4c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"></path></g>
<g id="expand-less"><path d="M12 8l-6 6 1.41 1.41L12 10.83l4.59 4.58L18 14z"></path></g>
<g id="expand-more"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></g>
<g id="explore"><path d="M12 10.9c-.61 0-1.1.49-1.1 1.1s.49 1.1 1.1 1.1c.61 0 1.1-.49 1.1-1.1s-.49-1.1-1.1-1.1zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm2.19 12.19L6 18l3.81-8.19L18 6l-3.81 8.19z"></path></g>
<g id="extension"><path d="M20.5 11H19V7c0-1.1-.9-2-2-2h-4V3.5C13 2.12 11.88 1 10.5 1S8 2.12 8 3.5V5H4c-1.1 0-1.99.9-1.99 2v3.8H3.5c1.49 0 2.7 1.21 2.7 2.7s-1.21 2.7-2.7 2.7H2V20c0 1.1.9 2 2 2h3.8v-1.5c0-1.49 1.21-2.7 2.7-2.7 1.49 0 2.7 1.21 2.7 2.7V22H17c1.1 0 2-.9 2-2v-4h1.5c1.38 0 2.5-1.12 2.5-2.5S21.88 11 20.5 11z"></path></g>
<g id="face"><path d="M9 11.75c-.69 0-1.25.56-1.25 1.25s.56 1.25 1.25 1.25 1.25-.56 1.25-1.25-.56-1.25-1.25-1.25zm6 0c-.69 0-1.25.56-1.25 1.25s.56 1.25 1.25 1.25 1.25-.56 1.25-1.25-.56-1.25-1.25-1.25zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8 0-.29.02-.58.05-.86 2.36-1.05 4.23-2.98 5.21-5.37C11.07 8.33 14.05 10 17.42 10c.78 0 1.53-.09 2.25-.26.21.71.33 1.47.33 2.26 0 4.41-3.59 8-8 8z"></path></g>
<g id="favorite"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></g>
<g id="favorite-border"><path d="M16.5 3c-1.74 0-3.41.81-4.5 2.09C10.91 3.81 9.24 3 7.5 3 4.42 3 2 5.42 2 8.5c0 3.78 3.4 6.86 8.55 11.54L12 21.35l1.45-1.32C18.6 15.36 22 12.28 22 8.5 22 5.42 19.58 3 16.5 3zm-4.4 15.55l-.1.1-.1-.1C7.14 14.24 4 11.39 4 8.5 4 6.5 5.5 5 7.5 5c1.54 0 3.04.99 3.57 2.36h1.87C13.46 5.99 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5 0 2.89-3.14 5.74-7.9 10.05z"></path></g>
<g id="feedback"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-7 12h-2v-2h2v2zm0-4h-2V6h2v4z"></path></g>
<g id="file-download"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"></path></g>
<g id="file-upload"><path d="M9 16h6v-6h4l-7-7-7 7h4zm-4 2h14v2H5z"></path></g>
<g id="filter-list"><path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"></path></g>
<g id="find-in-page"><path d="M20 19.59V8l-6-6H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c.45 0 .85-.15 1.19-.4l-4.43-4.43c-.8.52-1.74.83-2.76.83-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5c0 1.02-.31 1.96-.83 2.75L20 19.59zM9 13c0 1.66 1.34 3 3 3s3-1.34 3-3-1.34-3-3-3-3 1.34-3 3z"></path></g>
<g id="find-replace"><path d="M11 6c1.38 0 2.63.56 3.54 1.46L12 10h6V4l-2.05 2.05C14.68 4.78 12.93 4 11 4c-3.53 0-6.43 2.61-6.92 6H6.1c.46-2.28 2.48-4 4.9-4zm5.64 9.14c.66-.9 1.12-1.97 1.28-3.14H15.9c-.46 2.28-2.48 4-4.9 4-1.38 0-2.63-.56-3.54-1.46L10 12H4v6l2.05-2.05C7.32 17.22 9.07 18 11 18c1.55 0 2.98-.51 4.14-1.36L20 21.49 21.49 20l-4.85-4.86z"></path></g>
<g id="fingerprint"><path d="M17.81 4.47c-.08 0-.16-.02-.23-.06C15.66 3.42 14 3 12.01 3c-1.98 0-3.86.47-5.57 1.41-.24.13-.54.04-.68-.2-.13-.24-.04-.55.2-.68C7.82 2.52 9.86 2 12.01 2c2.13 0 3.99.47 6.03 1.52.25.13.34.43.21.67-.09.18-.26.28-.44.28zM3.5 9.72c-.1 0-.2-.03-.29-.09-.23-.16-.28-.47-.12-.7.99-1.4 2.25-2.5 3.75-3.27C9.98 4.04 14 4.03 17.15 5.65c1.5.77 2.76 1.86 3.75 3.25.16.22.11.54-.12.7-.23.16-.54.11-.7-.12-.9-1.26-2.04-2.25-3.39-2.94-2.87-1.47-6.54-1.47-9.4.01-1.36.7-2.5 1.7-3.4 2.96-.08.14-.23.21-.39.21zm6.25 12.07c-.13 0-.26-.05-.35-.15-.87-.87-1.34-1.43-2.01-2.64-.69-1.23-1.05-2.73-1.05-4.34 0-2.97 2.54-5.39 5.66-5.39s5.66 2.42 5.66 5.39c0 .28-.22.5-.5.5s-.5-.22-.5-.5c0-2.42-2.09-4.39-4.66-4.39-2.57 0-4.66 1.97-4.66 4.39 0 1.44.32 2.77.93 3.85.64 1.15 1.08 1.64 1.85 2.42.19.2.19.51 0 .71-.11.1-.24.15-.37.15zm7.17-1.85c-1.19 0-2.24-.3-3.1-.89-1.49-1.01-2.38-2.65-2.38-4.39 0-.28.22-.5.5-.5s.5.22.5.5c0 1.41.72 2.74 1.94 3.56.71.48 1.54.71 2.54.71.24 0 .64-.03 1.04-.1.27-.05.53.13.58.41.05.27-.13.53-.41.58-.57.11-1.07.12-1.21.12zM14.91 22c-.04 0-.09-.01-.13-.02-1.59-.44-2.63-1.03-3.72-2.1-1.4-1.39-2.17-3.24-2.17-5.22 0-1.62 1.38-2.94 3.08-2.94 1.7 0 3.08 1.32 3.08 2.94 0 1.07.93 1.94 2.08 1.94s2.08-.87 2.08-1.94c0-3.77-3.25-6.83-7.25-6.83-2.84 0-5.44 1.58-6.61 4.03-.39.81-.59 1.76-.59 2.8 0 .78.07 2.01.67 3.61.1.26-.03.55-.29.64-.26.1-.55-.04-.64-.29-.49-1.31-.73-2.61-.73-3.96 0-1.2.23-2.29.68-3.24 1.33-2.79 4.28-4.6 7.51-4.6 4.55 0 8.25 3.51 8.25 7.83 0 1.62-1.38 2.94-3.08 2.94s-3.08-1.32-3.08-2.94c0-1.07-.93-1.94-2.08-1.94s-2.08.87-2.08 1.94c0 1.71.66 3.31 1.87 4.51.95.94 1.86 1.46 3.27 1.85.27.07.42.35.35.61-.05.23-.26.38-.47.38z"></path></g>
<g id="first-page"><path d="M18.41 16.59L13.82 12l4.59-4.59L17 6l-6 6 6 6zM6 6h2v12H6z"></path></g>
<g id="flag"><path d="M14.4 6L14 4H5v17h2v-7h5.6l.4 2h7V6z"></path></g>
<g id="flight-land"><path d="M2.5 19h19v2h-19zm7.18-5.73l4.35 1.16 5.31 1.42c.8.21 1.62-.26 1.84-1.06.21-.8-.26-1.62-1.06-1.84l-5.31-1.42-2.76-9.02L10.12 2v8.28L5.15 8.95l-.93-2.32-1.45-.39v5.17l1.6.43 5.31 1.43z"></path></g>
<g id="flight-takeoff"><path d="M2.5 19h19v2h-19zm19.57-9.36c-.21-.8-1.04-1.28-1.84-1.06L14.92 10l-6.9-6.43-1.93.51 4.14 7.17-4.97 1.33-1.97-1.54-1.45.39 1.82 3.16.77 1.33 1.6-.43 5.31-1.42 4.35-1.16L21 11.49c.81-.23 1.28-1.05 1.07-1.85z"></path></g>
<g id="flip-to-back"><path d="M9 7H7v2h2V7zm0 4H7v2h2v-2zm0-8c-1.11 0-2 .9-2 2h2V3zm4 12h-2v2h2v-2zm6-12v2h2c0-1.1-.9-2-2-2zm-6 0h-2v2h2V3zM9 17v-2H7c0 1.1.89 2 2 2zm10-4h2v-2h-2v2zm0-4h2V7h-2v2zm0 8c1.1 0 2-.9 2-2h-2v2zM5 7H3v12c0 1.1.89 2 2 2h12v-2H5V7zm10-2h2V3h-2v2zm0 12h2v-2h-2v2z"></path></g>
<g id="flip-to-front"><path d="M3 13h2v-2H3v2zm0 4h2v-2H3v2zm2 4v-2H3c0 1.1.89 2 2 2zM3 9h2V7H3v2zm12 12h2v-2h-2v2zm4-18H9c-1.11 0-2 .9-2 2v10c0 1.1.89 2 2 2h10c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 12H9V5h10v10zm-8 6h2v-2h-2v2zm-4 0h2v-2H7v2z"></path></g>
<g id="folder"><path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"></path></g>
<g id="folder-open"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z"></path></g>
<g id="folder-shared"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-5 3c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm4 8h-8v-1c0-1.33 2.67-2 4-2s4 .67 4 2v1z"></path></g>
<g id="font-download"><path d="M9.93 13.5h4.14L12 7.98zM20 2H4c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-4.05 16.5l-1.14-3H9.17l-1.12 3H5.96l5.11-13h1.86l5.11 13h-2.09z"></path></g>
<g id="forward"><path d="M12 8V4l8 8-8 8v-4H4V8z"></path></g>
<g id="fullscreen"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"></path></g>
<g id="fullscreen-exit"><path d="M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z"></path></g>
<g id="g-translate"><path d="M20 5h-9.12L10 2H4c-1.1 0-2 .9-2 2v13c0 1.1.9 2 2 2h7l1 3h8c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zM7.17 14.59c-2.25 0-4.09-1.83-4.09-4.09s1.83-4.09 4.09-4.09c1.04 0 1.99.37 2.74 1.07l.07.06-1.23 1.18-.06-.05c-.29-.27-.78-.59-1.52-.59-1.31 0-2.38 1.09-2.38 2.42s1.07 2.42 2.38 2.42c1.37 0 1.96-.87 2.12-1.46H7.08V9.91h3.95l.01.07c.04.21.05.4.05.61 0 2.35-1.61 4-3.92 4zm6.03-1.71c.33.6.74 1.18 1.19 1.7l-.54.53-.65-2.23zm.77-.76h-.99l-.31-1.04h3.99s-.34 1.31-1.56 2.74c-.52-.62-.89-1.23-1.13-1.7zM21 20c0 .55-.45 1-1 1h-7l2-2-.81-2.77.92-.92L17.79 18l.73-.73-2.71-2.68c.9-1.03 1.6-2.25 1.92-3.51H19v-1.04h-3.64V9h-1.04v1.04h-1.96L11.18 6H20c.55 0 1 .45 1 1v13z"></path></g>
<g id="gavel"><path d="M1 21h12v2H1zM5.245 8.07l2.83-2.827 14.14 14.142-2.828 2.828zM12.317 1l5.657 5.656-2.83 2.83-5.654-5.66zM3.825 9.485l5.657 5.657-2.828 2.828-5.657-5.657z"></path></g>
<g id="gesture"><path d="M4.59 6.89c.7-.71 1.4-1.35 1.71-1.22.5.2 0 1.03-.3 1.52-.25.42-2.86 3.89-2.86 6.31 0 1.28.48 2.34 1.34 2.98.75.56 1.74.73 2.64.46 1.07-.31 1.95-1.4 3.06-2.77 1.21-1.49 2.83-3.44 4.08-3.44 1.63 0 1.65 1.01 1.76 1.79-3.78.64-5.38 3.67-5.38 5.37 0 1.7 1.44 3.09 3.21 3.09 1.63 0 4.29-1.33 4.69-6.1H21v-2.5h-2.47c-.15-1.65-1.09-4.2-4.03-4.2-2.25 0-4.18 1.91-4.94 2.84-.58.73-2.06 2.48-2.29 2.72-.25.3-.68.84-1.11.84-.45 0-.72-.83-.36-1.92.35-1.09 1.4-2.86 1.85-3.52.78-1.14 1.3-1.92 1.3-3.28C8.95 3.69 7.31 3 6.44 3 5.12 3 3.97 4 3.72 4.25c-.36.36-.66.66-.88.93l1.75 1.71zm9.29 11.66c-.31 0-.74-.26-.74-.72 0-.6.73-2.2 2.87-2.76-.3 2.69-1.43 3.48-2.13 3.48z"></path></g>
<g id="get-app"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"></path></g>
<g id="gif"><path d="M11.5 9H13v6h-1.5zM9 9H6c-.6 0-1 .5-1 1v4c0 .5.4 1 1 1h3c.6 0 1-.5 1-1v-2H8.5v1.5h-2v-3H10V10c0-.5-.4-1-1-1zm10 1.5V9h-4.5v6H16v-2h2v-1.5h-2v-1z"></path></g>
<g id="grade"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path></g>
<g id="group-work"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zM8 17.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5zM9.5 8c0-1.38 1.12-2.5 2.5-2.5s2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5S9.5 9.38 9.5 8zm6.5 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"></path></g>
<g id="help"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"></path></g>
<g id="help-outline"><path d="M11 18h2v-2h-2v2zm1-16C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-2.21 0-4 1.79-4 4h2c0-1.1.9-2 2-2s2 .9 2 2c0 2-3 1.75-3 5h2c0-2.25 3-2.5 3-5 0-2.21-1.79-4-4-4z"></path></g>
<g id="highlight-off"><path d="M14.59 8L12 10.59 9.41 8 8 9.41 10.59 12 8 14.59 9.41 16 12 13.41 14.59 16 16 14.59 13.41 12 16 9.41 14.59 8zM12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></g>
<g id="history"><path d="M13 3c-4.97 0-9 4.03-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42C8.27 19.99 10.51 21 13 21c4.97 0 9-4.03 9-9s-4.03-9-9-9zm-1 5v5l4.28 2.54.72-1.21-3.5-2.08V8H12z"></path></g>
<g id="home"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"></path></g>
<g id="hourglass-empty"><path d="M6 2v6h.01L6 8.01 10 12l-4 4 .01.01H6V22h12v-5.99h-.01L18 16l-4-4 4-3.99-.01-.01H18V2H6zm10 14.5V20H8v-3.5l4-4 4 4zm-4-5l-4-4V4h8v3.5l-4 4z"></path></g>
<g id="hourglass-full"><path d="M6 2v6h.01L6 8.01 10 12l-4 4 .01.01H6V22h12v-5.99h-.01L18 16l-4-4 4-3.99-.01-.01H18V2H6z"></path></g>
<g id="http"><path d="M4.5 11h-2V9H1v6h1.5v-2.5h2V15H6V9H4.5v2zm2.5-.5h1.5V15H10v-4.5h1.5V9H7v1.5zm5.5 0H14V15h1.5v-4.5H17V9h-4.5v1.5zm9-1.5H18v6h1.5v-2h2c.8 0 1.5-.7 1.5-1.5v-1c0-.8-.7-1.5-1.5-1.5zm0 2.5h-2v-1h2v1z"></path></g>
<g id="https"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"></path></g>
<g id="important-devices"><path d="M23 11.01L18 11c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5c.55 0 1-.45 1-1v-9c0-.55-.45-.99-1-.99zM23 20h-5v-7h5v7zM20 2H2C.89 2 0 2.89 0 4v12c0 1.1.89 2 2 2h7v2H7v2h8v-2h-2v-2h2v-2H2V4h18v5h2V4c0-1.11-.9-2-2-2zm-8.03 7L11 6l-.97 3H7l2.47 1.76-.94 2.91 2.47-1.8 2.47 1.8-.94-2.91L15 9h-3.03z"></path></g>
<g id="inbox"><path d="M19 3H4.99c-1.11 0-1.98.89-1.98 2L3 19c0 1.1.88 2 1.99 2H19c1.1 0 2-.9 2-2V5c0-1.11-.9-2-2-2zm0 12h-4c0 1.66-1.35 3-3 3s-3-1.34-3-3H4.99V5H19v10z"></path></g>
<g id="indeterminate-check-box"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10H7v-2h10v2z"></path></g>
<g id="info"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"></path></g>
<g id="info-outline"><path d="M11 17h2v-6h-2v6zm1-15C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM11 9h2V7h-2v2z"></path></g>
<g id="input"><path d="M21 3.01H3c-1.1 0-2 .9-2 2V9h2V4.99h18v14.03H3V15H1v4.01c0 1.1.9 1.98 2 1.98h18c1.1 0 2-.88 2-1.98v-14c0-1.11-.9-2-2-2zM11 16l4-4-4-4v3H1v2h10v3z"></path></g>
<g id="invert-colors"><path d="M17.66 7.93L12 2.27 6.34 7.93c-3.12 3.12-3.12 8.19 0 11.31C7.9 20.8 9.95 21.58 12 21.58c2.05 0 4.1-.78 5.66-2.34 3.12-3.12 3.12-8.19 0-11.31zM12 19.59c-1.6 0-3.11-.62-4.24-1.76C6.62 16.69 6 15.19 6 13.59s.62-3.11 1.76-4.24L12 5.1v14.49z"></path></g>
<g id="label"><path d="M17.63 5.84C17.27 5.33 16.67 5 16 5L5 5.01C3.9 5.01 3 5.9 3 7v10c0 1.1.9 1.99 2 1.99L16 19c.67 0 1.27-.33 1.63-.84L22 12l-4.37-6.16z"></path></g>
<g id="label-outline"><path d="M17.63 5.84C17.27 5.33 16.67 5 16 5L5 5.01C3.9 5.01 3 5.9 3 7v10c0 1.1.9 1.99 2 1.99L16 19c.67 0 1.27-.33 1.63-.84L22 12l-4.37-6.16zM16 17H5V7h11l3.55 5L16 17z"></path></g>
<g id="language"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95c-.32-1.25-.78-2.45-1.38-3.56 1.84.63 3.37 1.91 4.33 3.56zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56-1.84-.63-3.37-1.9-4.33-3.56zm2.95-8H5.08c.96-1.66 2.49-2.93 4.33-3.56C8.81 5.55 8.35 6.75 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.66-.16-1.32-.16-2 0-.68.07-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.34-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95c-.96 1.65-2.49 2.93-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z"></path></g>
<g id="last-page"><path d="M5.59 7.41L10.18 12l-4.59 4.59L7 18l6-6-6-6zM16 6h2v12h-2z"></path></g>
<g id="launch"><path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"></path></g>
<g id="lightbulb-outline"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6C7.8 12.16 7 10.63 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"></path></g>
<g id="line-style"><path d="M3 16h5v-2H3v2zm6.5 0h5v-2h-5v2zm6.5 0h5v-2h-5v2zM3 20h2v-2H3v2zm4 0h2v-2H7v2zm4 0h2v-2h-2v2zm4 0h2v-2h-2v2zm4 0h2v-2h-2v2zM3 12h8v-2H3v2zm10 0h8v-2h-8v2zM3 4v4h18V4H3z"></path></g>
<g id="line-weight"><path d="M3 17h18v-2H3v2zm0 3h18v-1H3v1zm0-7h18v-3H3v3zm0-9v4h18V4H3z"></path></g>
<g id="link"><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></g>
<g id="list"><path d="M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 4h14v-2H7v2zm0 4h14v-2H7v2zM7 7v2h14V7H7z"></path></g>
<g id="lock"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"></path></g>
<g id="lock-open"><path d="M12 17c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm6-9h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6h1.9c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm0 12H6V10h12v10z"></path></g>
<g id="lock-outline"><path d="M12 17c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm6-9h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zM8.9 6c0-1.71 1.39-3.1 3.1-3.1s3.1 1.39 3.1 3.1v2H8.9V6zM18 20H6V10h12v10z"></path></g>
<g id="low-priority"><path d="M14 5h8v2h-8zm0 5.5h8v2h-8zm0 5.5h8v2h-8zM2 11.5C2 15.08 4.92 18 8.5 18H9v2l3-3-3-3v2h-.5C6.02 16 4 13.98 4 11.5S6.02 7 8.5 7H12V5H8.5C4.92 5 2 7.92 2 11.5z"></path></g>
<g id="loyalty"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7zm11.77 8.27L13 19.54l-4.27-4.27C8.28 14.81 8 14.19 8 13.5c0-1.38 1.12-2.5 2.5-2.5.69 0 1.32.28 1.77.74l.73.72.73-.73c.45-.45 1.08-.73 1.77-.73 1.38 0 2.5 1.12 2.5 2.5 0 .69-.28 1.32-.73 1.77z"></path></g>
<g id="mail"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"></path></g>
<g id="markunread"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"></path></g>
<g id="markunread-mailbox"><path d="M20 6H10v6H8V4h6V0H6v6H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2z"></path></g>
<g id="menu"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></g>
<g id="more-horiz"><path d="M6 10c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm12 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-6 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g>
<g id="more-vert"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g>
<g id="motorcycle"><path d="M19.44 9.03L15.41 5H11v2h3.59l2 2H5c-2.8 0-5 2.2-5 5s2.2 5 5 5c2.46 0 4.45-1.69 4.9-4h1.65l2.77-2.77c-.21.54-.32 1.14-.32 1.77 0 2.8 2.2 5 5 5s5-2.2 5-5c0-2.65-1.97-4.77-4.56-4.97zM7.82 15C7.4 16.15 6.28 17 5 17c-1.63 0-3-1.37-3-3s1.37-3 3-3c1.28 0 2.4.85 2.82 2H5v2h2.82zM19 17c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"></path></g>
<g id="move-to-inbox"><path d="M19 3H4.99c-1.11 0-1.98.9-1.98 2L3 19c0 1.1.88 2 1.99 2H19c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 12h-4c0 1.66-1.35 3-3 3s-3-1.34-3-3H4.99V5H19v10zm-3-5h-2V7h-4v3H8l4 4 4-4z"></path></g>
<g id="next-week"><path d="M20 7h-4V5c0-.55-.22-1.05-.59-1.41C15.05 3.22 14.55 3 14 3h-4c-1.1 0-2 .9-2 2v2H4c-1.1 0-2 .9-2 2v11c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2zM10 5h4v2h-4V5zm1 13.5l-1-1 3-3-3-3 1-1 4 4-4 4z"></path></g>
<g id="note-add"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 14h-3v3h-2v-3H8v-2h3v-3h2v3h3v2zm-3-7V3.5L18.5 9H13z"></path></g>
<g id="offline-pin"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm5 16H7v-2h10v2zm-6.7-4L7 10.7l1.4-1.4 1.9 1.9 5.3-5.3L17 7.3 10.3 14z"></path></g>
<g id="opacity"><path d="M17.66 8L12 2.35 6.34 8C4.78 9.56 4 11.64 4 13.64s.78 4.11 2.34 5.67 3.61 2.35 5.66 2.35 4.1-.79 5.66-2.35S20 15.64 20 13.64 19.22 9.56 17.66 8zM6 14c.01-2 .62-3.27 1.76-4.4L12 5.27l4.24 4.38C17.38 10.77 17.99 12 18 14H6z"></path></g>
<g id="open-in-browser"><path d="M19 4H5c-1.11 0-2 .9-2 2v12c0 1.1.89 2 2 2h4v-2H5V8h14v10h-4v2h4c1.1 0 2-.9 2-2V6c0-1.1-.89-2-2-2zm-7 6l-4 4h3v6h2v-6h3l-4-4z"></path></g>
<g id="open-in-new"><path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"></path></g>
<g id="open-with"><path d="M10 9h4V6h3l-5-5-5 5h3v3zm-1 1H6V7l-5 5 5 5v-3h3v-4zm14 2l-5-5v3h-3v4h3v3l5-5zm-9 3h-4v3H7l5 5 5-5h-3v-3z"></path></g>
<g id="pageview"><path d="M11.5 9C10.12 9 9 10.12 9 11.5s1.12 2.5 2.5 2.5 2.5-1.12 2.5-2.5S12.88 9 11.5 9zM20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-3.21 14.21l-2.91-2.91c-.69.44-1.51.7-2.39.7C9.01 16 7 13.99 7 11.5S9.01 7 11.5 7 16 9.01 16 11.5c0 .88-.26 1.69-.7 2.39l2.91 2.9-1.42 1.42z"></path></g>
<g id="pan-tool"><path d="M23 5.5V20c0 2.2-1.8 4-4 4h-7.3c-1.08 0-2.1-.43-2.85-1.19L1 14.83s1.26-1.23 1.3-1.25c.22-.19.49-.29.79-.29.22 0 .42.06.6.16.04.01 4.31 2.46 4.31 2.46V4c0-.83.67-1.5 1.5-1.5S11 3.17 11 4v7h1V1.5c0-.83.67-1.5 1.5-1.5S15 .67 15 1.5V11h1V2.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5V11h1V5.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5z"></path></g>
<g id="payment"><path d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"></path></g>
<g id="perm-camera-mic"><path d="M20 5h-3.17L15 3H9L7.17 5H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h7v-2.09c-2.83-.48-5-2.94-5-5.91h2c0 2.21 1.79 4 4 4s4-1.79 4-4h2c0 2.97-2.17 5.43-5 5.91V21h7c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm-6 8c0 1.1-.9 2-2 2s-2-.9-2-2V9c0-1.1.9-2 2-2s2 .9 2 2v4z"></path></g>
<g id="perm-contact-calendar"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6 12H6v-1c0-2 4-3.1 6-3.1s6 1.1 6 3.1v1z"></path></g>
<g id="perm-data-setting"><path d="M18.99 11.5c.34 0 .67.03 1 .07L20 0 0 20h11.56c-.04-.33-.07-.66-.07-1 0-4.14 3.36-7.5 7.5-7.5zm3.71 7.99c.02-.16.04-.32.04-.49 0-.17-.01-.33-.04-.49l1.06-.83c.09-.08.12-.21.06-.32l-1-1.73c-.06-.11-.19-.15-.31-.11l-1.24.5c-.26-.2-.54-.37-.85-.49l-.19-1.32c-.01-.12-.12-.21-.24-.21h-2c-.12 0-.23.09-.25.21l-.19 1.32c-.3.13-.59.29-.85.49l-1.24-.5c-.11-.04-.24 0-.31.11l-1 1.73c-.06.11-.04.24.06.32l1.06.83c-.02.16-.03.32-.03.49 0 .17.01.33.03.49l-1.06.83c-.09.08-.12.21-.06.32l1 1.73c.06.11.19.15.31.11l1.24-.5c.26.2.54.37.85.49l.19 1.32c.02.12.12.21.25.21h2c.12 0 .23-.09.25-.21l.19-1.32c.3-.13.59-.29.84-.49l1.25.5c.11.04.24 0 .31-.11l1-1.73c.06-.11.03-.24-.06-.32l-1.07-.83zm-3.71 1.01c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"></path></g>
<g id="perm-device-information"><path d="M13 7h-2v2h2V7zm0 4h-2v6h2v-6zm4-9.99L7 1c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V3c0-1.1-.9-1.99-2-1.99zM17 19H7V5h10v14z"></path></g>
<g id="perm-identity"><path d="M12 5.9c1.16 0 2.1.94 2.1 2.1s-.94 2.1-2.1 2.1S9.9 9.16 9.9 8s.94-2.1 2.1-2.1m0 9c2.97 0 6.1 1.46 6.1 2.1v1.1H5.9V17c0-.64 3.13-2.1 6.1-2.1M12 4C9.79 4 8 5.79 8 8s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm0 9c-2.67 0-8 1.34-8 4v3h16v-3c0-2.66-5.33-4-8-4z"></path></g>
<g id="perm-media"><path d="M2 6H0v5h.01L0 20c0 1.1.9 2 2 2h18v-2H2V6zm20-2h-8l-2-2H6c-1.1 0-1.99.9-1.99 2L4 16c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zM7 15l4.5-6 3.5 4.51 2.5-3.01L21 15H7z"></path></g>
<g id="perm-phone-msg"><path d="M20 15.5c-1.25 0-2.45-.2-3.57-.57-.35-.11-.74-.03-1.02.24l-2.2 2.2c-2.83-1.44-5.15-3.75-6.59-6.58l2.2-2.21c.28-.27.36-.66.25-1.01C8.7 6.45 8.5 5.25 8.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1zM12 3v10l3-3h6V3h-9z"></path></g>
<g id="perm-scan-wifi"><path d="M12 3C6.95 3 3.15 4.85 0 7.23L12 22 24 7.25C20.85 4.87 17.05 3 12 3zm1 13h-2v-6h2v6zm-2-8V6h2v2h-2z"></path></g>
<g id="pets"><circle cx="4.5" cy="9.5" r="2.5"></circle><circle cx="9" cy="5.5" r="2.5"></circle><circle cx="15" cy="5.5" r="2.5"></circle><circle cx="19.5" cy="9.5" r="2.5"></circle><path d="M17.34 14.86c-.87-1.02-1.6-1.89-2.48-2.91-.46-.54-1.05-1.08-1.75-1.32-.11-.04-.22-.07-.33-.09-.25-.04-.52-.04-.78-.04s-.53 0-.79.05c-.11.02-.22.05-.33.09-.7.24-1.28.78-1.75 1.32-.87 1.02-1.6 1.89-2.48 2.91-1.31 1.31-2.92 2.76-2.62 4.79.29 1.02 1.02 2.03 2.33 2.32.73.15 3.06-.44 5.54-.44h.18c2.48 0 4.81.58 5.54.44 1.31-.29 2.04-1.31 2.33-2.32.31-2.04-1.3-3.49-2.61-4.8z"></path></g>
<g id="picture-in-picture"><path d="M19 7h-8v6h8V7zm2-4H3c-1.1 0-2 .9-2 2v14c0 1.1.9 1.98 2 1.98h18c1.1 0 2-.88 2-1.98V5c0-1.1-.9-2-2-2zm0 16.01H3V4.98h18v14.03z"></path></g>
<g id="picture-in-picture-alt"><path d="M19 11h-8v6h8v-6zm4 8V4.98C23 3.88 22.1 3 21 3H3c-1.1 0-2 .88-2 1.98V19c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2zm-2 .02H3V4.97h18v14.05z"></path></g>
<g id="play-for-work"><path d="M11 5v5.59H7.5l4.5 4.5 4.5-4.5H13V5h-2zm-5 9c0 3.31 2.69 6 6 6s6-2.69 6-6h-2c0 2.21-1.79 4-4 4s-4-1.79-4-4H6z"></path></g>
<g id="polymer"><path d="M19 4h-4L7.11 16.63 4.5 12 9 4H5L.5 12 5 20h4l7.89-12.63L19.5 12 15 20h4l4.5-8z"></path></g>
<g id="power-settings-new"><path d="M13 3h-2v10h2V3zm4.83 2.17l-1.42 1.42C17.99 7.86 19 9.81 19 12c0 3.87-3.13 7-7 7s-7-3.13-7-7c0-2.19 1.01-4.14 2.58-5.42L6.17 5.17C4.23 6.82 3 9.26 3 12c0 4.97 4.03 9 9 9s9-4.03 9-9c0-2.74-1.23-5.18-3.17-6.83z"></path></g>
<g id="pregnant-woman"><path d="M9 4c0-1.11.89-2 2-2s2 .89 2 2-.89 2-2 2-2-.89-2-2zm7 9c-.01-1.34-.83-2.51-2-3 0-1.66-1.34-3-3-3s-3 1.34-3 3v7h2v5h3v-5h3v-4z"></path></g>
<g id="print"><path d="M19 8H5c-1.66 0-3 1.34-3 3v6h4v4h12v-4h4v-6c0-1.66-1.34-3-3-3zm-3 11H8v-5h8v5zm3-7c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm-1-9H6v4h12V3z"></path></g>
<g id="query-builder"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"></path></g>
<g id="question-answer"><path d="M21 6h-2v9H6v2c0 .55.45 1 1 1h11l4 4V7c0-.55-.45-1-1-1zm-4 6V3c0-.55-.45-1-1-1H3c-.55 0-1 .45-1 1v14l4-4h10c.55 0 1-.45 1-1z"></path></g>
<g id="radio-button-checked"><path d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zm0-5C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"></path></g>
<g id="radio-button-unchecked"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"></path></g>
<g id="receipt"><path d="M18 17H6v-2h12v2zm0-4H6v-2h12v2zm0-4H6V7h12v2zM3 22l1.5-1.5L6 22l1.5-1.5L9 22l1.5-1.5L12 22l1.5-1.5L15 22l1.5-1.5L18 22l1.5-1.5L21 22V2l-1.5 1.5L18 2l-1.5 1.5L15 2l-1.5 1.5L12 2l-1.5 1.5L9 2 7.5 3.5 6 2 4.5 3.5 3 2v20z"></path></g>
<g id="record-voice-over"><circle cx="9" cy="9" r="4"></circle><path d="M9 15c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4zm7.76-9.64l-1.68 1.69c.84 1.18.84 2.71 0 3.89l1.68 1.69c2.02-2.02 2.02-5.07 0-7.27zM20.07 2l-1.63 1.63c2.77 3.02 2.77 7.56 0 10.74L20.07 16c3.9-3.89 3.91-9.95 0-14z"></path></g>
<g id="redeem"><path d="M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v6z"></path></g>
<g id="redo"><path d="M18.4 10.6C16.55 8.99 14.15 8 11.5 8c-4.65 0-8.58 3.03-9.96 7.22L3.9 16c1.05-3.19 4.05-5.5 7.6-5.5 1.95 0 3.73.72 5.12 1.88L13 16h9V7l-3.6 3.6z"></path></g>
<g id="refresh"><path d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"></path></g>
<g id="remove"><path d="M19 13H5v-2h14v2z"></path></g>
<g id="remove-circle"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11H7v-2h10v2z"></path></g>
<g id="remove-circle-outline"><path d="M7 11v2h10v-2H7zm5-9C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></g>
<g id="remove-shopping-cart"><path d="M22.73 22.73L2.77 2.77 2 2l-.73-.73L0 2.54l4.39 4.39 2.21 4.66-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h7.46l1.38 1.38c-.5.36-.83.95-.83 1.62 0 1.1.89 2 1.99 2 .67 0 1.26-.33 1.62-.84L21.46 24l1.27-1.27zM7.42 15c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h2.36l2 2H7.42zm8.13-2c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H6.54l9.01 9zM7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2z"></path></g>
<g id="reorder"><path d="M3 15h18v-2H3v2zm0 4h18v-2H3v2zm0-8h18V9H3v2zm0-6v2h18V5H3z"></path></g>
<g id="reply"><path d="M10 9V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z"></path></g>
<g id="reply-all"><path d="M7 8V5l-7 7 7 7v-3l-4-4 4-4zm6 1V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z"></path></g>
<g id="report"><path d="M15.73 3H8.27L3 8.27v7.46L8.27 21h7.46L21 15.73V8.27L15.73 3zM12 17.3c-.72 0-1.3-.58-1.3-1.3 0-.72.58-1.3 1.3-1.3.72 0 1.3.58 1.3 1.3 0 .72-.58 1.3-1.3 1.3zm1-4.3h-2V7h2v6z"></path></g>
<g id="report-problem"><path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"></path></g>
<g id="restore"><path d="M13 3c-4.97 0-9 4.03-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42C8.27 19.99 10.51 21 13 21c4.97 0 9-4.03 9-9s-4.03-9-9-9zm-1 5v5l4.28 2.54.72-1.21-3.5-2.08V8H12z"></path></g>
<g id="restore-page"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm-2 16c-2.05 0-3.81-1.24-4.58-3h1.71c.63.9 1.68 1.5 2.87 1.5 1.93 0 3.5-1.57 3.5-3.5S13.93 9.5 12 9.5c-1.35 0-2.52.78-3.1 1.9l1.6 1.6h-4V9l1.3 1.3C8.69 8.92 10.23 8 12 8c2.76 0 5 2.24 5 5s-2.24 5-5 5z"></path></g>
<g id="room"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"></path></g>
<g id="rounded-corner"><path d="M19 19h2v2h-2v-2zm0-2h2v-2h-2v2zM3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm0-4h2V3H3v2zm4 0h2V3H7v2zm8 16h2v-2h-2v2zm-4 0h2v-2h-2v2zm4 0h2v-2h-2v2zm-8 0h2v-2H7v2zm-4 0h2v-2H3v2zM21 8c0-2.76-2.24-5-5-5h-5v2h5c1.65 0 3 1.35 3 3v5h2V8z"></path></g>
<g id="rowing"><path d="M8.5 14.5L4 19l1.5 1.5L9 17h2l-2.5-2.5zM15 1c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm6 20.01L18 24l-2.99-3.01V19.5l-7.1-7.09c-.31.05-.61.07-.91.07v-2.16c1.66.03 3.61-.87 4.67-2.04l1.4-1.55c.19-.21.43-.38.69-.5.29-.14.62-.23.96-.23h.03C15.99 6.01 17 7.02 17 8.26v5.75c0 .84-.35 1.61-.92 2.16l-3.58-3.58v-2.27c-.63.52-1.43 1.02-2.29 1.39L16.5 18H18l3 3.01z"></path></g>
<g id="save"><path d="M17 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V7l-4-4zm-5 16c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm3-10H5V5h10v4z"></path></g>
<g id="schedule"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"></path></g>
<g id="search"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path></g>
<g id="select-all"><path d="M3 5h2V3c-1.1 0-2 .9-2 2zm0 8h2v-2H3v2zm4 8h2v-2H7v2zM3 9h2V7H3v2zm10-6h-2v2h2V3zm6 0v2h2c0-1.1-.9-2-2-2zM5 21v-2H3c0 1.1.9 2 2 2zm-2-4h2v-2H3v2zM9 3H7v2h2V3zm2 18h2v-2h-2v2zm8-8h2v-2h-2v2zm0 8c1.1 0 2-.9 2-2h-2v2zm0-12h2V7h-2v2zm0 8h2v-2h-2v2zm-4 4h2v-2h-2v2zm0-16h2V3h-2v2zM7 17h10V7H7v10zm2-8h6v6H9V9z"></path></g>
<g id="send"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"></path></g>
<g id="settings"><path d="M19.43 12.98c.04-.32.07-.64.07-.98s-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.12-.22-.39-.3-.61-.22l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65C14.46 2.18 14.25 2 14 2h-4c-.25 0-.46.18-.49.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.23-.09-.49 0-.61.22l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98s.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.12.22.39.3.61.22l2.49-1c.52.4 1.08.73 1.69.98l.38 2.65c.03.24.24.42.49.42h4c.25 0 .46-.18.49-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.23.09.49 0 .61-.22l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zM12 15.5c-1.93 0-3.5-1.57-3.5-3.5s1.57-3.5 3.5-3.5 3.5 1.57 3.5 3.5-1.57 3.5-3.5 3.5z"></path></g>
<g id="settings-applications"><path d="M12 10c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm7-7H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.11 0 2-.9 2-2V5c0-1.1-.89-2-2-2zm-1.75 9c0 .23-.02.46-.05.68l1.48 1.16c.13.11.17.3.08.45l-1.4 2.42c-.09.15-.27.21-.43.15l-1.74-.7c-.36.28-.76.51-1.18.69l-.26 1.85c-.03.17-.18.3-.35.3h-2.8c-.17 0-.32-.13-.35-.29l-.26-1.85c-.43-.18-.82-.41-1.18-.69l-1.74.7c-.16.06-.34 0-.43-.15l-1.4-2.42c-.09-.15-.05-.34.08-.45l1.48-1.16c-.03-.23-.05-.46-.05-.69 0-.23.02-.46.05-.68l-1.48-1.16c-.13-.11-.17-.3-.08-.45l1.4-2.42c.09-.15.27-.21.43-.15l1.74.7c.36-.28.76-.51 1.18-.69l.26-1.85c.03-.17.18-.3.35-.3h2.8c.17 0 .32.13.35.29l.26 1.85c.43.18.82.41 1.18.69l1.74-.7c.16-.06.34 0 .43.15l1.4 2.42c.09.15.05.34-.08.45l-1.48 1.16c.03.23.05.46.05.69z"></path></g>
<g id="settings-backup-restore"><path d="M14 12c0-1.1-.9-2-2-2s-2 .9-2 2 .9 2 2 2 2-.9 2-2zm-2-9c-4.97 0-9 4.03-9 9H0l4 4 4-4H5c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.51 0-2.91-.49-4.06-1.3l-1.42 1.44C8.04 20.3 9.94 21 12 21c4.97 0 9-4.03 9-9s-4.03-9-9-9z"></path></g>
<g id="settings-bluetooth"><path d="M11 24h2v-2h-2v2zm-4 0h2v-2H7v2zm8 0h2v-2h-2v2zm2.71-18.29L12 0h-1v7.59L6.41 3 5 4.41 10.59 10 5 15.59 6.41 17 11 12.41V20h1l5.71-5.71-4.3-4.29 4.3-4.29zM13 3.83l1.88 1.88L13 7.59V3.83zm1.88 10.46L13 16.17v-3.76l1.88 1.88z"></path></g>
<g id="settings-brightness"><path d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16.01H3V4.99h18v14.02zM8 16h2.5l1.5 1.5 1.5-1.5H16v-2.5l1.5-1.5-1.5-1.5V8h-2.5L12 6.5 10.5 8H8v2.5L6.5 12 8 13.5V16zm4-7c1.66 0 3 1.34 3 3s-1.34 3-3 3V9z"></path></g>
<g id="settings-cell"><path d="M7 24h2v-2H7v2zm4 0h2v-2h-2v2zm4 0h2v-2h-2v2zM16 .01L8 0C6.9 0 6 .9 6 2v16c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V2c0-1.1-.9-1.99-2-1.99zM16 16H8V4h8v12z"></path></g>
<g id="settings-ethernet"><path d="M7.77 6.76L6.23 5.48.82 12l5.41 6.52 1.54-1.28L3.42 12l4.35-5.24zM7 13h2v-2H7v2zm10-2h-2v2h2v-2zm-6 2h2v-2h-2v2zm6.77-7.52l-1.54 1.28L20.58 12l-4.35 5.24 1.54 1.28L23.18 12l-5.41-6.52z"></path></g>
<g id="settings-input-antenna"><path d="M12 5c-3.87 0-7 3.13-7 7h2c0-2.76 2.24-5 5-5s5 2.24 5 5h2c0-3.87-3.13-7-7-7zm1 9.29c.88-.39 1.5-1.26 1.5-2.29 0-1.38-1.12-2.5-2.5-2.5S9.5 10.62 9.5 12c0 1.02.62 1.9 1.5 2.29v3.3L7.59 21 9 22.41l3-3 3 3L16.41 21 13 17.59v-3.3zM12 1C5.93 1 1 5.93 1 12h2c0-4.97 4.03-9 9-9s9 4.03 9 9h2c0-6.07-4.93-11-11-11z"></path></g>
<g id="settings-input-component"><path d="M5 2c0-.55-.45-1-1-1s-1 .45-1 1v4H1v6h6V6H5V2zm4 14c0 1.3.84 2.4 2 2.82V23h2v-4.18c1.16-.41 2-1.51 2-2.82v-2H9v2zm-8 0c0 1.3.84 2.4 2 2.82V23h2v-4.18C6.16 18.4 7 17.3 7 16v-2H1v2zM21 6V2c0-.55-.45-1-1-1s-1 .45-1 1v4h-2v6h6V6h-2zm-8-4c0-.55-.45-1-1-1s-1 .45-1 1v4H9v6h6V6h-2V2zm4 14c0 1.3.84 2.4 2 2.82V23h2v-4.18c1.16-.41 2-1.51 2-2.82v-2h-6v2z"></path></g>
<g id="settings-input-composite"><path d="M5 2c0-.55-.45-1-1-1s-1 .45-1 1v4H1v6h6V6H5V2zm4 14c0 1.3.84 2.4 2 2.82V23h2v-4.18c1.16-.41 2-1.51 2-2.82v-2H9v2zm-8 0c0 1.3.84 2.4 2 2.82V23h2v-4.18C6.16 18.4 7 17.3 7 16v-2H1v2zM21 6V2c0-.55-.45-1-1-1s-1 .45-1 1v4h-2v6h6V6h-2zm-8-4c0-.55-.45-1-1-1s-1 .45-1 1v4H9v6h6V6h-2V2zm4 14c0 1.3.84 2.4 2 2.82V23h2v-4.18c1.16-.41 2-1.51 2-2.82v-2h-6v2z"></path></g>
<g id="settings-input-hdmi"><path d="M18 7V4c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v3H5v6l3 6v3h8v-3l3-6V7h-1zM8 4h8v3h-2V5h-1v2h-2V5h-1v2H8V4z"></path></g>
<g id="settings-input-svideo"><path d="M8 11.5c0-.83-.67-1.5-1.5-1.5S5 10.67 5 11.5 5.67 13 6.5 13 8 12.33 8 11.5zm7-5c0-.83-.67-1.5-1.5-1.5h-3C9.67 5 9 5.67 9 6.5S9.67 8 10.5 8h3c.83 0 1.5-.67 1.5-1.5zM8.5 15c-.83 0-1.5.67-1.5 1.5S7.67 18 8.5 18s1.5-.67 1.5-1.5S9.33 15 8.5 15zM12 1C5.93 1 1 5.93 1 12s4.93 11 11 11 11-4.93 11-11S18.07 1 12 1zm0 20c-4.96 0-9-4.04-9-9s4.04-9 9-9 9 4.04 9 9-4.04 9-9 9zm5.5-11c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm-2 5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5z"></path></g>
<g id="settings-overscan"><path d="M12.01 5.5L10 8h4l-1.99-2.5zM18 10v4l2.5-1.99L18 10zM6 10l-2.5 2.01L6 14v-4zm8 6h-4l2.01 2.5L14 16zm7-13H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16.01H3V4.99h18v14.02z"></path></g>
<g id="settings-phone"><path d="M13 9h-2v2h2V9zm4 0h-2v2h2V9zm3 6.5c-1.25 0-2.45-.2-3.57-.57-.35-.11-.74-.03-1.02.24l-2.2 2.2c-2.83-1.44-5.15-3.75-6.59-6.58l2.2-2.21c.28-.27.36-.66.25-1.01C8.7 6.45 8.5 5.25 8.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1zM19 9v2h2V9h-2z"></path></g>
<g id="settings-power"><path d="M7 24h2v-2H7v2zm4 0h2v-2h-2v2zm2-22h-2v10h2V2zm3.56 2.44l-1.45 1.45C16.84 6.94 18 8.83 18 11c0 3.31-2.69 6-6 6s-6-2.69-6-6c0-2.17 1.16-4.06 2.88-5.12L7.44 4.44C5.36 5.88 4 8.28 4 11c0 4.42 3.58 8 8 8s8-3.58 8-8c0-2.72-1.36-5.12-3.44-6.56zM15 24h2v-2h-2v2z"></path></g>
<g id="settings-remote"><path d="M15 9H9c-.55 0-1 .45-1 1v12c0 .55.45 1 1 1h6c.55 0 1-.45 1-1V10c0-.55-.45-1-1-1zm-3 6c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zM7.05 6.05l1.41 1.41C9.37 6.56 10.62 6 12 6s2.63.56 3.54 1.46l1.41-1.41C15.68 4.78 13.93 4 12 4s-3.68.78-4.95 2.05zM12 0C8.96 0 6.21 1.23 4.22 3.22l1.41 1.41C7.26 3.01 9.51 2 12 2s4.74 1.01 6.36 2.64l1.41-1.41C17.79 1.23 15.04 0 12 0z"></path></g>
<g id="settings-voice"><path d="M7 24h2v-2H7v2zm5-11c1.66 0 2.99-1.34 2.99-3L15 4c0-1.66-1.34-3-3-3S9 2.34 9 4v6c0 1.66 1.34 3 3 3zm-1 11h2v-2h-2v2zm4 0h2v-2h-2v2zm4-14h-1.7c0 3-2.54 5.1-5.3 5.1S6.7 13 6.7 10H5c0 3.41 2.72 6.23 6 6.72V20h2v-3.28c3.28-.49 6-3.31 6-6.72z"></path></g>
<g id="shop"><path d="M16 6V4c0-1.11-.89-2-2-2h-4c-1.11 0-2 .89-2 2v2H2v13c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6h-6zm-6-2h4v2h-4V4zM9 18V9l7.5 4L9 18z"></path></g>
<g id="shop-two"><path d="M3 9H1v11c0 1.11.89 2 2 2h14c1.11 0 2-.89 2-2H3V9zm15-4V3c0-1.11-.89-2-2-2h-4c-1.11 0-2 .89-2 2v2H5v11c0 1.11.89 2 2 2h14c1.11 0 2-.89 2-2V5h-5zm-6-2h4v2h-4V3zm0 12V8l5.5 3-5.5 4z"></path></g>
<g id="shopping-basket"><path d="M17.21 9l-4.38-6.56c-.19-.28-.51-.42-.83-.42-.32 0-.64.14-.83.43L6.79 9H2c-.55 0-1 .45-1 1 0 .09.01.18.04.27l2.54 9.27c.23.84 1 1.46 1.92 1.46h13c.92 0 1.69-.62 1.93-1.46l2.54-9.27L23 10c0-.55-.45-1-1-1h-4.79zM9 9l3-4.4L15 9H9zm3 8c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"></path></g>
<g id="shopping-cart"><path d="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"></path></g>
<g id="sort"><path d="M3 18h6v-2H3v2zM3 6v2h18V6H3zm0 7h12v-2H3v2z"></path></g>
<g id="speaker-notes"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM8 14H6v-2h2v2zm0-3H6V9h2v2zm0-3H6V6h2v2zm7 6h-5v-2h5v2zm3-3h-8V9h8v2zm0-3h-8V6h8v2z"></path></g>
<g id="speaker-notes-off"><path d="M10.54 11l-.54-.54L7.54 8 6 6.46 2.38 2.84 1.27 1.73 0 3l2.01 2.01L2 22l4-4h9l5.73 5.73L22 22.46 17.54 18l-7-7zM8 14H6v-2h2v2zm-2-3V9l2 2H6zm14-9H4.08L10 7.92V6h8v2h-7.92l1 1H18v2h-4.92l6.99 6.99C21.14 17.95 22 17.08 22 16V4c0-1.1-.9-2-2-2z"></path></g>
<g id="spellcheck"><path d="M12.45 16h2.09L9.43 3H7.57L2.46 16h2.09l1.12-3h5.64l1.14 3zm-6.02-5L8.5 5.48 10.57 11H6.43zm15.16.59l-8.09 8.09L9.83 16l-1.41 1.41 5.09 5.09L23 13l-1.41-1.41z"></path></g>
<g id="star"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path></g>
<g id="star-border"><path d="M22 9.24l-7.19-.62L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21 12 17.27 18.18 21l-1.63-7.03L22 9.24zM12 15.4l-3.76 2.27 1-4.28-3.32-2.88 4.38-.38L12 6.1l1.71 4.04 4.38.38-3.32 2.88 1 4.28L12 15.4z"></path></g>
<g id="star-half"><path d="M22 9.24l-7.19-.62L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21 12 17.27 18.18 21l-1.63-7.03L22 9.24zM12 15.4V6.1l1.71 4.04 4.38.38-3.32 2.88 1 4.28L12 15.4z"></path></g>
<g id="stars"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.45 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z"></path></g>
<g id="store"><path d="M20 4H4v2h16V4zm1 10v-2l-1-5H4l-1 5v2h1v6h10v-6h4v6h2v-6h1zm-9 4H6v-4h6v4z"></path></g>
<g id="subdirectory-arrow-left"><path d="M11 9l1.42 1.42L8.83 14H18V4h2v12H8.83l3.59 3.58L11 21l-6-6 6-6z"></path></g>
<g id="subdirectory-arrow-right"><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z"></path></g>
<g id="subject"><path d="M14 17H4v2h10v-2zm6-8H4v2h16V9zM4 15h16v-2H4v2zM4 5v2h16V5H4z"></path></g>
<g id="supervisor-account"><path d="M16.5 12c1.38 0 2.49-1.12 2.49-2.5S17.88 7 16.5 7C15.12 7 14 8.12 14 9.5s1.12 2.5 2.5 2.5zM9 11c1.66 0 2.99-1.34 2.99-3S10.66 5 9 5C7.34 5 6 6.34 6 8s1.34 3 3 3zm7.5 3c-1.83 0-5.5.92-5.5 2.75V19h11v-2.25c0-1.83-3.67-2.75-5.5-2.75zM9 13c-2.33 0-7 1.17-7 3.5V19h7v-2.25c0-.85.33-2.34 2.37-3.47C10.5 13.1 9.66 13 9 13z"></path></g>
<g id="swap-horiz"><path d="M6.99 11L3 15l3.99 4v-3H14v-2H6.99v-3zM21 9l-3.99-4v3H10v2h7.01v3L21 9z"></path></g>
<g id="swap-vert"><path d="M16 17.01V10h-2v7.01h-3L15 21l4-3.99h-3zM9 3L5 6.99h3V14h2V6.99h3L9 3z"></path></g>
<g id="swap-vertical-circle"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zM6.5 9L10 5.5 13.5 9H11v4H9V9H6.5zm11 6L14 18.5 10.5 15H13v-4h2v4h2.5z"></path></g>
<g id="system-update-alt"><path d="M12 16.5l4-4h-3v-9h-2v9H8l4 4zm9-13h-6v1.99h6v14.03H3V5.49h6V3.5H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2v-14c0-1.1-.9-2-2-2z"></path></g>
<g id="tab"><path d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H3V5h10v4h8v10z"></path></g>
<g id="tab-unselected"><path d="M1 9h2V7H1v2zm0 4h2v-2H1v2zm0-8h2V3c-1.1 0-2 .9-2 2zm8 16h2v-2H9v2zm-8-4h2v-2H1v2zm2 4v-2H1c0 1.1.9 2 2 2zM21 3h-8v6h10V5c0-1.1-.9-2-2-2zm0 14h2v-2h-2v2zM9 5h2V3H9v2zM5 21h2v-2H5v2zM5 5h2V3H5v2zm16 16c1.1 0 2-.9 2-2h-2v2zm0-8h2v-2h-2v2zm-8 8h2v-2h-2v2zm4 0h2v-2h-2v2z"></path></g>
<g id="text-format"><path d="M5 17v2h14v-2H5zm4.5-4.2h5l.9 2.2h2.1L12.75 4h-1.5L6.5 15h2.1l.9-2.2zM12 5.98L13.87 11h-3.74L12 5.98z"></path></g>
<g id="theaters"><path d="M18 3v2h-2V3H8v2H6V3H4v18h2v-2h2v2h8v-2h2v2h2V3h-2zM8 17H6v-2h2v2zm0-4H6v-2h2v2zm0-4H6V7h2v2zm10 8h-2v-2h2v2zm0-4h-2v-2h2v2zm0-4h-2V7h2v2z"></path></g>
<g id="thumb-down"><path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z"></path></g>
<g id="thumb-up"><path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z"></path></g>
<g id="thumbs-up-down"><path d="M12 6c0-.55-.45-1-1-1H5.82l.66-3.18.02-.23c0-.31-.13-.59-.33-.8L5.38 0 .44 4.94C.17 5.21 0 5.59 0 6v6.5c0 .83.67 1.5 1.5 1.5h6.75c.62 0 1.15-.38 1.38-.91l2.26-5.29c.07-.17.11-.36.11-.55V6zm10.5 4h-6.75c-.62 0-1.15.38-1.38.91l-2.26 5.29c-.07.17-.11.36-.11.55V18c0 .55.45 1 1 1h5.18l-.66 3.18-.02.24c0 .31.13.59.33.8l.79.78 4.94-4.94c.27-.27.44-.65.44-1.06v-6.5c0-.83-.67-1.5-1.5-1.5z"></path></g>
<g id="timeline"><path d="M23 8c0 1.1-.9 2-2 2-.18 0-.35-.02-.51-.07l-3.56 3.55c.05.16.07.34.07.52 0 1.1-.9 2-2 2s-2-.9-2-2c0-.18.02-.36.07-.52l-2.55-2.55c-.16.05-.34.07-.52.07s-.36-.02-.52-.07l-4.55 4.56c.05.16.07.33.07.51 0 1.1-.9 2-2 2s-2-.9-2-2 .9-2 2-2c.18 0 .35.02.51.07l4.56-4.55C8.02 9.36 8 9.18 8 9c0-1.1.9-2 2-2s2 .9 2 2c0 .18-.02.36-.07.52l2.55 2.55c.16-.05.34-.07.52-.07s.36.02.52.07l3.55-3.56C19.02 8.35 19 8.18 19 8c0-1.1.9-2 2-2s2 .9 2 2z"></path></g>
<g id="toc"><path d="M3 9h14V7H3v2zm0 4h14v-2H3v2zm0 4h14v-2H3v2zm16 0h2v-2h-2v2zm0-10v2h2V7h-2zm0 6h2v-2h-2v2z"></path></g>
<g id="today"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"></path></g>
<g id="toll"><path d="M15 4c-4.42 0-8 3.58-8 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm0 14c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6zM3 12c0-2.61 1.67-4.83 4-5.65V4.26C3.55 5.15 1 8.27 1 12s2.55 6.85 6 7.74v-2.09c-2.33-.82-4-3.04-4-5.65z"></path></g>
<g id="touch-app"><path d="M9 11.24V7.5C9 6.12 10.12 5 11.5 5S14 6.12 14 7.5v3.74c1.21-.81 2-2.18 2-3.74C16 5.01 13.99 3 11.5 3S7 5.01 7 7.5c0 1.56.79 2.93 2 3.74zm9.84 4.63l-4.54-2.26c-.17-.07-.35-.11-.54-.11H13v-6c0-.83-.67-1.5-1.5-1.5S10 6.67 10 7.5v10.74l-3.43-.72c-.08-.01-.15-.03-.24-.03-.31 0-.59.13-.79.33l-.79.8 4.94 4.94c.27.27.65.44 1.06.44h6.79c.75 0 1.33-.55 1.44-1.28l.75-5.27c.01-.07.02-.14.02-.2 0-.62-.38-1.16-.91-1.38z"></path></g>
<g id="track-changes"><path d="M19.07 4.93l-1.41 1.41C19.1 7.79 20 9.79 20 12c0 4.42-3.58 8-8 8s-8-3.58-8-8c0-4.08 3.05-7.44 7-7.93v2.02C8.16 6.57 6 9.03 6 12c0 3.31 2.69 6 6 6s6-2.69 6-6c0-1.66-.67-3.16-1.76-4.24l-1.41 1.41C15.55 9.9 16 10.9 16 12c0 2.21-1.79 4-4 4s-4-1.79-4-4c0-1.86 1.28-3.41 3-3.86v2.14c-.6.35-1 .98-1 1.72 0 1.1.9 2 2 2s2-.9 2-2c0-.74-.4-1.38-1-1.72V2h-1C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10c0-2.76-1.12-5.26-2.93-7.07z"></path></g>
<g id="translate"><path d="M12.87 15.07l-2.54-2.51.03-.03c1.74-1.94 2.98-4.17 3.71-6.53H17V4h-7V2H8v2H1v1.99h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12zm-2.62 7l1.62-4.33L19.12 17h-3.24z"></path></g>
<g id="trending-down"><path d="M16 18l2.29-2.29-4.88-4.88-4 4L2 7.41 3.41 6l6 6 4-4 6.3 6.29L22 12v6z"></path></g>
<g id="trending-flat"><path d="M22 12l-4-4v3H3v2h15v3z"></path></g>
<g id="trending-up"><path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"></path></g>
<g id="turned-in"><path d="M17 3H7c-1.1 0-1.99.9-1.99 2L5 21l7-3 7 3V5c0-1.1-.9-2-2-2z"></path></g>
<g id="turned-in-not"><path d="M17 3H7c-1.1 0-1.99.9-1.99 2L5 21l7-3 7 3V5c0-1.1-.9-2-2-2zm0 15l-5-2.18L7 18V5h10v13z"></path></g>
<g id="unarchive"><path d="M20.55 5.22l-1.39-1.68C18.88 3.21 18.47 3 18 3H6c-.47 0-.88.21-1.15.55L3.46 5.22C3.17 5.57 3 6.01 3 6.5V19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6.5c0-.49-.17-.93-.45-1.28zM12 9.5l5.5 5.5H14v2h-4v-2H6.5L12 9.5zM5.12 5l.82-1h12l.93 1H5.12z"></path></g>
<g id="undo"><path d="M12.5 8c-2.65 0-5.05.99-6.9 2.6L2 7v9h9l-3.62-3.62c1.39-1.16 3.16-1.88 5.12-1.88 3.54 0 6.55 2.31 7.6 5.5l2.37-.78C21.08 11.03 17.15 8 12.5 8z"></path></g>
<g id="unfold-less"><path d="M7.41 18.59L8.83 20 12 16.83 15.17 20l1.41-1.41L12 14l-4.59 4.59zm9.18-13.18L15.17 4 12 7.17 8.83 4 7.41 5.41 12 10l4.59-4.59z"></path></g>
<g id="unfold-more"><path d="M12 5.83L15.17 9l1.41-1.41L12 3 7.41 7.59 8.83 9 12 5.83zm0 12.34L8.83 15l-1.41 1.41L12 21l4.59-4.59L15.17 15 12 18.17z"></path></g>
<g id="update"><path d="M21 10.12h-6.78l2.74-2.82c-2.73-2.7-7.15-2.8-9.88-.1-2.73 2.71-2.73 7.08 0 9.79 2.73 2.71 7.15 2.71 9.88 0C18.32 15.65 19 14.08 19 12.1h2c0 1.98-.88 4.55-2.64 6.29-3.51 3.48-9.21 3.48-12.72 0-3.5-3.47-3.53-9.11-.02-12.58 3.51-3.47 9.14-3.47 12.65 0L21 3v7.12zM12.5 8v4.25l3.5 2.08-.72 1.21L11 13V8h1.5z"></path></g>
<g id="verified-user"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"></path></g>
<g id="view-agenda"><path d="M20 13H3c-.55 0-1 .45-1 1v6c0 .55.45 1 1 1h17c.55 0 1-.45 1-1v-6c0-.55-.45-1-1-1zm0-10H3c-.55 0-1 .45-1 1v6c0 .55.45 1 1 1h17c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1z"></path></g>
<g id="view-array"><path d="M4 18h3V5H4v13zM18 5v13h3V5h-3zM8 18h9V5H8v13z"></path></g>
<g id="view-carousel"><path d="M7 19h10V4H7v15zm-5-2h4V6H2v11zM18 6v11h4V6h-4z"></path></g>
<g id="view-column"><path d="M10 18h5V5h-5v13zm-6 0h5V5H4v13zM16 5v13h5V5h-5z"></path></g>
<g id="view-day"><path d="M2 21h19v-3H2v3zM20 8H3c-.55 0-1 .45-1 1v6c0 .55.45 1 1 1h17c.55 0 1-.45 1-1V9c0-.55-.45-1-1-1zM2 3v3h19V3H2z"></path></g>
<g id="view-headline"><path d="M4 15h16v-2H4v2zm0 4h16v-2H4v2zm0-8h16V9H4v2zm0-6v2h16V5H4z"></path></g>
<g id="view-list"><path d="M4 14h4v-4H4v4zm0 5h4v-4H4v4zM4 9h4V5H4v4zm5 5h12v-4H9v4zm0 5h12v-4H9v4zM9 5v4h12V5H9z"></path></g>
<g id="view-module"><path d="M4 11h5V5H4v6zm0 7h5v-6H4v6zm6 0h5v-6h-5v6zm6 0h5v-6h-5v6zm-6-7h5V5h-5v6zm6-6v6h5V5h-5z"></path></g>
<g id="view-quilt"><path d="M10 18h5v-6h-5v6zm-6 0h5V5H4v13zm12 0h5v-6h-5v6zM10 5v6h11V5H10z"></path></g>
<g id="view-stream"><path d="M4 18h17v-6H4v6zM4 5v6h17V5H4z"></path></g>
<g id="view-week"><path d="M6 5H3c-.55 0-1 .45-1 1v12c0 .55.45 1 1 1h3c.55 0 1-.45 1-1V6c0-.55-.45-1-1-1zm14 0h-3c-.55 0-1 .45-1 1v12c0 .55.45 1 1 1h3c.55 0 1-.45 1-1V6c0-.55-.45-1-1-1zm-7 0h-3c-.55 0-1 .45-1 1v12c0 .55.45 1 1 1h3c.55 0 1-.45 1-1V6c0-.55-.45-1-1-1z"></path></g>
<g id="visibility"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"></path></g>
<g id="visibility-off"><path d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z"></path></g>
<g id="warning"><path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"></path></g>
<g id="watch-later"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm4.2 14.2L11 13V7h1.5v5.2l4.5 2.7-.8 1.3z"></path></g>
<g id="weekend"><path d="M21 10c-1.1 0-2 .9-2 2v3H5v-3c0-1.1-.9-2-2-2s-2 .9-2 2v5c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2v-5c0-1.1-.9-2-2-2zm-3-5H6c-1.1 0-2 .9-2 2v2.15c1.16.41 2 1.51 2 2.82V14h12v-2.03c0-1.3.84-2.4 2-2.82V7c0-1.1-.9-2-2-2z"></path></g>
<g id="work"><path d="M20 6h-4V4c0-1.11-.89-2-2-2h-4c-1.11 0-2 .89-2 2v2H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-6 0h-4V4h4v2z"></path></g>
<g id="youtube-searched-for"><path d="M17.01 14h-.8l-.27-.27c.98-1.14 1.57-2.61 1.57-4.23 0-3.59-2.91-6.5-6.5-6.5s-6.5 3-6.5 6.5H2l3.84 4 4.16-4H6.51C6.51 7 8.53 5 11.01 5s4.5 2.01 4.5 4.5c0 2.48-2.02 4.5-4.5 4.5-.65 0-1.26-.14-1.82-.38L7.71 15.1c.97.57 2.09.9 3.3.9 1.61 0 3.08-.59 4.22-1.57l.27.27v.79l5.01 4.99L22 19l-4.99-5z"></path></g>
<g id="zoom-in"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14zm2.5-4h-2v2H9v-2H7V9h2V7h1v2h2v1z"></path></g>
<g id="zoom-out"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14zM7 9h5v1H7z"></path></g>
</defs></svg>
</iron-iconset-svg><dom-module id="paper-item-shared-styles">
  <template></template>
</dom-module><custom-style>
  <style is="custom-style">html {
  --shadow-transition_-_transition:  box-shadow 0.28s cubic-bezier(0.4, 0, 0.2, 1);;

      --shadow-none_-_box-shadow:  none;;

      

      --shadow-elevation-2dp_-_box-shadow:  0 2px 2px 0 rgba(0, 0, 0, 0.14),
                    0 1px 5px 0 rgba(0, 0, 0, 0.12),
                    0 3px 1px -2px rgba(0, 0, 0, 0.2);;

      --shadow-elevation-3dp_-_box-shadow:  0 3px 4px 0 rgba(0, 0, 0, 0.14),
                    0 1px 8px 0 rgba(0, 0, 0, 0.12),
                    0 3px 3px -2px rgba(0, 0, 0, 0.4);;

      --shadow-elevation-4dp_-_box-shadow:  0 4px 5px 0 rgba(0, 0, 0, 0.14),
                    0 1px 10px 0 rgba(0, 0, 0, 0.12),
                    0 2px 4px -1px rgba(0, 0, 0, 0.4);;

      --shadow-elevation-6dp_-_box-shadow:  0 6px 10px 0 rgba(0, 0, 0, 0.14),
                    0 1px 18px 0 rgba(0, 0, 0, 0.12),
                    0 3px 5px -1px rgba(0, 0, 0, 0.4);;

      --shadow-elevation-8dp_-_box-shadow:  0 8px 10px 1px rgba(0, 0, 0, 0.14),
                    0 3px 14px 2px rgba(0, 0, 0, 0.12),
                    0 5px 5px -3px rgba(0, 0, 0, 0.4);;

      --shadow-elevation-12dp_-_box-shadow:  0 12px 16px 1px rgba(0, 0, 0, 0.14),
                    0 4px 22px 3px rgba(0, 0, 0, 0.12),
                    0 6px 7px -4px rgba(0, 0, 0, 0.4);;

      --shadow-elevation-16dp_-_box-shadow:  0 16px 24px 2px rgba(0, 0, 0, 0.14),
                    0  6px 30px 5px rgba(0, 0, 0, 0.12),
                    0  8px 10px -5px rgba(0, 0, 0, 0.4);;

      --shadow-elevation-24dp_-_box-shadow:  0 24px 38px 3px rgba(0, 0, 0, 0.14),
                    0 9px 46px 8px rgba(0, 0, 0, 0.12),
                    0 11px 15px -7px rgba(0, 0, 0, 0.4);;
}

</style>
</custom-style><dom-module id="paper-material-styles">
  <template></template>
</dom-module><iron-iconset-svg name="editor" size="24" style="display: none;">
<svg><defs>
<g id="attach-file"><path d="M16.5 6v11.5c0 2.21-1.79 4-4 4s-4-1.79-4-4V5c0-1.38 1.12-2.5 2.5-2.5s2.5 1.12 2.5 2.5v10.5c0 .55-.45 1-1 1s-1-.45-1-1V6H10v9.5c0 1.38 1.12 2.5 2.5 2.5s2.5-1.12 2.5-2.5V5c0-2.21-1.79-4-4-4S7 2.79 7 5v12.5c0 3.04 2.46 5.5 5.5 5.5s5.5-2.46 5.5-5.5V6h-1.5z"></path></g>
<g id="attach-money"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z"></path></g>
<g id="border-all"><path d="M3 3v18h18V3H3zm8 16H5v-6h6v6zm0-8H5V5h6v6zm8 8h-6v-6h6v6zm0-8h-6V5h6v6z"></path></g>
<g id="border-bottom"><path d="M9 11H7v2h2v-2zm4 4h-2v2h2v-2zM9 3H7v2h2V3zm4 8h-2v2h2v-2zM5 3H3v2h2V3zm8 4h-2v2h2V7zm4 4h-2v2h2v-2zm-4-8h-2v2h2V3zm4 0h-2v2h2V3zm2 10h2v-2h-2v2zm0 4h2v-2h-2v2zM5 7H3v2h2V7zm14-4v2h2V3h-2zm0 6h2V7h-2v2zM5 11H3v2h2v-2zM3 21h18v-2H3v2zm2-6H3v2h2v-2z"></path></g>
<g id="border-clear"><path d="M7 5h2V3H7v2zm0 8h2v-2H7v2zm0 8h2v-2H7v2zm4-4h2v-2h-2v2zm0 4h2v-2h-2v2zm-8 0h2v-2H3v2zm0-4h2v-2H3v2zm0-4h2v-2H3v2zm0-4h2V7H3v2zm0-4h2V3H3v2zm8 8h2v-2h-2v2zm8 4h2v-2h-2v2zm0-4h2v-2h-2v2zm0 8h2v-2h-2v2zm0-12h2V7h-2v2zm-8 0h2V7h-2v2zm8-6v2h2V3h-2zm-8 2h2V3h-2v2zm4 16h2v-2h-2v2zm0-8h2v-2h-2v2zm0-8h2V3h-2v2z"></path></g>
<g id="border-color"><path d="M17.75 7L14 3.25l-10 10V17h3.75l10-10zm2.96-2.96c.39-.39.39-1.02 0-1.41L18.37.29c-.39-.39-1.02-.39-1.41 0L15 2.25 18.75 6l1.96-1.96z"></path><path fill-opacity=".36" d="M0 20h24v4H0z"></path></g>
<g id="border-horizontal"><path d="M3 21h2v-2H3v2zM5 7H3v2h2V7zM3 17h2v-2H3v2zm4 4h2v-2H7v2zM5 3H3v2h2V3zm4 0H7v2h2V3zm8 0h-2v2h2V3zm-4 4h-2v2h2V7zm0-4h-2v2h2V3zm6 14h2v-2h-2v2zm-8 4h2v-2h-2v2zm-8-8h18v-2H3v2zM19 3v2h2V3h-2zm0 6h2V7h-2v2zm-8 8h2v-2h-2v2zm4 4h2v-2h-2v2zm4 0h2v-2h-2v2z"></path></g>
<g id="border-inner"><path d="M3 21h2v-2H3v2zm4 0h2v-2H7v2zM5 7H3v2h2V7zM3 17h2v-2H3v2zM9 3H7v2h2V3zM5 3H3v2h2V3zm12 0h-2v2h2V3zm2 6h2V7h-2v2zm0-6v2h2V3h-2zm-4 18h2v-2h-2v2zM13 3h-2v8H3v2h8v8h2v-8h8v-2h-8V3zm6 18h2v-2h-2v2zm0-4h2v-2h-2v2z"></path></g>
<g id="border-left"><path d="M11 21h2v-2h-2v2zm0-4h2v-2h-2v2zm0-12h2V3h-2v2zm0 4h2V7h-2v2zm0 4h2v-2h-2v2zm-4 8h2v-2H7v2zM7 5h2V3H7v2zm0 8h2v-2H7v2zm-4 8h2V3H3v18zM19 9h2V7h-2v2zm-4 12h2v-2h-2v2zm4-4h2v-2h-2v2zm0-14v2h2V3h-2zm0 10h2v-2h-2v2zm0 8h2v-2h-2v2zm-4-8h2v-2h-2v2zm0-8h2V3h-2v2z"></path></g>
<g id="border-outer"><path d="M13 7h-2v2h2V7zm0 4h-2v2h2v-2zm4 0h-2v2h2v-2zM3 3v18h18V3H3zm16 16H5V5h14v14zm-6-4h-2v2h2v-2zm-4-4H7v2h2v-2z"></path></g>
<g id="border-right"><path d="M7 21h2v-2H7v2zM3 5h2V3H3v2zm4 0h2V3H7v2zm0 8h2v-2H7v2zm-4 8h2v-2H3v2zm8 0h2v-2h-2v2zm-8-8h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm8 8h2v-2h-2v2zm4-4h2v-2h-2v2zm4-10v18h2V3h-2zm-4 18h2v-2h-2v2zm0-16h2V3h-2v2zm-4 8h2v-2h-2v2zm0-8h2V3h-2v2zm0 4h2V7h-2v2z"></path></g>
<g id="border-style"><path d="M15 21h2v-2h-2v2zm4 0h2v-2h-2v2zM7 21h2v-2H7v2zm4 0h2v-2h-2v2zm8-4h2v-2h-2v2zm0-4h2v-2h-2v2zM3 3v18h2V5h16V3H3zm16 6h2V7h-2v2z"></path></g>
<g id="border-top"><path d="M7 21h2v-2H7v2zm0-8h2v-2H7v2zm4 0h2v-2h-2v2zm0 8h2v-2h-2v2zm-8-4h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2v-2H3v2zm0-4h2V7H3v2zm8 8h2v-2h-2v2zm8-8h2V7h-2v2zm0 4h2v-2h-2v2zM3 3v2h18V3H3zm16 14h2v-2h-2v2zm-4 4h2v-2h-2v2zM11 9h2V7h-2v2zm8 12h2v-2h-2v2zm-4-8h2v-2h-2v2z"></path></g>
<g id="border-vertical"><path d="M3 9h2V7H3v2zm0-4h2V3H3v2zm4 16h2v-2H7v2zm0-8h2v-2H7v2zm-4 0h2v-2H3v2zm0 8h2v-2H3v2zm0-4h2v-2H3v2zM7 5h2V3H7v2zm12 12h2v-2h-2v2zm-8 4h2V3h-2v18zm8 0h2v-2h-2v2zm0-8h2v-2h-2v2zm0-10v2h2V3h-2zm0 6h2V7h-2v2zm-4-4h2V3h-2v2zm0 16h2v-2h-2v2zm0-8h2v-2h-2v2z"></path></g>
<g id="bubble-chart"><circle cx="7.2" cy="14.4" r="3.2"></circle><circle cx="14.8" cy="18" r="2"></circle><circle cx="15.2" cy="8.8" r="4.8"></circle></g>
<g id="drag-handle"><path d="M20 9H4v2h16V9zM4 15h16v-2H4v2z"></path></g>
<g id="format-align-center"><path d="M7 15v2h10v-2H7zm-4 6h18v-2H3v2zm0-8h18v-2H3v2zm4-6v2h10V7H7zM3 3v2h18V3H3z"></path></g>
<g id="format-align-justify"><path d="M3 21h18v-2H3v2zm0-4h18v-2H3v2zm0-4h18v-2H3v2zm0-4h18V7H3v2zm0-6v2h18V3H3z"></path></g>
<g id="format-align-left"><path d="M15 15H3v2h12v-2zm0-8H3v2h12V7zM3 13h18v-2H3v2zm0 8h18v-2H3v2zM3 3v2h18V3H3z"></path></g>
<g id="format-align-right"><path d="M3 21h18v-2H3v2zm6-4h12v-2H9v2zm-6-4h18v-2H3v2zm6-4h12V7H9v2zM3 3v2h18V3H3z"></path></g>
<g id="format-bold"><path d="M15.6 10.79c.97-.67 1.65-1.77 1.65-2.79 0-2.26-1.75-4-4-4H7v14h7.04c2.09 0 3.71-1.7 3.71-3.79 0-1.52-.86-2.82-2.15-3.42zM10 6.5h3c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5h-3v-3zm3.5 9H10v-3h3.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5z"></path></g>
<g id="format-clear"><path d="M3.27 5L2 6.27l6.97 6.97L6.5 19h3l1.57-3.66L16.73 21 18 19.73 3.55 5.27 3.27 5zM6 5v.18L8.82 8h2.4l-.72 1.68 2.1 2.1L14.21 8H20V5H6z"></path></g>
<g id="format-color-fill"><path d="M16.56 8.94L7.62 0 6.21 1.41l2.38 2.38-5.15 5.15c-.59.59-.59 1.54 0 2.12l5.5 5.5c.29.29.68.44 1.06.44s.77-.15 1.06-.44l5.5-5.5c.59-.58.59-1.53 0-2.12zM5.21 10L10 5.21 14.79 10H5.21zM19 11.5s-2 2.17-2 3.5c0 1.1.9 2 2 2s2-.9 2-2c0-1.33-2-3.5-2-3.5z"></path><path fill-opacity=".36" d="M0 20h24v4H0z"></path></g>
<g id="format-color-reset"><path d="M18 14c0-4-6-10.8-6-10.8s-1.33 1.51-2.73 3.52l8.59 8.59c.09-.42.14-.86.14-1.31zm-.88 3.12L12.5 12.5 5.27 5.27 4 6.55l3.32 3.32C6.55 11.32 6 12.79 6 14c0 3.31 2.69 6 6 6 1.52 0 2.9-.57 3.96-1.5l2.63 2.63 1.27-1.27-2.74-2.74z"></path></g>
<g id="format-color-text"><path fill-opacity=".36" d="M0 20h24v4H0z"></path><path d="M11 3L5.5 17h2.25l1.12-3h6.25l1.12 3h2.25L13 3h-2zm-1.38 9L12 5.67 14.38 12H9.62z"></path></g>
<g id="format-indent-decrease"><path d="M11 17h10v-2H11v2zm-8-5l4 4V8l-4 4zm0 9h18v-2H3v2zM3 3v2h18V3H3zm8 6h10V7H11v2zm0 4h10v-2H11v2z"></path></g>
<g id="format-indent-increase"><path d="M3 21h18v-2H3v2zM3 8v8l4-4-4-4zm8 9h10v-2H11v2zM3 3v2h18V3H3zm8 6h10V7H11v2zm0 4h10v-2H11v2z"></path></g>
<g id="format-italic"><path d="M10 4v3h2.21l-3.42 8H6v3h8v-3h-2.21l3.42-8H18V4z"></path></g>
<g id="format-line-spacing"><path d="M6 7h2.5L5 3.5 1.5 7H4v10H1.5L5 20.5 8.5 17H6V7zm4-2v2h12V5H10zm0 14h12v-2H10v2zm0-6h12v-2H10v2z"></path></g>
<g id="format-list-bulleted"><path d="M4 10.5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm0-6c-.83 0-1.5.67-1.5 1.5S3.17 7.5 4 7.5 5.5 6.83 5.5 6 4.83 4.5 4 4.5zm0 12c-.83 0-1.5.68-1.5 1.5s.68 1.5 1.5 1.5 1.5-.68 1.5-1.5-.67-1.5-1.5-1.5zM7 19h14v-2H7v2zm0-6h14v-2H7v2zm0-8v2h14V5H7z"></path></g>
<g id="format-list-numbered"><path d="M2 17h2v.5H3v1h1v.5H2v1h3v-4H2v1zm1-9h1V4H2v1h1v3zm-1 3h1.8L2 13.1v.9h3v-1H3.2L5 10.9V10H2v1zm5-6v2h14V5H7zm0 14h14v-2H7v2zm0-6h14v-2H7v2z"></path></g>
<g id="format-paint"><path d="M18 4V3c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1v4c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V6h1v4H9v11c0 .55.45 1 1 1h2c.55 0 1-.45 1-1v-9h8V4h-3z"></path></g>
<g id="format-quote"><path d="M6 17h3l2-4V7H5v6h3zm8 0h3l2-4V7h-6v6h3z"></path></g>
<g id="format-shapes"><path d="M23 7V1h-6v2H7V1H1v6h2v10H1v6h6v-2h10v2h6v-6h-2V7h2zM3 3h2v2H3V3zm2 18H3v-2h2v2zm12-2H7v-2H5V7h2V5h10v2h2v10h-2v2zm4 2h-2v-2h2v2zM19 5V3h2v2h-2zm-5.27 9h-3.49l-.73 2H7.89l3.4-9h1.4l3.41 9h-1.63l-.74-2zm-3.04-1.26h2.61L12 8.91l-1.31 3.83z"></path></g>
<g id="format-size"><path d="M9 4v3h5v12h3V7h5V4H9zm-6 8h3v7h3v-7h3V9H3v3z"></path></g>
<g id="format-strikethrough"><path d="M10 19h4v-3h-4v3zM5 4v3h5v3h4V7h5V4H5zM3 14h18v-2H3v2z"></path></g>
<g id="format-textdirection-l-to-r"><path d="M9 10v5h2V4h2v11h2V4h2V2H9C6.79 2 5 3.79 5 6s1.79 4 4 4zm12 8l-4-4v3H5v2h12v3l4-4z"></path></g>
<g id="format-textdirection-r-to-l"><path d="M10 10v5h2V4h2v11h2V4h2V2h-8C7.79 2 6 3.79 6 6s1.79 4 4 4zm-2 7v-3l-4 4 4 4v-3h12v-2H8z"></path></g>
<g id="format-underlined"><path d="M12 17c3.31 0 6-2.69 6-6V3h-2.5v8c0 1.93-1.57 3.5-3.5 3.5S8.5 12.93 8.5 11V3H6v8c0 3.31 2.69 6 6 6zm-7 2v2h14v-2H5z"></path></g>
<g id="functions"><path d="M18 4H6v2l6.5 6L6 18v2h12v-3h-7l5-5-5-5h7z"></path></g>
<g id="highlight"><path d="M6 14l3 3v5h6v-5l3-3V9H6zm5-12h2v3h-2zM3.5 5.875L4.914 4.46l2.12 2.122L5.62 7.997zm13.46.71l2.123-2.12 1.414 1.414L18.375 8z"></path></g>
<g id="insert-chart"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"></path></g>
<g id="insert-comment"><path d="M20 2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14l4 4V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"></path></g>
<g id="insert-drive-file"><path d="M6 2c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6H6zm7 7V3.5L18.5 9H13z"></path></g>
<g id="insert-emoticon"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm3.5-9c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-7 0c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm3.5 6.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z"></path></g>
<g id="insert-invitation"><path d="M17 12h-5v5h5v-5zM16 1v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-1V1h-2zm3 18H5V8h14v11z"></path></g>
<g id="insert-link"><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></g>
<g id="insert-photo"><path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"></path></g>
<g id="linear-scale"><path d="M19.5 9.5c-1.03 0-1.9.62-2.29 1.5h-2.92c-.39-.88-1.26-1.5-2.29-1.5s-1.9.62-2.29 1.5H6.79c-.39-.88-1.26-1.5-2.29-1.5C3.12 9.5 2 10.62 2 12s1.12 2.5 2.5 2.5c1.03 0 1.9-.62 2.29-1.5h2.92c.39.88 1.26 1.5 2.29 1.5s1.9-.62 2.29-1.5h2.92c.39.88 1.26 1.5 2.29 1.5 1.38 0 2.5-1.12 2.5-2.5s-1.12-2.5-2.5-2.5z"></path></g>
<g id="merge-type"><path d="M17 20.41L18.41 19 15 15.59 13.59 17 17 20.41zM7.5 8H11v5.59L5.59 19 7 20.41l6-6V8h3.5L12 3.5 7.5 8z"></path></g>
<g id="mode-comment"><path d="M21.99 4c0-1.1-.89-2-1.99-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14l4 4-.01-18z"></path></g>
<g id="mode-edit"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"></path></g>
<g id="monetization-on"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1.41 16.09V20h-2.67v-1.93c-1.71-.36-3.16-1.46-3.27-3.4h1.96c.1 1.05.82 1.87 2.65 1.87 1.96 0 2.4-.98 2.4-1.59 0-.83-.44-1.61-2.67-2.14-2.48-.6-4.18-1.62-4.18-3.67 0-1.72 1.39-2.84 3.11-3.21V4h2.67v1.95c1.86.45 2.79 1.86 2.85 3.39H14.3c-.05-1.11-.64-1.87-2.22-1.87-1.5 0-2.4.68-2.4 1.64 0 .84.65 1.39 2.67 1.91s4.18 1.39 4.18 3.91c-.01 1.83-1.38 2.83-3.12 3.16z"></path></g>
<g id="money-off"><path d="M12.5 6.9c1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-.53.12-1.03.3-1.48.54l1.47 1.47c.41-.17.91-.27 1.51-.27zM5.33 4.06L4.06 5.33 7.5 8.77c0 2.08 1.56 3.21 3.91 3.91l3.51 3.51c-.34.48-1.05.91-2.42.91-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c.96-.18 1.82-.55 2.45-1.12l2.22 2.22 1.27-1.27L5.33 4.06z"></path></g>
<g id="multiline-chart"><path d="M22 6.92l-1.41-1.41-2.85 3.21C15.68 6.4 12.83 5 9.61 5 6.72 5 4.07 6.16 2 8l1.42 1.42C5.12 7.93 7.27 7 9.61 7c2.74 0 5.09 1.26 6.77 3.24l-2.88 3.24-4-4L2 16.99l1.5 1.5 6-6.01 4 4 4.05-4.55c.75 1.35 1.25 2.9 1.44 4.55H21c-.22-2.3-.95-4.39-2.04-6.14L22 6.92z"></path></g>
<g id="pie-chart"><path d="M11 2v20c-5.07-.5-9-4.79-9-10s3.93-9.5 9-10zm2.03 0v8.99H22c-.47-4.74-4.24-8.52-8.97-8.99zm0 11.01V22c4.74-.47 8.5-4.25 8.97-8.99h-8.97z"></path></g>
<g id="pie-chart-outlined"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm1 2.07c3.61.45 6.48 3.33 6.93 6.93H13V4.07zM4 12c0-4.06 3.07-7.44 7-7.93v15.87c-3.93-.5-7-3.88-7-7.94zm9 7.93V13h6.93c-.45 3.61-3.32 6.48-6.93 6.93z"></path></g>
<g id="publish"><path d="M5 4v2h14V4H5zm0 10h4v6h6v-6h4l-7-7-7 7z"></path></g>
<g id="short-text"><path d="M4 9h16v2H4zm0 4h10v2H4z"></path></g>
<g id="show-chart"><path d="M3.5 18.49l6-6.01 4 4L22 6.92l-1.41-1.41-7.09 7.97-4-4L2 16.99z"></path></g>
<g id="space-bar"><path d="M18 9v4H6V9H4v6h16V9z"></path></g>
<g id="strikethrough-s"><path d="M7.24 8.75c-.26-.48-.39-1.03-.39-1.67 0-.61.13-1.16.4-1.67.26-.5.63-.93 1.11-1.29.48-.35 1.05-.63 1.7-.83.66-.19 1.39-.29 2.18-.29.81 0 1.54.11 2.21.34.66.22 1.23.54 1.69.94.47.4.83.88 1.08 1.43.25.55.38 1.15.38 1.81h-3.01c0-.31-.05-.59-.15-.85-.09-.27-.24-.49-.44-.68-.2-.19-.45-.33-.75-.44-.3-.1-.66-.16-1.06-.16-.39 0-.74.04-1.03.13-.29.09-.53.21-.72.36-.19.16-.34.34-.44.55-.1.21-.15.43-.15.66 0 .48.25.88.74 1.21.38.25.77.48 1.41.7H7.39c-.05-.08-.11-.17-.15-.25zM21 12v-2H3v2h9.62c.18.07.4.14.55.2.37.17.66.34.87.51.21.17.35.36.43.57.07.2.11.43.11.69 0 .23-.05.45-.14.66-.09.2-.23.38-.42.53-.19.15-.42.26-.71.35-.29.08-.63.13-1.01.13-.43 0-.83-.04-1.18-.13s-.66-.23-.91-.42c-.25-.19-.45-.44-.59-.75-.14-.31-.25-.76-.25-1.21H6.4c0 .55.08 1.13.24 1.58.16.45.37.85.65 1.21.28.35.6.66.98.92.37.26.78.48 1.22.65.44.17.9.3 1.38.39.48.08.96.13 1.44.13.8 0 1.53-.09 2.18-.28s1.21-.45 1.67-.79c.46-.34.82-.77 1.07-1.27s.38-1.07.38-1.71c0-.6-.1-1.14-.31-1.61-.05-.11-.11-.23-.17-.33H21z"></path></g>
<g id="text-fields"><path d="M2.5 4v3h5v12h3V7h5V4h-13zm19 5h-9v3h3v7h3v-7h3V9z"></path></g>
<g id="title"><path d="M5 4v3h5.5v12h3V7H19V4z"></path></g>
<g id="vertical-align-bottom"><path d="M16 13h-3V3h-2v10H8l4 4 4-4zM4 19v2h16v-2H4z"></path></g>
<g id="vertical-align-center"><path d="M8 19h3v4h2v-4h3l-4-4-4 4zm8-14h-3V1h-2v4H8l4 4 4-4zM4 11v2h16v-2H4z"></path></g>
<g id="vertical-align-top"><path d="M8 11h3v10h2V11h3l-4-4-4 4zM4 3v2h16V3H4z"></path></g>
<g id="wrap-text"><path d="M4 19h6v-2H4v2zM20 5H4v2h16V5zm-3 6H4v2h13.25c1.1 0 2 .9 2 2s-.9 2-2 2H15v-2l-3 3 3 3v-2h2c2.21 0 4-1.79 4-4s-1.79-4-4-4z"></path></g>
</defs></svg>
</iron-iconset-svg><iron-iconset-svg name="paper-dropdown-menu" size="24" style="display: none;">
<svg><defs>
<g id="arrow-drop-down"><path d="M7 10l5 5 5-5z"></path></g>
</defs></svg>
</iron-iconset-svg><dom-module id="paper-dropdown-menu-shared-styles">
  <template></template>
</dom-module><iron-iconset-svg name="social" size="24" style="display: none;">
<svg><defs>
<g id="cake"><path d="M12 6c1.11 0 2-.9 2-2 0-.38-.1-.73-.29-1.03L12 0l-1.71 2.97c-.19.3-.29.65-.29 1.03 0 1.1.9 2 2 2zm4.6 9.99l-1.07-1.07-1.08 1.07c-1.3 1.3-3.58 1.31-4.89 0l-1.07-1.07-1.09 1.07C6.75 16.64 5.88 17 4.96 17c-.73 0-1.4-.23-1.96-.61V21c0 .55.45 1 1 1h16c.55 0 1-.45 1-1v-4.61c-.56.38-1.23.61-1.96.61-.92 0-1.79-.36-2.44-1.01zM18 9h-5V7h-2v2H6c-1.66 0-3 1.34-3 3v1.54c0 1.08.88 1.96 1.96 1.96.52 0 1.02-.2 1.38-.57l2.14-2.13 2.13 2.13c.74.74 2.03.74 2.77 0l2.14-2.13 2.13 2.13c.37.37.86.57 1.38.57 1.08 0 1.96-.88 1.96-1.96V12C21 10.34 19.66 9 18 9z"></path></g>
<g id="domain"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"></path></g>
<g id="group"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"></path></g>
<g id="group-add"><path d="M8 10H5V7H3v3H0v2h3v3h2v-3h3v-2zm10 1c1.66 0 2.99-1.34 2.99-3S19.66 5 18 5c-.32 0-.63.05-.91.14.57.81.9 1.79.9 2.86s-.34 2.04-.9 2.86c.28.09.59.14.91.14zm-5 0c1.66 0 2.99-1.34 2.99-3S14.66 5 13 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm6.62 2.16c.83.73 1.38 1.66 1.38 2.84v2h3v-2c0-1.54-2.37-2.49-4.38-2.84zM13 13c-2 0-6 1-6 3v2h12v-2c0-2-4-3-6-3z"></path></g>
<g id="location-city"><path d="M15 11V5l-3-3-3 3v2H3v14h18V11h-6zm-8 8H5v-2h2v2zm0-4H5v-2h2v2zm0-4H5V9h2v2zm6 8h-2v-2h2v2zm0-4h-2v-2h2v2zm0-4h-2V9h2v2zm0-4h-2V5h2v2zm6 12h-2v-2h2v2zm0-4h-2v-2h2v2z"></path></g>
<g id="mood"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm3.5-9c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-7 0c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm3.5 6.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z"></path></g>
<g id="mood-bad"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm3.5-9c.83 0 1.5-.67 1.5-1.5S16.33 8 15.5 8 14 8.67 14 9.5s.67 1.5 1.5 1.5zm-7 0c.83 0 1.5-.67 1.5-1.5S9.33 8 8.5 8 7 8.67 7 9.5 7.67 11 8.5 11zm3.5 3c-2.33 0-4.31 1.46-5.11 3.5h10.22c-.8-2.04-2.78-3.5-5.11-3.5z"></path></g>
<g id="notifications"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"></path></g>
<g id="notifications-active"><path d="M7.58 4.08L6.15 2.65C3.75 4.48 2.17 7.3 2.03 10.5h2c.15-2.65 1.51-4.97 3.55-6.42zm12.39 6.42h2c-.15-3.2-1.73-6.02-4.12-7.85l-1.42 1.43c2.02 1.45 3.39 3.77 3.54 6.42zM18 11c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2v-5zm-6 11c.14 0 .27-.01.4-.04.65-.14 1.18-.58 1.44-1.18.1-.24.15-.5.15-.78h-4c.01 1.1.9 2 2.01 2z"></path></g>
<g id="notifications-none"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.63-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.64 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2zm-2 1H8v-6c0-2.48 1.51-4.5 4-4.5s4 2.02 4 4.5v6z"></path></g>
<g id="notifications-off"><path d="M20 18.69L7.84 6.14 5.27 3.49 4 4.76l2.8 2.8v.01c-.52.99-.8 2.16-.8 3.42v5l-2 2v1h13.73l2 2L21 19.72l-1-1.03zM12 22c1.11 0 2-.89 2-2h-4c0 1.11.89 2 2 2zm6-7.32V11c0-3.08-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68c-.15.03-.29.08-.42.12-.1.03-.2.07-.3.11h-.01c-.01 0-.01 0-.02.01-.23.09-.46.2-.68.31 0 0-.01 0-.01.01L18 14.68z"></path></g>
<g id="notifications-paused"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.93 6 11v5l-2 2v1h16v-1l-2-2zm-3.5-6.2l-2.8 3.4h2.8V15h-5v-1.8l2.8-3.4H9.5V8h5v1.8z"></path></g>
<g id="pages"><path d="M3 5v6h5L7 7l4 1V3H5c-1.1 0-2 .9-2 2zm5 8H3v6c0 1.1.9 2 2 2h6v-5l-4 1 1-4zm9 4l-4-1v5h6c1.1 0 2-.9 2-2v-6h-5l1 4zm2-14h-6v5l4-1-1 4h5V5c0-1.1-.9-2-2-2z"></path></g>
<g id="party-mode"><path d="M20 4h-3.17L15 2H9L7.17 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-8 3c1.63 0 3.06.79 3.98 2H12c-1.66 0-3 1.34-3 3 0 .35.07.69.18 1H7.1c-.06-.32-.1-.66-.1-1 0-2.76 2.24-5 5-5zm0 10c-1.63 0-3.06-.79-3.98-2H12c1.66 0 3-1.34 3-3 0-.35-.07-.69-.18-1h2.08c.07.32.1.66.1 1 0 2.76-2.24 5-5 5z"></path></g>
<g id="people"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"></path></g>
<g id="people-outline"><path d="M16.5 13c-1.2 0-3.07.34-4.5 1-1.43-.67-3.3-1-4.5-1C5.33 13 1 14.08 1 16.25V19h22v-2.75c0-2.17-4.33-3.25-6.5-3.25zm-4 4.5h-10v-1.25c0-.54 2.56-1.75 5-1.75s5 1.21 5 1.75v1.25zm9 0H14v-1.25c0-.46-.2-.86-.52-1.22.88-.3 1.96-.53 3.02-.53 2.44 0 5 1.21 5 1.75v1.25zM7.5 12c1.93 0 3.5-1.57 3.5-3.5S9.43 5 7.5 5 4 6.57 4 8.5 5.57 12 7.5 12zm0-5.5c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 5.5c1.93 0 3.5-1.57 3.5-3.5S18.43 5 16.5 5 13 6.57 13 8.5s1.57 3.5 3.5 3.5zm0-5.5c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2z"></path></g>
<g id="person"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"></path></g>
<g id="person-add"><path d="M15 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm-9-2V7H4v3H1v2h3v3h2v-3h3v-2H6zm9 4c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"></path></g>
<g id="person-outline"><path d="M12 5.9c1.16 0 2.1.94 2.1 2.1s-.94 2.1-2.1 2.1S9.9 9.16 9.9 8s.94-2.1 2.1-2.1m0 9c2.97 0 6.1 1.46 6.1 2.1v1.1H5.9V17c0-.64 3.13-2.1 6.1-2.1M12 4C9.79 4 8 5.79 8 8s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm0 9c-2.67 0-8 1.34-8 4v3h16v-3c0-2.66-5.33-4-8-4z"></path></g>
<g id="plus-one"><path d="M10 8H8v4H4v2h4v4h2v-4h4v-2h-4zm4.5-1.92V7.9l2.5-.5V18h2V5z"></path></g>
<g id="poll"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"></path></g>
<g id="public"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"></path></g>
<g id="school"><path d="M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82zM12 3L1 9l11 6 9-4.91V17h2V9L12 3z"></path></g>
<g id="sentiment-dissatisfied"><circle cx="15.5" cy="9.5" r="1.5"></circle><circle cx="8.5" cy="9.5" r="1.5"></circle><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm0-6c-2.33 0-4.32 1.45-5.12 3.5h1.67c.69-1.19 1.97-2 3.45-2s2.75.81 3.45 2h1.67c-.8-2.05-2.79-3.5-5.12-3.5z"></path></g>
<g id="sentiment-neutral"><path d="M9 14h6v1.5H9z"></path><circle cx="15.5" cy="9.5" r="1.5"></circle><circle cx="8.5" cy="9.5" r="1.5"></circle><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"></path></g>
<g id="sentiment-satisfied"><circle cx="15.5" cy="9.5" r="1.5"></circle><circle cx="8.5" cy="9.5" r="1.5"></circle><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm0-4c-1.48 0-2.75-.81-3.45-2H6.88c.8 2.05 2.79 3.5 5.12 3.5s4.32-1.45 5.12-3.5h-1.67c-.7 1.19-1.97 2-3.45 2z"></path></g>
<g id="sentiment-very-dissatisfied"><path d="M11.99 2C6.47 2 2 6.47 2 12s4.47 10 9.99 10S22 17.53 22 12 17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm4.18-12.24l-1.06 1.06-1.06-1.06L13 8.82l1.06 1.06L13 10.94 14.06 12l1.06-1.06L16.18 12l1.06-1.06-1.06-1.06 1.06-1.06zM7.82 12l1.06-1.06L9.94 12 11 10.94 9.94 9.88 11 8.82 9.94 7.76 8.88 8.82 7.82 7.76 6.76 8.82l1.06 1.06-1.06 1.06zM12 14c-2.33 0-4.31 1.46-5.11 3.5h10.22c-.8-2.04-2.78-3.5-5.11-3.5z"></path></g>
<g id="sentiment-very-satisfied"><path d="M11.99 2C6.47 2 2 6.47 2 12s4.47 10 9.99 10S22 17.53 22 12 17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm1-10.06L14.06 11l1.06-1.06L16.18 11l1.06-1.06-2.12-2.12zm-4.12 0L9.94 11 11 9.94 8.88 7.82 6.76 9.94 7.82 11zM12 17.5c2.33 0 4.31-1.46 5.11-3.5H6.89c.8 2.04 2.78 3.5 5.11 3.5z"></path></g>
<g id="share"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"></path></g>
<g id="whatshot"><path d="M13.5.67s.74 2.65.74 4.8c0 2.06-1.35 3.73-3.41 3.73-2.07 0-3.63-1.67-3.63-3.73l.03-.36C5.21 7.51 4 10.62 4 14c0 4.42 3.58 8 8 8s8-3.58 8-8C20 8.61 17.41 3.8 13.5.67zM11.71 19c-1.78 0-3.22-1.4-3.22-3.14 0-1.62 1.05-2.76 2.81-3.12 1.77-.36 3.6-1.21 4.62-2.58.39 1.29.59 2.65.59 4.04 0 2.65-2.15 4.8-4.8 4.8z"></path></g>
</defs></svg>
</iron-iconset-svg><iron-iconset-svg name="paper-tabs" size="24" style="display: none;">
<svg><defs>
<g id="chevron-left"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></g>
<g id="chevron-right"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></g>
</defs></svg>
</iron-iconset-svg><custom-style include="colab-styles"><style>.formview {
  --paper-input-container_-_padding:  0;

          --paper-slider-input_-_width:  auto;
}

colab-date-picker paper-input {
  --paper-input-error_-_overflow:  visible;

          --paper-input-container-input-webkit-spinner_-_display:  none;

          --paper-input-container-input-webkit-clear_-_display:  none;
}

body:not(.mobile) paper-listbox, body:not(.mobile) paper-item {
  white-space: nowrap;
}

html {
  --paper-input-container-underline-wrapper-height: 0;
}

paper-tabs {
  --paper-font-common-base_-_font-family:  var(--colab-google-sans-font-family); --paper-font-common-base_-_-webkit-font-smoothing: initial;
          --paper-tabs-selection-bar_-_z-index:  1;
}

paper-tab {
  --paper-tab-content-focused_-_background:  var(--colab-secondary-surface-color); --paper-tab-content-focused_-_font-weight:  700; --paper-tab-content-focused_-_background-color: initial;
}

colab-debugger paper-toolbar {
  background: var(--paper-grey-800);
          --paper-toolbar-height: 32px;
          --paper-toolbar-title_-_font-size:  14px; --paper-toolbar-title_-_font-weight:  bold; --paper-toolbar-title_-_margin:  0;
}

colab-debugger .inspect-breakpoints-add {
  --paper-input-container_-_padding:  0 0 8px 0;
}

colab-debugger paper-tab {
  --paper-tab-content-focused_-_background:  var(--colab-highlighted-surface-color); --paper-tab-content-focused_-_font-weight:  700; --paper-tab-content-focused_-_background-color: initial;
}

.tab-pane-header paper-tabs {
  position: relative;
          padding: 0 4px 0 8px;

          --paper-icon-buttons_-_background-color:  var(--google-blue-600); --paper-icon-buttons_-_border-radius:  50%; --paper-icon-buttons_-_color:  white; --paper-icon-buttons_-_height:  20px; --paper-icon-buttons_-_padding:  2px; --paper-icon-buttons_-_position:  absolute; --paper-icon-buttons_-_width:  20px;

          --paper-icon-button-left_-_left:  0; --paper-icon-button-left_-_z-index:  1;

          --paper-icon-button-right_-_right:  -3px;
}

.tab-pane-header paper-tab {
  --paper-tab-content-focused_-_background-color:  transparent; --paper-tab-content-focused_-_font-weight:  500; --paper-tab-content-focused_-_background: initial;
}

colab-tab-layout-container.flexible-tabs .tab-pane-header paper-tabs {
  --paper-tab-content-unselected {
            opacity: 1;
          }
}

.colab-open-dialog paper-tabs {
  --paper-icon-buttons_-_background-color:  var(--paper-orange-700); --paper-icon-buttons_-_border-radius:  50%; --paper-icon-buttons_-_color:  white; --paper-icon-buttons_-_height:  20px; --paper-icon-buttons_-_padding:  2px; --paper-icon-buttons_-_position:  absolute; --paper-icon-buttons_-_width:  20px;

          --paper-icon-button-left_-_left:  0; --paper-icon-button-left_-_z-index:  1;

          --paper-icon-button-right_-_right:  -3px;
}

.command-palette {
  --paper-input-container-shared-input-style_-_font-size:  var(--colab-chrome-font-size); --paper-input-container-shared-input-style_-_padding:  0 4px; --paper-input-container-shared-input-style_-_width:  100%; --paper-input-container-shared-input-style_-_position: initial; --paper-input-container-shared-input-style_-_outline: initial; --paper-input-container-shared-input-style_-_box-shadow: initial; --paper-input-container-shared-input-style_-_margin: initial; --paper-input-container-shared-input-style_-_max-width: initial; --paper-input-container-shared-input-style_-_background: initial; --paper-input-container-shared-input-style_-_border: initial; --paper-input-container-shared-input-style_-_color: initial; --paper-input-container-shared-input-style_-_-webkit-appearance: initial; --paper-input-container-shared-input-style_-_text-align: initial; --paper-input-container-shared-input-style_-_vertical-align: initial; --paper-input-container-shared-input-style_-_font-family: initial; --paper-input-container-shared-input-style_-_-webkit-font-smoothing: initial; --paper-input-container-shared-input-style_-_font-weight: initial; --paper-input-container-shared-input-style_-_line-height: initial;
          --paper-input-container-underline-focus-height: 0;
          --paper-input-container-underline-height: 0;
}

</style></custom-style><custom-style include="colab-themes"><style></style></custom-style><custom-style>
    <style is="custom-style">html {
  --google-orange-600: #e8710a;
        --google-yellow-600: #f9ab00;
        
        --code-cell-background: #f7f7f7;
        --colab-anchor-color: #00e;
        --colab-border-color: #dadada;
        --colab-bold-border-color: #111;
        --colab-callout-color: var(--paper-blue-700);
        --colab-divider-color: var(--paper-grey-300);
        --colab-debugger-line-color: var(--paper-red-100);
        --colab-editor-focus-color: var(--paper-grey-200);
        --colab-highlighted-surface-color: var(--paper-grey-200);
        --colab-icon-color: var(--paper-grey-700);
        --colab-secondary-icon-color: #93ADCF;
        --colab-input-placeholder-color: var(--colab-secondary-text-color);
        --colab-primary-surface-color: var(--paper-white);
        --colab-primary-text-color: var(--paper-grey-900);
        --colab-secondary-text-color: #616161;
        --colab-tertiary-text-color: var(--paper-grey-600);
        --colab-secondary-surface-color: #f7f7f7;
        --colab-scrollbar-color: rgba(0, 0, 0, 0.1);
        --colab-gutter-icon-color: #8c8c8c;
        --colab-active-execution-icon-color: var(--paper-grey-800);
        --colab-error-icon-color: var(--paper-red-a700);
        --colab-title-color: #000;
        --colab-toolbar-button-color: var(--paper-grey-800);
        --colab-form-field-underline-color: var(--paper-grey-600);
        --colab-editor-focus-border-thickness: 2px;
        --colab-diff-editor-background: #fff;
        --colab-local-diff-background: #eef;
        --colab-remote-diff-background: #feffe0;
        --colab-merged-diff-background: #d7fed8;
        --colab-status-okay: var(--google-green-700);
        --ansi-black: rgb(0, 0, 0);
        --ansi-red: rgb(139, 0, 0);
        --ansi-green: rgb(0, 100, 0);
        --ansi-yellow: rgb(205, 205, 0);
        --ansi-blue: rgb(0, 0, 238);
        --ansi-magenta: rgb(205, 0, 205);
        --ansi-cyan: rgb(70, 130, 180);
        --ansi-gray: rgb(229, 229, 229);
        --ansi-bright-black: rgb(127, 127, 127);
        --ansi-bright-red: rgb(255, 0, 0);
        --ansi-bright-green: rgb(0, 208, 0);
        --ansi-bright-yellow: rgb(255, 255, 0);
        --ansi-bright-blue: rgb(92, 92, 255);
        --ansi-bright-magenta: rgb(255, 0, 255);
        --ansi-bright-cyan: rgb(0, 255, 255);
        --ansi-bright-gray: rgb(255, 255, 255);
        --gcp-success-icon-color: var(--google-green-700);
        --colab-comment-anchor-color: var(--google-blue-600);
        --colab-filled-button-ripple-color: #000;
        --colab-comment-highlight-color: #ffe082; 
        
        --colab-input-border-color: #a9a9a9;
        --colab-logo-dark: var(--google-orange-600);
        --colab-logo-light: var(--google-yellow-600);
        --colab-status-error: #e51c23;
        --colab-status-warning: #f09300;
        --colab-chrome-font-family: 'Roboto', 'Noto', sans-serif;
        --colab-google-sans-font-family: 'Google Sans', 'Roboto', 'Noto', sans-serif;
        --colab-chrome-font-size: 14px;
        
        --colab-icon-hover-color: var(--colab-primary-text-color);
        --colab-fresh-execution-count-color: var(--colab-primary-text-color);
        --colab-stale-execution-count-color: var(--colab-input-placeholder-color);
        
        --primary-text-color: var(--colab-primary-text-color);
        --secondary-text-color: var(--colab-secondary-text-color);
        --primary-background-color: var(--colab-primary-surface-color);
        --paper-input-container-color: var(--colab-input-placeholder-color);
        --paper-slider-active-color: var(--primary-color);
        --paper-slider-knob-color: var(--primary-color);
        --paper-tabs-selection-bar-color: var(--google-blue-600);
        --error-color: #B3261E;
        --primary-color: var(--google-blue-700);
        --google-green-700: #188038;
        --google-grey-800: #3c4043;
        --google-blue-200: #AECBFA;
        --google-blue-300: #8AB4F8;
        --google-blue-700: #1967d2;
        --google-blue-900: #174ea6;
        --hairline-button-primary: var(--primary-color);
        --hairline-button-secondary: var(--google-blue-900);
        
        --hairline-button-overlay-hovered: #4285f40a;
        
        --hairline-button-disabled-label: var(--paper-grey-500);
        
        --hairline-button-disabled-container: var(--paper-grey-100);
        --mdc-theme-primary: var(--primary-color);
        --mdc-theme-on-primary: var(--colab-primary-surface-color);
        --md-sys-color-primary: var(--primary-color);
        --md-sys-color-on-primary: var(--colab-primary-surface-color);
}

html[theme=dark] {
  --colab-anchor-color: var(--paper-blue-300);
        --colab-callout-color: var(--google-blue-600);
        --code-cell-background: #1e1e1e;
        --colab-border-color: var(--paper-grey-700);
        --colab-bold-border-color: #eee;
        --colab-divider-color: var(--paper-grey-700);
        --colab-debugger-line-color: var(--paper-red-900);
        --colab-editor-focus-color: #282828;
        --colab-highlighted-surface-color: #525252;
        --colab-icon-color: var(--paper-grey-400);
        --colab-input-placeholder-color: var(--colab-tertiary-text-color);
        --colab-primary-surface-color: #383838;
        --colab-primary-text-color: #d5d5d5;
        --colab-secondary-text-color: #f7f7f7;
        --colab-tertiary-text-color: #b3b3b3;
        --colab-secondary-surface-color: #454545;
        --colab-scrollbar-color: rgba(255, 255, 255, 0.2);
        --colab-gutter-icon-color: #858585;
        --colab-active-execution-icon-color: var(--colab-icon-color);
        --colab-error-icon-color: var(--paper-red-400);
        --colab-title-color: #fff;
        --colab-toolbar-button-color: var(--paper-grey-200);
        --colab-form-field-underline-color: var(--paper-grey-400);
        --colab-diff-editor-background: #000;
        --colab-local-diff-background: #292935;
        --colab-remote-diff-background: #2e2f08;
        --colab-merged-diff-background: #09380b;
        --colab-status-okay: #00c752;
        --ansi-black: rgb(127, 127, 127);
        --ansi-red: rgb(255, 122, 136);
        --ansi-green: rgb(87, 187, 138);
        --ansi-yellow: rgb(255, 255, 102);
        --ansi-blue: rgb(130, 177, 255);
        --ansi-magenta: rgb(205, 0, 205);
        --ansi-cyan: rgb(153, 187, 215);
        --ansi-gray: rgb(229, 229, 229);
        --ansi-bright-green: rgb(0, 255, 0);
        --gcp-success-icon-color: #81c995;
        --colab-comment-anchor-color: var(--paper-blue-300);
        --colab-filled-button-ripple-color: #fff;
        --colab-comment-highlight-color: #1a237e; 
        
        --error-color: var(--paper-deep-orange-a100);
        --primary-color: var(--google-blue-300);
        --hairline-button-primary: var(--primary-color);
        --hairline-button-secondary: var(--google-blue-200);
        
        --hairline-button-overlay-hovered: #42a5f50a;
        
        --hairline-button-disabled-label: #ffffff4d;
        --hairline-button-disabled-container: #ffffff1f;
}

@media (prefers-color-scheme: dark) {
html[theme=adaptive] {
  --colab-anchor-color: var(--paper-blue-400);
          --colab-callout-color: var(--paper-blue-900);
          --code-cell-background: #1e1e1e;
          --colab-border-color: var(--paper-grey-700);
          --colab-bold-border-color: #eee;
          --colab-divider-color: var(--paper-grey-700);
          --colab-debugger-line-color: var(--paper-red-900);
          --colab-editor-focus-color: #282828;
          --colab-highlighted-surface-color: #525252;
          --colab-icon-color: var(--paper-grey-100);
          --colab-input-placeholder-color: var(--colab-tertiary-text-color);
          --colab-primary-surface-color: #383838;
          --colab-primary-text-color: #d5d5d5;
          --colab-secondary-text-color: #f7f7f7;
          --colab-tertiary-text-color: #b3b3b3;
          --colab-secondary-surface-color: #454545;
          --colab-scrollbar-color: rgba(255, 255, 255, 0.2);
          --colab-gutter-icon-color: #858585;
          --colab-execution-count: var(--colab-primary-text-color);
          --colab-active-execution-icon-color: var(--colab-icon-color);
          --colab-error-icon-color: var(--paper-red-400);
          --colab-title-color: #fff;
          --colab-toolbar-button-color: var(--paper-grey-200);
          --colab-form-field-underline-color: var(--paper-grey-400);
          --colab-diff-editor-background: #000;
          --colab-local-diff-background: #292935;
          --colab-remote-diff-background: #2e2f08;
          --colab-merged-diff-background: #09380b;
          --colab-status-okay: #00c752;
          --ansi-black: rgb(63, 63, 63);
          --ansi-red: rgb(255, 122, 136);
          --ansi-green: rgb(87, 187, 138);
          --ansi-yellow: rgb(255, 255, 102);
          --ansi-blue: rgb(130, 177, 255);
          --ansi-magenta: rgb(205, 0, 205);
          --ansi-cyan: rgb(153, 187, 215);
          --ansi-gray: rgb(229, 229, 229);
          --colab-filled-button-ripple-color: #fff;
          
          --error-color: var(--paper-deep-orange-a100);
          --primary-color: var(--google-blue-300);
          --hairline-button-primary: var(--primary-color);
          --hairline-button-secondary: var(--google-blue-200);
          
          --hairline-button-overlay-hovered: #42a5f50a;
          
          --hairline-button-disabled-label: #9e9e9e80;
          --hairline-button-disabled-container: #9e9e9e80;
}

}

html[editor="High Contrast Dark"] {
  --code-cell-background: #000;
        --colab-editor-focus-color: #f38518;
        --colab-editor-focus-border-thickness: 1px;
}

html[editor=Monokai] {
  --code-cell-background: #272822;
}

html[editor="All Hallows Eve"] {
  --code-cell-background: #000;
}

html[editor="Amy"] {
  --code-cell-background: #200020;
}

html[editor="Birds Of Paradise"] {
  --code-cell-background: #372725;
}

html[editor="Blackboard"] {
  --code-cell-background: #0c1021;
}

html[editor="Clouds Midnight"] {
  --code-cell-background: #191919;
}

html[editor="Dominion Day"] {
  --code-cell-background: #372725;
}

html[editor="Espresso Libre"] {
  --code-cell-background: #2a211c;
}

html[editor="Merbivore"] {
  --code-cell-background: #161616;
}

html[editor="Night Owl"] {
  --code-cell-background: #011627;
}

html[editor="Oceanic Next"] {
  --code-cell-background: #1b2b34;
}

html[editor="Pastels On Dark"] {
  --code-cell-background: #211e1e;
}

html[editor="Space Cadet"] {
  --code-cell-background: #0d0d0d;
}

html[editor="Sunburst"] {
  --code-cell-background: #000;
}

html[editor="Twilight"] {
  --code-cell-background: #141414;
}

html[editor="Vibrant Ink"] {
  --code-cell-background: #000;
}

html[editor="Zenburnesque"] {
  --code-cell-background: #404040;
}

html[editor="Idle Fingers"] {
  --code-cell-background: #323232;
}

html[editor="Mono Industrial"] {
  --code-cell-background: #222c28;
}

html[editor=Synthwave84] {
  --colab-primary-surface-color: #241b2f;
        --colab-secondary-surface-color: #49549539;
        --code-cell-background: #262335;
        --colab-highlighted-surface-color: #372d4b;
        --colab-border-color: #34294fb3;
        --colab-anchor-color: #f97e72;
        --ansi-red: #fe4450;
        --ansi-green: #72f1b8;
        --ansi-yellow: #f97e72;
        --ansi-blue: #03edf9;
        --ansi-magenta: #ff7edb;
        --ansi-cyan: #03edf9;
        --ansi-bright-red: #fe4450;
        --ansi-bright-green: #72f1b8;
        --ansi-bright-yellow: #fede5d;
        --ansi-bright-blue: #03edf9;
        --ansi-bright-magenta: #ff7edb;
        --ansi-bright-cyan: #03edf9;
}

</style>
  </custom-style><script async="" type="text/javascript" charset="UTF-8" src="./titanic_survival_prediction_files/rs=AA2YrTsL4HiE1bvJV-MS9_mgAxWPHzXqxw" nonce=""></script><link type="text/css" rel="stylesheet" href="./titanic_survival_prediction_files/rs=AA2YrTvwL5uXLldqnwtu49O3C0adR0c4Jg"><style type="text/css"><br>* {<br>  -webkit-user-select: text !important;<br>  -moz-user-select: text !important;<br>  -ms-user-select: text !important;<br>   user-select: text !important;<br>}<br></style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./titanic_survival_prediction_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./titanic_survival_prediction_files/editor.main.css"><script async="async" type="text/javascript" src="./titanic_survival_prediction_files/editor.main.nls.js.download"></script><script src="./titanic_survival_prediction_files/api.js.download" nonce=""></script><script src="./titanic_survival_prediction_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-insertedLineBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #6aa94f; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #f28b82; }
.mtk11 { color: #d7ba7d; }
.mtk12 { color: #dcdcdc; }
.mtk13 { color: #808080; }
.mtk14 { color: #4ec9b0; }
.mtk15 { color: #dcdcaa; }
.mtk16 { color: #f44747; }
.mtk17 { color: #82c6ff; }
.mtk18 { color: #c586c0; }
.mtk19 { color: #a79873; }
.mtk20 { color: #dd6a6f; }
.mtk21 { color: #5bb498; }
.mtk22 { color: #909090; }
.mtk23 { color: #778899; }
.mtk24 { color: #ff00ff; }
.mtk25 { color: #b46695; }
.mtk26 { color: #ff0000; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #3dc9b0; }
.mtk29 { color: #74b0df; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./titanic_survival_prediction_files/gapi_loader.js.download" nonce=""></script><script src="./titanic_survival_prediction_files/socketio_binary.js.download" nonce=""></script><script src="./titanic_survival_prediction_files/analytics_binary.js.download" nonce=""></script><script src="./titanic_survival_prediction_files/MathJax.js.download" nonce=""></script><script src="./titanic_survival_prediction_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');
          window.Polymer = {
            'legacyOptimizations': true,
          };
          </script><script src="./titanic_survival_prediction_files/external_polymer_binary_l10n__en_gb.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><paper-toast text="" id="message-area" class="message-area" style="outline: none; position: fixed; box-sizing: border-box; left: 0px; top: 622.2px; max-width: 288px; max-height: 48.8px; display: none;" aria-hidden="true"><template shadowrootmode="open"><style scope="paper-toast">:host {
  display: block;
        position: fixed;
        background-color: var(--paper-toast-background-color, #323232);
        color: var(--paper-toast-color, #f1f1f1);
        min-height: 48px;
        min-width: 288px;
        padding: 16px 24px;
        box-sizing: border-box;
        box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.26);
        border-radius: 2px;
        margin: 12px;
        font-size: 14px;
        cursor: default;
        -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
        transition: transform 0.3s, opacity 0.3s;
        opacity: 0;
        -webkit-transform: translateY(100px);
        transform: translateY(100px);
        font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
}

:host(.capsule) {
  border-radius: 24px;
}

:host(.fit-bottom) {
  width: 100%;
        min-width: 0;
        border-radius: 0;
        margin: 0;
}

:host(.paper-toast-open) {
  opacity: 1;
        -webkit-transform: translateY(0px);
        transform: translateY(0px);
}</style>
    

    <span id="label">Runtime disconnected</span>
    <slot></slot>
</template>
      <span class="paper-toast-extra"></span>
      <paper-icon-button class="close" icon="icons:close" aria-label="Close" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
      </paper-icon-button>
    </paper-toast><iron-a11y-announcer><template shadowrootmode="open"><style scope="iron-a11y-announcer">:host {
  display: inline-block;
        position: fixed;
        clip: rect(0px,0px,0px,0px);
}</style>
    
    <div aria-live="polite">Runtime disconnected</div>
</template></iron-a11y-announcer><paper-toast text="" id="message-area-secondary" class="message-area startup" style="outline: none; position: fixed; box-sizing: border-box; left: 0px; top: 622.2px; max-width: 288px; max-height: 48.8px; display: none;" aria-hidden="true"><template shadowrootmode="open"><style scope="paper-toast">:host {
  display: block;
        position: fixed;
        background-color: var(--paper-toast-background-color, #323232);
        color: var(--paper-toast-color, #f1f1f1);
        min-height: 48px;
        min-width: 288px;
        padding: 16px 24px;
        box-sizing: border-box;
        box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.26);
        border-radius: 2px;
        margin: 12px;
        font-size: 14px;
        cursor: default;
        -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
        transition: transform 0.3s, opacity 0.3s;
        opacity: 0;
        -webkit-transform: translateY(100px);
        transform: translateY(100px);
        font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
}

:host(.capsule) {
  border-radius: 24px;
}

:host(.fit-bottom) {
  width: 100%;
        min-width: 0;
        border-radius: 0;
        margin: 0;
}

:host(.paper-toast-open) {
  opacity: 1;
        -webkit-transform: translateY(0px);
        transform: translateY(0px);
}</style>
    

    <span id="label">Loading…</span>
    <slot></slot>
</template>
      <span class="paper-toast-extra"></span>
      <paper-icon-button class="close" icon="icons:close" aria-label="Close" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
      </paper-icon-button>
    </paper-toast><div ng-non-bindable=""></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Bd;_.Ad=function(a){const b=a.length;if(0<b){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Bd=function(a){return a};_.Cd=function(a){var b=null,c=_.q.trustedTypes;if(!c||!c.createPolicy)return b;try{b=c.createPolicy(a,{createHTML:Bd,createScript:Bd,createScriptURL:Bd})}catch(d){_.q.console&&_.q.console.error(d.message)}return b};_.Dd=function(a,b){return 0==a.lastIndexOf(b,0)};_.Ed=function(a,b){return Array.prototype.some.call(a,b,void 0)};try{(new self.OffscreenCanvas(0,0)).getContext("2d")}catch(a){};var Fd;_.Gd=function(){void 0===Fd&&(Fd=_.Cd("ogb-qtm#html"));return Fd};var Jd,Ld;_.Hd=class{constructor(a){this.i=a}toString(){return this.i.toString()}};_.Id=function(a){return a instanceof _.Hd&&a.constructor===_.Hd?a.i:"type_error:SafeUrl"};try{new URL("s://g"),Jd=!0}catch(a){Jd=!1}_.Kd=Jd;Ld={};_.Md=function(a){return new _.Hd(a,Ld)};_.Nd=_.Md("about:invalid#zClosurez");_.Od={};_.Pd=class{constructor(a){this.i=a}toString(){return this.i.toString()}};_.Qd=new _.Pd("",_.Od);_.Rd=RegExp("^[-+,.\"'%_!#/ a-zA-Z0-9\\[\\]]+$");_.Sd=RegExp("\\b(url\\([ \t\n]*)('[ -&(-\\[\\]-~]*'|\"[ !#-\\[\\]-~]*\"|[!#-&*-\\[\\]-~]*)([ \t\n]*\\))","g");_.Td=RegExp("\\b(calc|cubic-bezier|fit-content|hsl|hsla|linear-gradient|matrix|minmax|radial-gradient|repeat|rgb|rgba|(rotate|scale|translate)(X|Y|Z|3d)?|steps|var)\\([-+*/0-9a-zA-Z.%#\\[\\], ]+\\)","g");var Ud;Ud={};_.Wd=function(a){return a instanceof _.Vd&&a.constructor===_.Vd?a.i:"type_error:SafeHtml"};_.Xd=function(a){const b=_.Gd();a=b?b.createHTML(a):a;return new _.Vd(a,Ud)};_.Vd=class{constructor(a){this.i=a}toString(){return this.i.toString()}};_.Yd=new _.Vd(_.q.trustedTypes&&_.q.trustedTypes.emptyHTML||"",Ud);_.Zd=_.Xd("<br>");var ae;_.$d=function(a){let b=!1,c;return function(){b||(c=a(),b=!0);return c}}(function(){var a=document.createElement("div"),b=document.createElement("div");b.appendChild(document.createElement("div"));a.appendChild(b);b=a.firstChild.firstChild;a.innerHTML=_.Wd(_.Yd);return!b.parentElement});ae=/^[\w+/_-]+[=]{0,2}$/;
_.be=function(a){a=(a||_.q).document;return a.querySelector?(a=a.querySelector('style[nonce],link[rel="stylesheet"][nonce]'))&&(a=a.nonce||a.getAttribute("nonce"))&&ae.test(a)?a:"":""};_.ce=function(a,b){this.width=a;this.height=b};_.m=_.ce.prototype;_.m.aspectRatio=function(){return this.width/this.height};_.m.Jb=function(){return!(this.width*this.height)};_.m.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};_.m.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};_.m.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};_.R=function(a,b){var c=b||document;if(c.getElementsByClassName)a=c.getElementsByClassName(a)[0];else{c=document;var d=b||c;a=d.querySelectorAll&&d.querySelector&&a?d.querySelector(a?"."+a:""):_.de(c,a,b)[0]||null}return a||null};
_.de=function(a,b,c){var d;a=c||a;if(a.querySelectorAll&&a.querySelector&&b)return a.querySelectorAll(b?"."+b:"");if(b&&a.getElementsByClassName){var e=a.getElementsByClassName(b);return e}e=a.getElementsByTagName("*");if(b){var f={};for(c=d=0;a=e[c];c++){var g=a.className;"function"==typeof g.split&&_.sa(g.split(/\s+/),b)&&(f[d++]=a)}f.length=d;return f}return e};_.fe=function(a){return _.ee(document,a)};
_.ee=function(a,b){b=String(b);"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)};_.ge=function(a){for(var b;b=a.firstChild;)a.removeChild(b)};_.he=function(a){return 9==a.nodeType?a:a.ownerDocument||a.document};
}catch(e){_._DumpException(e)}
try{
var Ee,Ge;_.ye=function(a){if(null==a)return a;if("string"===typeof a){if(!a)return;a=+a}if("number"===typeof a)return Number.isFinite(a)?a|0:void 0};_.ze=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.Ae=function(a,b,c){return void 0!==_.fb(a,b,c,!1)};_.Be=function(a,b){return _.ye(_.nc(a,b))};_.T=function(a,b){a=_.nc(a,b);return null==a?a:Number.isFinite(a)?a|0:void 0};
_.U=function(a,b,c=0){return _.gb(_.Be(a,b),c)};_.Ce=function(a,b){if(void 0!==a.i||void 0!==a.j)throw Error("v");a.j=b;_.Zc(a)};_.De=class extends _.Q{constructor(a){super(a)}};Ee=class extends _.md{};_.Fe=function(a,b){if(b in a.i)return a.i[b];throw new Ee;};Ge=0;_.He=function(a){return Object.prototype.hasOwnProperty.call(a,_.ub)&&a[_.ub]||(a[_.ub]=++Ge)};_.Ie=function(a){return _.Fe(_.jd.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 SPDX-License-Identifier: Apache-2.0
*/
var pj=function(a){return new _.oj(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.oj=class{constructor(a){this.lh=a}};_.qj=[pj("data"),pj("http"),pj("https"),pj("mailto"),pj("ftp"),new _.oj(a=>/^[^:]*([/?#]|$)/.test(a))];_.rj="function"===typeof URL;
}catch(e){_._DumpException(e)}
try{
var sj;sj={};_.tj=class{constructor(a){this.i=a}toString(){return this.i+""}};_.uj=function(a){return a instanceof _.tj&&a.constructor===_.tj?a.i:"type_error:TrustedResourceUrl"};_.vj=function(a){const b=_.Gd();a=b?b.createScriptURL(a):a;return new _.tj(a,sj)};
}catch(e){_._DumpException(e)}
try{
_.wj=function(a){var b;let c;const d=null==(c=(b=(a.ownerDocument&&a.ownerDocument.defaultView||window).document).querySelector)?void 0:c.call(b,"script[nonce]");(b=d?d.nonce||d.getAttribute("nonce")||"":"")&&a.setAttribute("nonce",b)};_.xj=function(a){if(!a)return null;a=_.G(a,4);var b;null===a||void 0===a?b=null:b=_.vj(a);return b};_.yj=class extends _.Q{constructor(a){super(a)}};_.zj=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Bj=function(a,b,c){a<b?Aj(a+1,b):_.Dc.log(Error("W`"+a+"`"+b),{url:c})},Aj=function(a,b){if(Cj){const c=_.fe("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.uj(Cj);_.wj(c);c.onerror=_.ze(Bj,a,b,c.src);_.zj("HEAD")[0].appendChild(c)}},Dj=class extends _.Q{constructor(a){super(a)}};var Ej=_.E(_.dd,Dj,17)||new Dj,Fj,Cj=(Fj=_.E(Ej,_.yj,1))?_.xj(Fj):null,Gj,Hj=(Gj=_.E(Ej,_.yj,2))?_.xj(Gj):null,Ij=function(){Aj(1,2);if(Hj){const b=_.fe("LINK");b.setAttribute("type","text/css");b.rel="stylesheet";b.href=_.uj(Hj).toString();var a=_.be(b.ownerDocument&&b.ownerDocument.defaultView);a&&b.setAttribute("nonce",a);(a=_.be())&&b.setAttribute("nonce",a);_.zj("HEAD")[0].appendChild(b)}};(function(){const a=_.ed();if(_.D(a,18))Ij();else{const b=_.Be(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Ij,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div class="gb_q" ng-non-bindable=""><div class="gb_Ec"><div>Google Account</div><div class="gb_Eb">Harsha Badisepu</div><div>harshabadisepu@gmail.com</div></div></div><script type="text/javascript" src="chrome-extension://fpjppnhnpnknbenelmbnidjbolhandnf/content_script_web_accessible/ecp_regular.js" gapi_processed="true"></script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./titanic_survival_prediction_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical colab-left-pane-open" style="position: relative;">
      <div class="top-floater"><div role="banner">
    <colab-header-skip-button><template shadowrootmode="open"><!----><a id="skiplink" class="skip-link" href="https://colab.research.google.com/drive/1e6dcDo4Ce7F16rYq84tmNkkuTZccM5ze#top-toolbar"><!--?lit$939691256$-->Skip to main content</a></template></colab-header-skip-button>
    <!--?lit$939691256$-->
    <!--?lit$939691256$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning hidden">
            <!--?lit$939691256$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1e6dcDo4Ce7F16rYq84tmNkkuTZccM5ze#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
          <mwc-icon-button class="close" icon="close" title="Close"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Close"><!--?lit$939691256$-->
    <!--?lit$939691256$--><i class="material-icons"><!--?lit$939691256$-->close</i>
    <span><slot></slot></span>
  </button></template></mwc-icon-button></div>
        

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$939691256$-->
        <!--?lit$939691256$--><div id="header-logo">
              <!--?lit$939691256$--> <!--?lit$939691256$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$939691256$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$939691256$--> <!--?lit$939691256$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" style="width: 132.462px;" aria-describedby="doc-name-tooltip"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Untitled0.ipynb_</colab-input-sizer>
            <!--?lit$939691256$-->
                  <div class="screenreader-only" id="star-status" aria-live="polite">Notebook unstarred</div>
                  <mwc-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Star"><!--?lit$939691256$-->
    <!--?lit$939691256$-->
    <span><slot></slot></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </mwc-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" style="user-select: none;" tabindex="0"><!--?lit$939691256$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$939691256$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$939691256$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$939691256$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$939691256$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$939691256$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$939691256$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$939691256$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div>
    <div id="colab-menu-cover" style="display: none;"> </div></div><!----><colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$939691256$-->All changes saved</button></template></colab-last-saved-indicator></div></div>
        <div id="header-right">
          <!--?lit$939691256$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$939691256$-->
      <!--?lit$939691256$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$939691256$--> <paper-button id="comments" command="open-comments-thread" role="button" animated="" elevation="0" aria-disabled="false" aria-describedby="comments-tooltip" tabindex="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
                <span> <!--?lit$939691256$-->Comment </span>
              </paper-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$939691256$--> <paper-button id="share-toolbar-button" command="share" role="button" animated="" elevation="0" aria-disabled="false" aria-describedby="share-toolbar-button-tooltip" tabindex="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->people</md-icon>
                <span> <!--?lit$939691256$-->Share </span>
              </paper-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$939691256$--> <mwc-icon-button id="settings-cog" command="preferences" title="Open settings"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Open settings"><!--?lit$939691256$-->
    <!--?lit$939691256$-->
    <span><slot></slot></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </mwc-icon-button>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Pa gb_ld gb_gb gb_0c" id="gb"><div class="gb_Bd gb_eb gb_qd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Ud" style="display:block"><div class="gb_6c"></div><div class="gb_b gb_w gb_3f gb_J"><div class="gb_f gb_db gb_3f gb_J"><a class="gb_d gb_Fa gb_J" aria-label="Google Account: Harsha Badisepu  
(harshabadisepu@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en-GB&amp;continue=https://colab.research.google.com/&amp;ec=GBRAqQM" tabindex="0" role="button"><img class="gb_n gbii" src="./titanic_survival_prediction_files/unnamed.png" srcset="https://lh3.googleusercontent.com/ogw/ANLem4Z3GnT3Qvm6YFjUNa0uj-1eaOR2s1YrjZ_YE_a-lA=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/ANLem4Z3GnT3Qvm6YFjUNa0uj-1eaOR2s1YrjZ_YE_a-lA=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.wd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.wd(a,b,d);else{d=(0,_.y)(a.B,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.C[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("s`"+b))}};
}catch(e){_._DumpException(e)}
try{
_.xd=function(){if(!_.q.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});try{const c=()=>{};_.q.addEventListener("test",c,b);_.q.removeEventListener("test",c,b)}catch(c){}return a}();
}catch(e){_._DumpException(e)}
try{
var yd=document.querySelector(".gb_k .gb_d"),zd=document.querySelector("#gb.gb_Wc");yd&&!zd&&_.wd(_.id,yd,"click");
}catch(e){_._DumpException(e)}
try{
_.wh=function(a){const b=[];let c=0;for(const d in a)b[c++]=a[d];return b};_.xh=function(a){if(a.o)return a.o;for(const b in a.i)if(a.i[b].ua()&&a.i[b].C())return a.i[b];return null};_.yh=function(a,b){a.i[b.K()]=b};var zh=new class extends _.Bc{constructor(){var a=_.Dc;super();this.C=a;this.o=null;this.j={};this.B={};this.i={};this.v=null}A(a){this.i[a]&&(_.xh(this)&&_.xh(this).K()==a||this.i[a].P(!0))}Za(a){this.v=a;for(const b in this.i)this.i[b].ua()&&this.i[b].Za(a)}wc(a){return a in this.i?this.i[a]:null}};_.ld("dd",zh);
}catch(e){_._DumpException(e)}
try{
_.ij=function(a,b){return _.K(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var jj=document.querySelector(".gb_b .gb_d"),kj=document.querySelector("#gb.gb_Wc");jj&&!kj&&_.wd(_.id,jj,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><div class="notebook-horizontal">
        <!--?lit$939691256$--><colab-left-pane role="complementary" aria-label="left pane" class="colab-left-pane-open"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$939691256$--><mwc-icon-button-toggle command="show-toc-pane" title="Table of contents"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex   " aria-pressed="false" aria-label="Table of contents"><!--?lit$939691256$-->
        <span class="mdc-icon-button__icon"><slot name="offIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
        <span class="mdc-icon-button__icon mdc-icon-button__icon--on"><slot name="onIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
      </button></template>
          <md-icon slot="offIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->format_list_bulleted</md-icon>
          <md-icon slot="onIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->format_list_bulleted</md-icon>
        </mwc-icon-button-toggle> <!--?lit$939691256$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$939691256$--><mwc-icon-button-toggle command="find" title="Find and replace"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex   " aria-pressed="false" aria-label="Find and replace"><!--?lit$939691256$-->
        <span class="mdc-icon-button__icon"><slot name="offIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
        <span class="mdc-icon-button__icon mdc-icon-button__icon--on"><slot name="onIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
      </button></template>
          <md-icon slot="offIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->search</md-icon>
          <md-icon slot="onIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->search</md-icon>
        </mwc-icon-button-toggle> <!--?lit$939691256$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$939691256$--><mwc-icon-button-toggle command="show-variables" title="Variables"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex   " aria-pressed="false" aria-label="Variables"><!--?lit$939691256$-->
        <span class="mdc-icon-button__icon"><slot name="offIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
        <span class="mdc-icon-button__icon mdc-icon-button__icon--on"><slot name="onIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
      </button></template>
          <md-icon slot="offIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
          <md-icon slot="onIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
        </mwc-icon-button-toggle> <!--?lit$939691256$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$939691256$--><mwc-icon-button-toggle command="open-user-secrets" title="Secrets"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex   " aria-pressed="false" aria-label="Secrets"><!--?lit$939691256$-->
            <mwc-ripple unbounded=""><template shadowrootmode="open"><!---->
        <div class="mdc-ripple-surface mdc-ripple-upgraded mdc-ripple-upgraded--unbounded" style="--mdc-ripple-fg-scale: 1.7272727272727273; --mdc-ripple-fg-size: 22px; --mdc-ripple-left: 8px; --mdc-ripple-top: 8px;"></div></template>
            </mwc-ripple>
        <span class="mdc-icon-button__icon"><slot name="offIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
        <span class="mdc-icon-button__icon mdc-icon-button__icon--on"><slot name="onIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
      </button></template>
          <md-icon slot="offIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->vpn_key</md-icon>
          <md-icon slot="onIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->vpn_key</md-icon>
        </mwc-icon-button-toggle> <!--?lit$939691256$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$939691256$--><mwc-icon-button-toggle command="show-files" title="Files" on=""><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex mdc-icon-button--on" aria-pressed="true" aria-label="Files"><!--?lit$939691256$-->
            <mwc-ripple unbounded=""><template shadowrootmode="open"><!---->
        <div class="mdc-ripple-surface mdc-ripple-upgraded mdc-ripple-upgraded--unbounded" style="--mdc-ripple-fg-scale: 1.7272727272727273; --mdc-ripple-fg-size: 22px; --mdc-ripple-left: 8px; --mdc-ripple-top: 8px;"></div></template>
            </mwc-ripple>
        <span class="mdc-icon-button__icon"><slot name="offIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
        <span class="mdc-icon-button__icon mdc-icon-button__icon--on"><slot name="onIcon"><i class="material-icons"><!--?lit$939691256$--></i></slot></span>
      </button></template>
          <md-icon slot="offIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->folder</md-icon>
          <md-icon slot="onIcon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->folder</md-icon>
        </mwc-icon-button-toggle> <!--?lit$939691256$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$939691256$--><mwc-icon-button command="snippets" title="Code snippets"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Code snippets"><!--?lit$939691256$-->
    <!--?lit$939691256$-->
    <span><slot></slot></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->code</md-icon>
        </mwc-icon-button> <!--?lit$939691256$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$939691256$--><mwc-icon-button command="show-command-palette" title="Command palette"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Command palette"><!--?lit$939691256$-->
    <!--?lit$939691256$-->
    <span><slot></slot></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <path d="M21,3H3A2,2,0,0,0,1,5V17a2,2,0,0,0,2,2H21a2,2,0,0,0,2-2V5A2,2,0,0,0,21,3Zm0,2V17H3V5"></path>
      <rect x="5" y="12" width="11" height="2"></rect>
      <rect x="5" y="8" width="11" height="2"></rect>
      <rect x="17" y="8" width="2" height="2"></rect>
      <rect x="17" y="12" width="2" height="2"></rect></svg></md-icon>
        </mwc-icon-button> <!--?lit$939691256$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$939691256$--><mwc-icon-button command="show-terminal" title="Terminal"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Terminal"><!--?lit$939691256$-->
    <!--?lit$939691256$-->
    <span><slot></slot></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->terminal</md-icon>
        </mwc-icon-button> <!--?lit$939691256$-->
      </div></div>
      </div><colab-resizer class="ew-resize">
          <div class="resizer-contents">
            <div class="colab-left-pane-header layout horizontal noshrink">
              <h3 class="left-pane-content-title">Files</h3>
              <!--?lit$939691256$--><mwc-icon-button class="colab-left-pane-move"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Move left pane to a tab"><!--?lit$939691256$-->
    <!--?lit$939691256$-->
    <span><slot></slot></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>tab</md-icon>
    </mwc-icon-button> <!--?lit$939691256$--><mwc-icon-button class="colab-left-pane-close"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Close left pane"><!--?lit$939691256$-->
            <mwc-ripple unbounded=""><template shadowrootmode="open"><!---->
        <div class="mdc-ripple-surface mdc-ripple-upgraded mdc-ripple-upgraded--unbounded" style="--mdc-ripple-fg-scale: 1.7777777777777777; --mdc-ripple-fg-size: 18px; --mdc-ripple-left: 7px; --mdc-ripple-top: 7px;"></div></template>
            </mwc-ripple>
    <!--?lit$939691256$-->
    <span><slot></slot></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </mwc-icon-button>
            </div>
            <div class="left-pane-container"><colab-file-browser class="layout vertical"><colab-file-tree><!----> <div class="file-tree-buttons">
          <paper-button class="file-upload" title="Upload to session storage" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
            <iron-icon icon="colab:file-upload"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g>
      <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm4 18H6V4h7v5h5v11zM8 15.01l1.41 1.41L11 14.84V19h2v-4.16l1.59 1.59L16 15.01 12.01 11z"></path>
    </g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
            <input type="file" multiple=""> </paper-button><paper-icon-button icon="colab:folder-refresh" title="Refresh" role="button" tabindex="0" aria-disabled="false"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g>
      <path d="M4,18V8H20v3h2V8a2,2,0,0,0-2-2H12L10,4H4A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2h9l-1-2Z"></path>
      <path d="M18,12.25A4.75,4.75,0,1,0,22.64,18H21.08a3.26,3.26,0,1,1-.76-3.25H18.5v1.5h4.25V12h-1.5v1.56A4.74,4.74,0,0,0,18,12.25Z"></path>
    </g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
          </paper-icon-button><paper-icon-button class="mount-drive-button" icon="colab:drive-folder" title="Mount Drive" role="button" tabindex="0" aria-disabled="false" style="display: inline-block;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g>
      <path d="M20,6H12L10,4H4A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H20a2,2,0,0,0,2-2V8A2,2,0,0,0,20,6ZM13.57,9.32,13,8.4l.34-.6h3.11l3.69,6.5H16.38M12.11,17l-.67,1.2h-1L9,15.42,12.72,9l2,3.46h0M19.3,18.2H12.09l.67-1.2,1.15-2h6.64l.34.6Z"></path>
    </g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
          </paper-icon-button><paper-icon-button id="hidden-files-toggle" icon="icons:visibility-off" role="button" tabindex="0" aria-disabled="false" title="Show hidden files"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M12 7c2.76 0 5 2.24 5 5 0 .65-.13 1.26-.36 1.83l2.92 2.92c1.51-1.26 2.7-2.89 3.43-4.75-1.73-4.39-6-7.5-11-7.5-1.4 0-2.74.25-3.98.7l2.16 2.16C10.74 7.13 11.35 7 12 7zM2 4.27l2.28 2.28.46.46C3.08 8.3 1.78 10.02 1 12c1.73 4.39 6 7.5 11 7.5 1.55 0 3.03-.3 4.38-.84l.42.42L19.73 22 21 20.73 3.27 3 2 4.27zM7.53 9.8l1.55 1.55c-.05.21-.08.43-.08.65 0 1.66 1.34 3 3 3 .22 0 .44-.03.65-.08l1.55 1.55c-.67.33-1.41.53-2.2.53-2.76 0-5-2.24-5-5 0-.79.2-1.53.53-2.2zm4.31-.78l3.15 3.15.02-.16c0-1.66-1.34-3-3-3l-.17.01z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
          </paper-icon-button>
        </div>
        <div class="parent-link"><div class="file-title-row">
          <!--?lit$939691256$-->
                <div class="file-icon colab-icon" style="margin-left: 0px;"></div>
              
          <iron-icon class="file-icon colab-icon" icon="colab:files-up-one-level"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g>
      <path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2zM11 13v4h-4v-4H4l5-5 5 5h-3z">
      </path>
    </g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
          <span class="file-tree-name" title="Up one level">
            <!--?lit$939691256$-->..
          </span>
          <input class="file-tree-name-input" value="..">
          <paper-icon-button class="file-item-menu" icon="icons:more-vert" role="button" tabindex="0" aria-disabled="false"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>
        </div></div>
        <div class="files-root"><colab-file-view filename="content" draggable="true"><!----><!--?lit$939691256$--><!--?--><!--?lit$939691256$-->
        <div class="child-files"><colab-file-view filename="sample_data" class="collapsed" draggable="true"><!----><!--?lit$939691256$-->
        <div class="file-title-row">
          <!--?lit$939691256$--> <iron-icon class="file-icon colab-icon directory-icon" icon="icons:arrow-drop-down" style="margin-left: 0px;"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M7 10l5 5 5-5z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template>
              </iron-icon>
          <iron-icon class="file-icon colab-icon" icon="icons:folder"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
          <span class="file-tree-name" title="sample_data">
            <!--?lit$939691256$-->sample_data
          </span>
          <input class="file-tree-name-input" value="sample_data">
          <paper-icon-button class="file-item-menu" icon="icons:more-vert" role="button" tabindex="0" aria-disabled="false"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>
        </div>
      <!--?lit$939691256$-->
        <div class="child-files"></div>
        <div class="overflow-ellipsis" title="Directory is too large to display all files." style="margin-left: 0px;">
          …
        </div>
      <!--?--></colab-file-view><colab-file-view filename="titanic.csv" draggable="true"><!----><!--?lit$939691256$-->
        <div class="file-title-row">
          <!--?lit$939691256$-->
                <div class="file-icon colab-icon" style="margin-left: 0px;"></div>
              
          <iron-icon class="file-icon colab-icon" icon="editor:insert-drive-file"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M6 2c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6H6zm7 7V3.5L18.5 9H13z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
          <span class="file-tree-name" title="titanic.csv (59.76K) 
Last modified Thu Feb 15 2024 17:59:36 GMT+0530 (India Standard Time)">
            <!--?lit$939691256$-->titanic.csv
          </span>
          <input class="file-tree-name-input" value="titanic.csv">
          <paper-icon-button class="file-item-menu" icon="icons:more-vert" role="button" tabindex="0" aria-disabled="false"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>
        </div>
      <!--?lit$939691256$--><!--?--><!--?--></colab-file-view></div>
        <div class="overflow-ellipsis" title="Directory is too large to display all files." style="margin-left: -20px;">
          …
        </div>
      <!--?--></colab-file-view></div>
        <div class="files-drag-to-upload layout horizontal">
          <iron-icon icon="icons:file-upload" class="layout noshrink"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M9 16h6v-6h4l-7-7-7 7h4zm-4 2h14v2H5z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
          <div> <!--?lit$939691256$-->Drop files to upload them to session storage. </div>
        </div>
        <div class="files-uploading"></div>
        <colab-usage-bar id="file-browser-disk-display" suffix="" label="Disk" style="display: flex;"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$939691256$-->Disk</div>
      <div class="total">
        <div usage="low" style="width:24%;"> </div>
      </div>
      <!--?lit$939691256$--><div class="suffix"><!--?lit$939691256$-->81.40 GB available</div>
    </template></colab-usage-bar>
        <colab-tooltip-trigger for="file-browser-disk-display" id="file-browser-disk-display-tooltip" aria-hidden="true"><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Disk: 26.31 GB/107.72 GB</div><!----><!--?--></template>
        </colab-tooltip-trigger></colab-file-tree></colab-file-browser></div>
          </div>
        <div class="resizer-thumb"></div></colab-resizer></colab-left-pane>
        <div class="layout vertical grow">
          <colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$939691256$-->
          <colab-toolbar-button command="insert-cell-below" id="toolbar-add-code" icon="icons:add"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-describedby="tooltip" role="button" animated="" elevation="0" tabindex="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$--><iron-icon icon="icons:add"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Insert code cell below</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
            <!--?lit$939691256$-->Code
          </colab-toolbar-button>
          <colab-toolbar-button command="add-text" id="toolbar-add-text" icon="icons:add"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-describedby="tooltip" role="button" animated="" elevation="0" tabindex="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$--><iron-icon icon="icons:add"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Add text cell</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
            <!--?lit$939691256$-->Text
          </colab-toolbar-button>
          <!--?lit$939691256$-->
        
    <!--?lit$939691256$-->
    <!--?lit$939691256$-->
    <!--?lit$939691256$-->
    <!--?lit$939691256$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$939691256$-->All changes saved</button></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$939691256$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$939691256$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$939691256$--> <colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$939691256$--> <colab-toolbar-button id="connect-icon" class="big-icon icon-okay" icon="icons:done" label="Focus the last run cell" tooltiptext="Focus the last run cell"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-label="Focus the last run cell" aria-describedby="tooltip" role="button" tabindex="0" animated="" elevation="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$--><iron-icon icon="icons:done"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="Focus the last run cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Focus the last run cell</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
        </colab-toolbar-button>
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connected to

          Python 3 Google Compute Engine backend

          

RAM: 1.05 GB/12.67 GB
Disk: 26.31 GB/107.72 GB"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-describedby="colab-connect-tooltip" role="button" animated="" elevation="0" tabindex="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$-->
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="colab-connect-tooltip" message="Connected to

          Python 3 Google Compute Engine backend

          

RAM: 1.05 GB/12.67 GB
Disk: 26.31 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Connected to</div><!----><!----><div><!--?lit$939691256$--></div><!----><!----><div><!--?lit$939691256$-->          Python 3 Google Compute Engine backend</div><!----><!----><div><!--?lit$939691256$--></div><!----><!----><div><!--?lit$939691256$-->          </div><!----><!----><div><!--?lit$939691256$--></div><!----><!----><div><!--?lit$939691256$-->RAM: 1.05 GB/12.67 GB</div><!----><!----><div><!--?lit$939691256$-->Disk: 26.31 GB/107.72 GB</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
        <!--?lit$939691256$--> <div id="connect-button-resource-display">
        <!--?lit$939691256$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$939691256$-->RAM</div>
      <!--?lit$939691256$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        <!--?lit$939691256$--><colab-usage-sparkline class="disk" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$939691256$-->Disk</div>
      <!--?lit$939691256$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
      </div>
      </colab-toolbar-button>
      <!--?lit$939691256$--> <colab-toolbar-button id="connect-dropdown" class="icon-okay" label="Additional connection options" tooltiptext="Additional connection options"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-label="Additional connection options" aria-describedby="tooltip" role="button" animated="" elevation="0" tabindex="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$-->
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="Additional connection options" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
      <md-icon id="connect-dropdown-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
    </colab-toolbar-button><!--?--></template> </colab-connect-button>
    <!--?lit$939691256$--> <span class="colab-separator"></span>
          <colab-toolbar-button command="show-chat" icon="colab:supervised_user_circle"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-describedby="tooltip" role="button" animated="" elevation="0" tabindex="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$--><iron-icon icon="colab:supervised_user_circle"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g>
      <!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$-->
      <path d="M 9.9582499,21.35987 C 10.842594,19.382021 12.606506,17.817985 14.716516,17.279566 16.41989,16.686126 18.317872,16.656934 20.03281,17.22182 22.44796,13.614773 22.030038,8.3464205 18.90388,5.2829204 15.571823,1.7178775 9.420202,1.3974701 5.769982,4.6587762 3.3377473,6.6864955 2.0387092,9.9509867 2.4603251,13.095093 c 0.1463132,1.333314 0.5764246,2.646122 1.3212592,3.766896 2.6970808,-1.363945 5.949002,-1.659216 8.8152407,-0.659689 -1.241623,0.378685 -1.898774,2.052201 -3.36112,1.793886 -1.3568211,-0.0051 -2.7332571,0.237474 -3.9549301,0.844871 1.267179,1.273083 2.9115843,2.175024 4.677475,2.518813 z m 2.0388991,2.638757 C 6.6511222,24.107652 1.5826283,20.137336 0.35384605,14.940954 -0.87900818,10.201889 1.1156845,4.8167637 5.2106158,2.1027623 9.1389196,-0.63068336 14.72247,-0.71788883 18.666809,2.0315664 c 3.770731,2.4797903 5.923366,7.1940181 5.205845,11.6657356 -0.561363,4.25325 -3.592409,8.039095 -7.614261,9.524313 -1.356179,0.518542 -2.808321,0.792183 -4.261244,0.777012 z M 8.9987675,13.80343 C 6.3557134,13.92683 4.1587181,11.059046 4.9242904,8.5324696 5.5067387,6.0598075 8.5843425,4.6198007 10.844905,5.8135307 c 2.251036,1.0498371 3.121931,4.2263483 1.586973,6.2196153 -0.777226,1.086407 -2.083619,1.810868 -3.4331105,1.770284 z m 0,-2.39887 C 10.82036,11.536018 11.503688,8.682573 9.8022883,7.9757151 8.3387516,7.206114 6.5439498,8.9550798 7.3889517,10.413062 c 0.2986856,0.592673 0.9351214,1.021277 1.6098158,0.991498 z m 8.3954675,3.598305 c -2.036107,0.118847 -3.612999,-2.238286 -2.81499,-4.095085 0.678013,-1.9105614 3.4227,-2.5652777 4.869242,-1.1247834 1.400594,1.2764214 1.220774,3.8379454 -0.469812,4.7846484 -0.472701,0.291047 -1.028762,0.44763 -1.58444,0.43522 z"></path></svg>
    </g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$--></div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
            <!--?lit$939691256$-->Colab AI
          </colab-toolbar-button>
    <!--?lit$939691256$-->
    <span class="collapsed-options">
      <!--?lit$939691256$--><span class="colab-separator"></span>
      <!--?lit$939691256$--> <paper-icon-button command="share" icon="social:people" alt="Share notebook" role="button" aria-disabled="false" aria-label="Share notebook" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt="Share notebook"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
          </paper-icon-button><paper-icon-button command="preferences" icon="icons:settings" title="Open settings" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19.43 12.98c.04-.32.07-.64.07-.98s-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.12-.22-.39-.3-.61-.22l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65C14.46 2.18 14.25 2 14 2h-4c-.25 0-.46.18-.49.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.23-.09-.49 0-.61.22l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98s.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.12.22.39.3.61.22l2.49-1c.52.4 1.08.73 1.69.98l.38 2.65c.03.24.24.42.49.42h4c.25 0 .46-.18.49-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.23.09.49 0 .61-.22l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zM12 15.5c-1.93 0-3.5-1.57-3.5-3.5s1.57-3.5 3.5-3.5 3.5 1.57 3.5 3.5-1.57 3.5-3.5 3.5z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
      </paper-icon-button>
    </span>
    <span class="colab-separator"></span>
    <paper-icon-button command="toggle-header" id="toggle-header-button" icon="icons:expand-less" aria-label="Toggle header visibility" role="button" aria-disabled="false" aria-describedby="toggle-header-button-tooltip" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M12 8l-6 6 1.41 1.41L12 10.83l4.59 4.58L18 14z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
    </paper-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger></colab-notebook-toolbar><colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$939691256$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$939691256$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <paper-tabs selected="0" noink="" class="layout grow" scrollable="" role="tablist" dir="null" tabindex="0"><template shadowrootmode="open"><style scope="paper-tabs">:host {
  display: var(--layout_-_display);
        -ms-flex-align: var(--layout-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center_-_-webkit-align-items); align-items: var(--layout-center_-_align-items);

        height: 48px;
        font-size: 14px;
        font-weight: 500;
        overflow: hidden;
        -moz-user-select: none;
        -ms-user-select: none;
        -webkit-user-select: none;
        user-select: none;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        ;
}

:host([dir="rtl"]) {
  display: var(--layout-horizontal-reverse_-_display); -ms-flex-direction: var(--layout-horizontal-reverse_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal-reverse_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal-reverse_-_flex-direction);
}

#tabsContainer {
  position: relative;
        height: 100%;
        white-space: nowrap;
        overflow: hidden;
        -ms-flex: var(--layout-flex-auto_-_-ms-flex); -webkit-flex: var(--layout-flex-auto_-_-webkit-flex); flex: var(--layout-flex-auto_-_flex);
        ;
}

#tabsContent {
  height: 100%;
        -moz-flex-basis: auto;
        -ms-flex-basis: auto;
        flex-basis: auto;
        ;
}

#tabsContent.scrollable {
  position: absolute;
        white-space: nowrap;
}

#tabsContent:not(.scrollable), #tabsContent.scrollable.fit-container {
  display: var(--layout-horizontal_-_display); -ms-flex-direction: var(--layout-horizontal_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal_-_flex-direction);
}

#tabsContent.scrollable.fit-container {
  min-width: 100%;
}

#tabsContent.scrollable.fit-container > ::slotted(*) {
  -ms-flex: 1 0 auto;
        -webkit-flex: 1 0 auto;
        flex: 1 0 auto;
}

.hidden {
  display: none;
}

.not-visible {
  opacity: 0;
        cursor: default;
}

paper-icon-button {
  width: 48px;
        height: 48px;
        padding: 12px;
        margin: 0 4px;
        background-color: var(--paper-icon-buttons_-_background-color); border-radius: var(--paper-icon-buttons_-_border-radius); color: var(--paper-icon-buttons_-_color); height: var(--paper-icon-buttons_-_height, 48px); padding: var(--paper-icon-buttons_-_padding, 12px); position: var(--paper-icon-buttons_-_position); width: var(--paper-icon-buttons_-_width, 48px)
}

paper-icon-button#left {
  left: var(--paper-icon-button-left_-_left); z-index: var(--paper-icon-button-left_-_z-index)
}

paper-icon-button#right {
  right: var(--paper-icon-button-right_-_right)
}

#selectionBar {
  position: absolute;
        height: 0;
        bottom: 0;
        left: 0;
        right: 0;
        border-bottom: 2px solid var(--paper-tabs-selection-bar-color, var(--paper-yellow-a100));
          -webkit-transform: scale(0);
        transform: scale(0);
          -webkit-transform-origin: left center;
        transform-origin: left center;
          transition: -webkit-transform;
        transition: transform;

        z-index: var(--paper-tabs-selection-bar_-_z-index);
}

#selectionBar.align-bottom {
  top: 0;
        bottom: auto;
}

#selectionBar.expand {
  transition-duration: 0.15s;
        transition-timing-function: cubic-bezier(0.4, 0.0, 1, 1);
}

#selectionBar.contract {
  transition-duration: 0.18s;
        transition-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1);
}

#tabsContent > ::slotted(:not(#selectionBar)) {
  height: 100%;
}</style>
    

    <paper-icon-button id="left" icon="paper-tabs:chevron-left" class="not-visible" aria-hidden="true" role="button" aria-disabled="true" aria-label="" disabled="" tabindex="-1" style="pointer-events: none;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt=""><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>

    <div id="tabsContainer" style="touch-action: pan-y;">
      <div id="tabsContent" class="scrollable">
        <div id="selectionBar" class="" style="transform: translateX(0%) scaleX(0);"></div>
        <slot></slot>
      </div>
    </div>

    <paper-icon-button id="right" icon="paper-tabs:chevron-right" class="not-visible" aria-hidden="true" role="button" aria-disabled="true" aria-label="" disabled="" tabindex="-1" style="pointer-events: none;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt=""><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>
</template>
      <paper-tab noink="" title="" aria-labelledby="tab-title-mHko_MGlvgH9" class="iron-selected" role="tab" aria-disabled="false" aria-selected="true" tabindex="0"><template shadowrootmode="open"><style scope="paper-tab">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center_-_-webkit-align-items); align-items: var(--layout-center_-_align-items);
        -ms-flex-pack: var(--layout-center-justified_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-justified_-_-webkit-justify-content); justify-content: var(--layout-center-justified_-_justify-content);
        -ms-flex: var(--layout-flex-auto_-_-ms-flex); -webkit-flex: var(--layout-flex-auto_-_-webkit-flex); flex: var(--layout-flex-auto_-_flex);

        position: relative;
        padding: 0 12px;
        overflow: hidden;
        cursor: pointer;
        vertical-align: middle;

        font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
        ;
}

:host(:focus) {
  outline: none;
}

:host([link]) {
  padding: 0;
}

.tab-content {
  height: 100%;
        transform: translateZ(0);
          -webkit-transform: translateZ(0);
        transition: opacity 0.1s cubic-bezier(0.4, 0.0, 1, 1);
        display: var(--layout-horizontal_-_display); -ms-flex-direction: var(--layout-horizontal_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal_-_flex-direction);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        -ms-flex: var(--layout-flex-auto_-_-ms-flex); -webkit-flex: var(--layout-flex-auto_-_-webkit-flex); flex: var(--layout-flex-auto_-_flex);
        ;
}

:host(:not(.iron-selected)) > .tab-content {
  opacity: 0.8;

        ;
}

:host(:focus) .tab-content {
  opacity: 1;
        font-weight: 700;

        background-color: var(--paper-tab-content-focused_-_background-color); font-weight: var(--paper-tab-content-focused_-_font-weight, 700); background: var(--paper-tab-content-focused_-_background);
}

paper-ripple {
  color: var(--paper-tab-ink, var(--paper-yellow-a100));
}

.tab-content > ::slotted(a) {
  -ms-flex: var(--layout-flex-auto_-_-ms-flex); -webkit-flex: var(--layout-flex-auto_-_-webkit-flex); flex: var(--layout-flex-auto_-_flex);

        height: 100%;
}</style>
    

    <div class="tab-content">
      <slot></slot>
    </div>
</template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-mHko_MGlvgH9"><!--?lit$939691256$--><!--?lit$939691256$-->Notebook<!--?--></span>
            <!--?lit$939691256$-->
          </div>
        </paper-tab></paper-tabs>
      <!--?lit$939691256$--> <paper-icon-button icon="icons:more-horiz" title="Show more" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M6 10c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm12 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-6 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
  </paper-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content iron-selected"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" role="main" class="notebook-container" aria-label="Notebook" tabindex="-1">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$939691256$-->
              <div class="notebook-content ">
                <!--?lit$939691256$--><div class="add-cell">
      <div class="add-cell-buttons">
        <colab-toolbar-button class="add-code add-button" icon="icons:add" title="Add code cell
Ctrl+M B"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-describedby="tooltip" role="button" tabindex="0" animated="" elevation="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$--><iron-icon icon="icons:add"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$--></div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
          <!--?lit$939691256$-->Code
        </colab-toolbar-button>
        <colab-toolbar-button class="add-text add-button" icon="icons:add" title="Add text cell"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-describedby="tooltip" role="button" tabindex="0" animated="" elevation="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$--><iron-icon icon="icons:add"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$--></div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
          <!--?lit$939691256$-->Text
        </colab-toolbar-button>
        <!--?lit$939691256$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code icon-scrolling focused code-has-output" id="cell-hO2Ns0tSvgHt" role="region" aria-label="Cell 0: Code cell: " style="" tabindex="-1"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----> <paper-icon-button class="colab-icon" noink="" icon="icons:arrow-upward" title="Move cell up
Ctrl+M K" command="move-cell-up" role="button" aria-disabled="true" disabled="" style="pointer-events: none;" tabindex="-1"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
        </paper-icon-button><!----><!----> <paper-icon-button class="colab-icon" noink="" icon="icons:arrow-downward" title="Move cell down
Ctrl+M J" command="move-cell-down" role="button" aria-disabled="true" disabled="" style="pointer-events: none;" tabindex="-1"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
        </paper-icon-button><!----><!----> <paper-icon-button class="colab-icon" noink="" icon="icons:link" title="Copy link to cell" command="copy-link-to-cell" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
        </paper-icon-button><!----><!----> <paper-icon-button class="colab-icon" noink="" icon="editor:insert-comment" title="Add a comment
Ctrl+Alt+M" command="add-comment" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M20 2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14l4 4V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
        </paper-icon-button><!----><!----> <paper-icon-button class="colab-icon" noink="" icon="icons:settings" title="Open editor settings" command="editor-preferences" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19.43 12.98c.04-.32.07-.64.07-.98s-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.12-.22-.39-.3-.61-.22l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65C14.46 2.18 14.25 2 14 2h-4c-.25 0-.46.18-.49.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.23-.09-.49 0-.61.22l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98s.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.12.22.39.3.61.22l2.49-1c.52.4 1.08.73 1.69.98l.38 2.65c.03.24.24.42.49.42h4c.25 0 .46-.18.49-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.23.09.49 0 .61-.22l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zM12 15.5c-1.93 0-3.5-1.57-3.5-3.5s1.57-3.5 3.5-3.5 3.5 1.57 3.5 3.5-1.57 3.5-3.5 3.5z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
        </paper-icon-button><!----><!----> <paper-icon-button class="colab-icon" noink="" icon="editor:mode-edit" title="Edit" command="toggle-edit-markdown" role="button" aria-disabled="false" style="display: none;" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
        </paper-icon-button><!----><!----> <paper-icon-button class="colab-icon" noink="" icon="colab:mirror-cell" title="Mirror cell in tab" command="mirror-cell-in-tab" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g>
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
        </paper-icon-button><!----><!----> <paper-icon-button class="colab-icon" noink="" icon="icons:delete" title="Delete cell
Ctrl+M D" command="delete-cell-or-selection" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
        </paper-icon-button><!----><!--?lit$939691256$--><paper-icon-button noink="" icon="icons:more-vert" title="More cell actions" class="colab-icon cell-toolbar-more" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
    </paper-icon-button><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button title="Run cell (Ctrl+Enter)
cell executed since last change

executed by Harsha Badisepu
18:26 (1 minute ago)
executed in 0.4 s" role="button" aria-label="Run cell"><template shadowrootmode="open"><!----> <div class="cell-execution focused">
      <div class="execution-count"><!--?lit$939691256$-->[17]</div>
      <div class="cell-execution-indicator"> <!--?lit$939691256$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$939691256$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg> </div>
      <!--?lit$939691256$--><div id="status">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$939691256$-->0s</div>
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="1" data-mode-id="notebook-python" style="height: 1093px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/3" style="width: 1110px; height: 1093px;"><div data-mprt="3" class="overflow-guard" style="width: 1110px; height: 1093px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 1093px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 1093px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 1093px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1104px; height: 1093px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1093px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1104px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"><div class="current-line" style="width:1104px; height:19px;"></div><div class="cdr bracket-match" style="left:38px;width:8px;height:19px;"></div><div class="cdr bracket-match" style="left:277px;width:8px;height:19px;"></div></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 1093px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1104px; height: 1093px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;pd</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.model_selection&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;train_test_split</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.linear_model&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;LogisticRegression</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk18">from</span><span class="mtk1">&nbsp;sklearn.metrics&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;accuracy_score</span><span class="mtk12">,</span><span class="mtk1">&nbsp;classification_report</span><span class="mtk12">,</span><span class="mtk1">&nbsp;confusion_matrix</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Load&nbsp;the&nbsp;dataset</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk1">titanic_data&nbsp;=&nbsp;pd.read_csv</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">'titanic.csv'</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Handle&nbsp;missing&nbsp;values</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">titanic_data</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk5">'Age'</span><span class="mtk12 bracket-highlighting-0">]</span><span class="mtk1">.fillna</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">titanic_data</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Age'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk1">.median</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12">,</span><span class="mtk1">&nbsp;inplace=</span><span class="mtk9">True</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">titanic_data</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk5">'Embarked'</span><span class="mtk12 bracket-highlighting-0">]</span><span class="mtk1">.fillna</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">titanic_data</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Embarked'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk1">.mode</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk6">0</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk12">,</span><span class="mtk1">&nbsp;inplace=</span><span class="mtk9">True</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Select&nbsp;features&nbsp;and&nbsp;target&nbsp;variable</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;titanic_data</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Age'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Sex'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Pclass'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Fare'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk12 bracket-highlighting-0">]</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">y&nbsp;=&nbsp;titanic_data</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk5">'Survived'</span><span class="mtk12 bracket-highlighting-0">]</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Convert&nbsp;categorical&nbsp;variables&nbsp;into&nbsp;numerical&nbsp;one</span><span class="mtk8">s</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;pd.get_dummies</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">X</span><span class="mtk12">,</span><span class="mtk1">&nbsp;columns=</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Sex'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk12">,</span><span class="mtk1">&nbsp;drop_first=</span><span class="mtk9">True</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Split&nbsp;the&nbsp;data</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk1">X_train</span><span class="mtk12">,</span><span class="mtk1">&nbsp;X_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_train</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_test&nbsp;=&nbsp;train_test_split</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">X</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y</span><span class="mtk12">,</span><span class="mtk1">&nbsp;test_size=</span><span class="mtk6">0.2</span><span class="mtk12">,</span><span class="mtk1">&nbsp;random_state=</span><span class="mtk6">42</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Model&nbsp;Building</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">model&nbsp;=&nbsp;LogisticRegression</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">model.fit</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">X_train</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_train</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Model&nbsp;Evaluation</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk1">y_pred&nbsp;=&nbsp;model.predict</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">X_test</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"Accuracy:"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;accuracy_score</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_pred</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"Classification&nbsp;Report:"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">classification_report</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_pred</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"Confusion&nbsp;Matrix:"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">confusion_matrix</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk1">y_test</span><span class="mtk12">,</span><span class="mtk1">&nbsp;y_pred</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Predict&nbsp;survival&nbsp;status&nbsp;for&nbsp;each&nbsp;passenger&nbsp;in&nbsp;th</span><span class="mtk8">e&nbsp;test&nbsp;set</span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk1">test_predictions&nbsp;=&nbsp;pd.DataFrame</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk12 bracket-highlighting-1">{</span><span class="mtk5">'PassengerId'</span><span class="mtk12">:</span><span class="mtk1">&nbsp;titanic_data.loc</span><span class="mtk12 bracket-highlighting-2">[</span><span class="mtk1">X_test.index</span><span class="mtk12 bracket-highlighting-2">]</span><span class="mtk12 bracket-highlighting-2">[</span><span class="mtk5">'PassengerId'</span><span class="mtk12 bracket-highlighting-2">]</span><span class="mtk12">,</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'Survived'</span><span class="mtk12">:</span><span class="mtk1">&nbsp;y_pred</span><span class="mtk12 bracket-highlighting-1">}</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"\nPredicted&nbsp;survival&nbsp;status&nbsp;for&nbsp;each&nbsp;passenger&nbsp;in</span><span class="mtk5">&nbsp;the&nbsp;test&nbsp;set:"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">test_predictions</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Filter&nbsp;rows&nbsp;for&nbsp;passengers&nbsp;who&nbsp;survived</span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span class="mtk1">survived_passengers&nbsp;=&nbsp;titanic_data</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk1">titanic_data</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Survived'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk1">&nbsp;==&nbsp;</span><span class="mtk6">1</span><span class="mtk12 bracket-highlighting-0">]</span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Filter&nbsp;rows&nbsp;for&nbsp;passengers&nbsp;who&nbsp;did&nbsp;not&nbsp;survive</span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span class="mtk1">not_survived_passengers&nbsp;=&nbsp;titanic_data</span><span class="mtk12 bracket-highlighting-0">[</span><span class="mtk1">titanic_data</span><span class="mtk12 bracket-highlighting-1">[</span><span class="mtk5">'Survived'</span><span class="mtk12 bracket-highlighting-1">]</span><span class="mtk1">&nbsp;==&nbsp;</span><span class="mtk6">0</span><span class="mtk12 bracket-highlighting-0">]</span></span></div><div style="top:874px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:893px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Display&nbsp;the&nbsp;first&nbsp;few&nbsp;rows&nbsp;of&nbsp;each</span></span></div><div style="top:912px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"\nPassengers&nbsp;who&nbsp;survived:"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:931px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">survived_passengers.head</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:950px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:969px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk5">"\nPassengers&nbsp;who&nbsp;did&nbsp;not&nbsp;survive:"</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:988px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk12 bracket-highlighting-0">(</span><span class="mtk1">not_survived_passengers.head</span><span class="mtk12 bracket-highlighting-1">(</span><span class="mtk12 bracket-highlighting-1">)</span><span class="mtk12 bracket-highlighting-0">)</span></span></div><div style="top:1007px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1026px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1045px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1064px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 1104px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 988px; left: 285px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1090px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1090px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="1366" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 1093px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 1093px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 1093px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1110px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 988px; left: 6px; width: 1110px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 1110px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 1093px;"><div class="minimap-shadow-hidden" style="height: 1093px;"></div><canvas width="0" height="1366" style="position: absolute; left: 0px; width: 0px; height: 1093px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="1366" style="position: absolute; left: 0px; width: 0px; height: 1093px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1536px; top: 310.2px; left: 676.4px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal disabled" style="top: 8px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" style="width: 0px; height: 0px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 732.6px; max-height: 273.25px; width: 0px; height: 0px;"><div class="hover-row"><div class="marker hover-contents" style="font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px;"><span style="white-space: pre-wrap;">IndentationError: unexpected indent</span></div></div><div class="hover-row status-bar"><div class="actions"><div class="action-container" tabindex="0"><a class="action" role="button"><span>View Problem (Alt+F8)</span></a></div><div>No quick fixes available</div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 0px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 0px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 0px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output"><!----> <div class="output-header"> </div>
        <div class="output-content" style="">
          <div class="output-info"><colab-output-info title="Clear output

executed by Harsha Badisepu
18:26 (0 minutes ago)
executed in 0.4 s" hovering=""><template shadowrootmode="open"><!----> <md-icon class="collaborator output" alt="Execution output" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->output</md-icon>
      <!--?lit$939691256$--> <mwc-icon-button icon="cancel" command="clear-focused-or-selected-outputs" alt="Clear output"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="cancel"><!--?lit$939691256$-->
    <!--?lit$939691256$--><i class="material-icons"><!--?lit$939691256$-->cancel</i>
    <span><slot></slot></span>
  </button></template>
          </mwc-icon-button><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-1 output_text"><pre>Accuracy: 0.8044692737430168
Classification Report:
              precision    recall  f1-score   support

           0       0.82      0.86      0.84       105
           1       0.78      0.73      0.76        74

    accuracy                           0.80       179
   macro avg       0.80      0.79      0.80       179
weighted avg       0.80      0.80      0.80       179

Confusion Matrix:
[[90 15]
 [20 54]]

Predicted survival status for each passenger in the test set:
     PassengerId  Survived
709          710         0
439          440         0
840          841         0
720          721         1
39            40         1
..           ...       ...
433          434         0
773          774         0
25            26         1
84            85         1
10            11         1

[179 rows x 2 columns]

Passengers who survived:
   PassengerId  Survived  Pclass  \
1            2         1       1   
2            3         1       3   
3            4         1       1   
8            9         1       3   
9           10         1       2   

                                                Name     Sex   Age  SibSp  \
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
8  Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)  female  27.0      0   
9                Nasser, Mrs. Nicholas (Adele Achem)  female  14.0      1   

   Parch            Ticket     Fare Cabin Embarked  
1      0          PC 17599  71.2833   C85        C  
2      0  STON/O2. 3101282   7.9250   NaN        S  
3      0            113803  53.1000  C123        S  
8      2            347742  11.1333   NaN        S  
9      0            237736  30.0708   NaN        C  

Passengers who did not survive:
   PassengerId  Survived  Pclass                            Name   Sex   Age  \
0            1         0       3         Braund, Mr. Owen Harris  male  22.0   
4            5         0       3        Allen, Mr. William Henry  male  35.0   
5            6         0       3                Moran, Mr. James  male  28.0   
6            7         0       1         McCarthy, Mr. Timothy J  male  54.0   
7            8         0       3  Palsson, Master. Gosta Leonard  male   2.0   

   SibSp  Parch     Ticket     Fare Cabin Embarked  
0      1      0  A/5 21171   7.2500   NaN        S  
4      0      0     373450   8.0500   NaN        S  
5      0      0     330877   8.4583   NaN        Q  
6      0      0      17463  51.8625   E46        S  
7      3      1     349909  21.0750   NaN        S  
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <colab-toolbar-button class="add-code add-button" icon="icons:add" title="Add code cell
Ctrl+M B"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-describedby="tooltip" role="button" tabindex="0" animated="" elevation="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$--><iron-icon icon="icons:add"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$--></div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
          <!--?lit$939691256$-->Code
        </colab-toolbar-button>
        <colab-toolbar-button class="add-text add-button" icon="icons:add" title="Add text cell"><template shadowrootmode="open"><!---->
      <paper-button id="button" aria-disabled="false" aria-describedby="tooltip" role="button" tabindex="0" animated="" elevation="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
        <!--?lit$939691256$--><iron-icon icon="icons:add"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon>
        <span class="button-content"><slot></slot></span>
      </paper-button>
      <colab-tooltip-trigger for="button" offset="7" aria-hidden="true" id="tooltip" message="" shortcut=""><template shadowrootmode="open"><!----><!--?lit$939691256$--><!----><div><!--?lit$939691256$--></div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </template>
          <!--?lit$939691256$-->Text
        </colab-toolbar-button>
        <!--?lit$939691256$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <div class="sidebar" style="display: none;"></div></div>
          <!--?lit$939691256$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$939691256$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$939691256$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -2px inset;"></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$939691256$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <paper-tabs selected="0" noink="" class="layout grow" scrollable="" role="tablist" dir="null" tabindex="0"><template shadowrootmode="open"><style scope="paper-tabs">:host {
  display: var(--layout_-_display);
        -ms-flex-align: var(--layout-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center_-_-webkit-align-items); align-items: var(--layout-center_-_align-items);

        height: 48px;
        font-size: 14px;
        font-weight: 500;
        overflow: hidden;
        -moz-user-select: none;
        -ms-user-select: none;
        -webkit-user-select: none;
        user-select: none;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        ;
}

:host([dir="rtl"]) {
  display: var(--layout-horizontal-reverse_-_display); -ms-flex-direction: var(--layout-horizontal-reverse_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal-reverse_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal-reverse_-_flex-direction);
}

#tabsContainer {
  position: relative;
        height: 100%;
        white-space: nowrap;
        overflow: hidden;
        -ms-flex: var(--layout-flex-auto_-_-ms-flex); -webkit-flex: var(--layout-flex-auto_-_-webkit-flex); flex: var(--layout-flex-auto_-_flex);
        ;
}

#tabsContent {
  height: 100%;
        -moz-flex-basis: auto;
        -ms-flex-basis: auto;
        flex-basis: auto;
        ;
}

#tabsContent.scrollable {
  position: absolute;
        white-space: nowrap;
}

#tabsContent:not(.scrollable), #tabsContent.scrollable.fit-container {
  display: var(--layout-horizontal_-_display); -ms-flex-direction: var(--layout-horizontal_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal_-_flex-direction);
}

#tabsContent.scrollable.fit-container {
  min-width: 100%;
}

#tabsContent.scrollable.fit-container > ::slotted(*) {
  -ms-flex: 1 0 auto;
        -webkit-flex: 1 0 auto;
        flex: 1 0 auto;
}

.hidden {
  display: none;
}

.not-visible {
  opacity: 0;
        cursor: default;
}

paper-icon-button {
  width: 48px;
        height: 48px;
        padding: 12px;
        margin: 0 4px;
        background-color: var(--paper-icon-buttons_-_background-color); border-radius: var(--paper-icon-buttons_-_border-radius); color: var(--paper-icon-buttons_-_color); height: var(--paper-icon-buttons_-_height, 48px); padding: var(--paper-icon-buttons_-_padding, 12px); position: var(--paper-icon-buttons_-_position); width: var(--paper-icon-buttons_-_width, 48px)
}

paper-icon-button#left {
  left: var(--paper-icon-button-left_-_left); z-index: var(--paper-icon-button-left_-_z-index)
}

paper-icon-button#right {
  right: var(--paper-icon-button-right_-_right)
}

#selectionBar {
  position: absolute;
        height: 0;
        bottom: 0;
        left: 0;
        right: 0;
        border-bottom: 2px solid var(--paper-tabs-selection-bar-color, var(--paper-yellow-a100));
          -webkit-transform: scale(0);
        transform: scale(0);
          -webkit-transform-origin: left center;
        transform-origin: left center;
          transition: -webkit-transform;
        transition: transform;

        z-index: var(--paper-tabs-selection-bar_-_z-index);
}

#selectionBar.align-bottom {
  top: 0;
        bottom: auto;
}

#selectionBar.expand {
  transition-duration: 0.15s;
        transition-timing-function: cubic-bezier(0.4, 0.0, 1, 1);
}

#selectionBar.contract {
  transition-duration: 0.18s;
        transition-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1);
}

#tabsContent > ::slotted(:not(#selectionBar)) {
  height: 100%;
}</style>
    

    <paper-icon-button id="left" icon="paper-tabs:chevron-left" class="not-visible" aria-hidden="true" role="button" aria-disabled="true" aria-label="" disabled="" tabindex="-1" style="pointer-events: none;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt=""><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>

    <div id="tabsContainer" style="touch-action: pan-y;">
      <div id="tabsContent" class="scrollable">
        <div id="selectionBar" class="" style="transform: translateX(0%) scaleX(0);"></div>
        <slot></slot>
      </div>
    </div>

    <paper-icon-button id="right" icon="paper-tabs:chevron-right" class="not-visible" aria-hidden="true" role="button" aria-disabled="true" aria-label="" disabled="" tabindex="-1" style="pointer-events: none;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt=""><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>
</template>
      </paper-tabs>
      <!--?lit$939691256$--> <paper-icon-button icon="icons:more-horiz" title="Show more" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M6 10c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm12 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-6 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
  </paper-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$939691256$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$939691256$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <paper-tabs selected="0" noink="" class="layout grow" scrollable="" role="tablist" dir="null" tabindex="0"><template shadowrootmode="open"><style scope="paper-tabs">:host {
  display: var(--layout_-_display);
        -ms-flex-align: var(--layout-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center_-_-webkit-align-items); align-items: var(--layout-center_-_align-items);

        height: 48px;
        font-size: 14px;
        font-weight: 500;
        overflow: hidden;
        -moz-user-select: none;
        -ms-user-select: none;
        -webkit-user-select: none;
        user-select: none;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        ;
}

:host([dir="rtl"]) {
  display: var(--layout-horizontal-reverse_-_display); -ms-flex-direction: var(--layout-horizontal-reverse_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal-reverse_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal-reverse_-_flex-direction);
}

#tabsContainer {
  position: relative;
        height: 100%;
        white-space: nowrap;
        overflow: hidden;
        -ms-flex: var(--layout-flex-auto_-_-ms-flex); -webkit-flex: var(--layout-flex-auto_-_-webkit-flex); flex: var(--layout-flex-auto_-_flex);
        ;
}

#tabsContent {
  height: 100%;
        -moz-flex-basis: auto;
        -ms-flex-basis: auto;
        flex-basis: auto;
        ;
}

#tabsContent.scrollable {
  position: absolute;
        white-space: nowrap;
}

#tabsContent:not(.scrollable), #tabsContent.scrollable.fit-container {
  display: var(--layout-horizontal_-_display); -ms-flex-direction: var(--layout-horizontal_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal_-_flex-direction);
}

#tabsContent.scrollable.fit-container {
  min-width: 100%;
}

#tabsContent.scrollable.fit-container > ::slotted(*) {
  -ms-flex: 1 0 auto;
        -webkit-flex: 1 0 auto;
        flex: 1 0 auto;
}

.hidden {
  display: none;
}

.not-visible {
  opacity: 0;
        cursor: default;
}

paper-icon-button {
  width: 48px;
        height: 48px;
        padding: 12px;
        margin: 0 4px;
        background-color: var(--paper-icon-buttons_-_background-color); border-radius: var(--paper-icon-buttons_-_border-radius); color: var(--paper-icon-buttons_-_color); height: var(--paper-icon-buttons_-_height, 48px); padding: var(--paper-icon-buttons_-_padding, 12px); position: var(--paper-icon-buttons_-_position); width: var(--paper-icon-buttons_-_width, 48px)
}

paper-icon-button#left {
  left: var(--paper-icon-button-left_-_left); z-index: var(--paper-icon-button-left_-_z-index)
}

paper-icon-button#right {
  right: var(--paper-icon-button-right_-_right)
}

#selectionBar {
  position: absolute;
        height: 0;
        bottom: 0;
        left: 0;
        right: 0;
        border-bottom: 2px solid var(--paper-tabs-selection-bar-color, var(--paper-yellow-a100));
          -webkit-transform: scale(0);
        transform: scale(0);
          -webkit-transform-origin: left center;
        transform-origin: left center;
          transition: -webkit-transform;
        transition: transform;

        z-index: var(--paper-tabs-selection-bar_-_z-index);
}

#selectionBar.align-bottom {
  top: 0;
        bottom: auto;
}

#selectionBar.expand {
  transition-duration: 0.15s;
        transition-timing-function: cubic-bezier(0.4, 0.0, 1, 1);
}

#selectionBar.contract {
  transition-duration: 0.18s;
        transition-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1);
}

#tabsContent > ::slotted(:not(#selectionBar)) {
  height: 100%;
}</style>
    

    <paper-icon-button id="left" icon="paper-tabs:chevron-left" class="not-visible" aria-hidden="true" role="button" aria-disabled="true" aria-label="" disabled="" tabindex="-1" style="pointer-events: none;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt=""><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>

    <div id="tabsContainer" style="touch-action: pan-y;">
      <div id="tabsContent" class="scrollable">
        <div id="selectionBar" class="" style="transform: translateX(0%) scaleX(0);"></div>
        <slot></slot>
      </div>
    </div>

    <paper-icon-button id="right" icon="paper-tabs:chevron-right" class="not-visible" aria-hidden="true" role="button" aria-disabled="true" aria-label="" disabled="" tabindex="-1" style="pointer-events: none;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt=""><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>
</template>
      </paper-tabs>
      <!--?lit$939691256$--> <paper-icon-button icon="icons:more-horiz" title="Show more" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M6 10c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm12 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-6 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
  </paper-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$939691256$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <paper-tabs selected="0" noink="" class="layout grow" scrollable="" role="tablist" dir="null" tabindex="0"><template shadowrootmode="open"><style scope="paper-tabs">:host {
  display: var(--layout_-_display);
        -ms-flex-align: var(--layout-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center_-_-webkit-align-items); align-items: var(--layout-center_-_align-items);

        height: 48px;
        font-size: 14px;
        font-weight: 500;
        overflow: hidden;
        -moz-user-select: none;
        -ms-user-select: none;
        -webkit-user-select: none;
        user-select: none;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        ;
}

:host([dir="rtl"]) {
  display: var(--layout-horizontal-reverse_-_display); -ms-flex-direction: var(--layout-horizontal-reverse_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal-reverse_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal-reverse_-_flex-direction);
}

#tabsContainer {
  position: relative;
        height: 100%;
        white-space: nowrap;
        overflow: hidden;
        -ms-flex: var(--layout-flex-auto_-_-ms-flex); -webkit-flex: var(--layout-flex-auto_-_-webkit-flex); flex: var(--layout-flex-auto_-_flex);
        ;
}

#tabsContent {
  height: 100%;
        -moz-flex-basis: auto;
        -ms-flex-basis: auto;
        flex-basis: auto;
        ;
}

#tabsContent.scrollable {
  position: absolute;
        white-space: nowrap;
}

#tabsContent:not(.scrollable), #tabsContent.scrollable.fit-container {
  display: var(--layout-horizontal_-_display); -ms-flex-direction: var(--layout-horizontal_-_-ms-flex-direction); -webkit-flex-direction: var(--layout-horizontal_-_-webkit-flex-direction); flex-direction: var(--layout-horizontal_-_flex-direction);
}

#tabsContent.scrollable.fit-container {
  min-width: 100%;
}

#tabsContent.scrollable.fit-container > ::slotted(*) {
  -ms-flex: 1 0 auto;
        -webkit-flex: 1 0 auto;
        flex: 1 0 auto;
}

.hidden {
  display: none;
}

.not-visible {
  opacity: 0;
        cursor: default;
}

paper-icon-button {
  width: 48px;
        height: 48px;
        padding: 12px;
        margin: 0 4px;
        background-color: var(--paper-icon-buttons_-_background-color); border-radius: var(--paper-icon-buttons_-_border-radius); color: var(--paper-icon-buttons_-_color); height: var(--paper-icon-buttons_-_height, 48px); padding: var(--paper-icon-buttons_-_padding, 12px); position: var(--paper-icon-buttons_-_position); width: var(--paper-icon-buttons_-_width, 48px)
}

paper-icon-button#left {
  left: var(--paper-icon-button-left_-_left); z-index: var(--paper-icon-button-left_-_z-index)
}

paper-icon-button#right {
  right: var(--paper-icon-button-right_-_right)
}

#selectionBar {
  position: absolute;
        height: 0;
        bottom: 0;
        left: 0;
        right: 0;
        border-bottom: 2px solid var(--paper-tabs-selection-bar-color, var(--paper-yellow-a100));
          -webkit-transform: scale(0);
        transform: scale(0);
          -webkit-transform-origin: left center;
        transform-origin: left center;
          transition: -webkit-transform;
        transition: transform;

        z-index: var(--paper-tabs-selection-bar_-_z-index);
}

#selectionBar.align-bottom {
  top: 0;
        bottom: auto;
}

#selectionBar.expand {
  transition-duration: 0.15s;
        transition-timing-function: cubic-bezier(0.4, 0.0, 1, 1);
}

#selectionBar.contract {
  transition-duration: 0.18s;
        transition-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1);
}

#tabsContent > ::slotted(:not(#selectionBar)) {
  height: 100%;
}</style>
    

    <paper-icon-button id="left" icon="paper-tabs:chevron-left" class="not-visible" aria-hidden="true" role="button" aria-disabled="true" aria-label="" disabled="" tabindex="-1" style="pointer-events: none;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt=""><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>

    <div id="tabsContainer" style="touch-action: pan-y;">
      <div id="tabsContent" class="scrollable">
        <div id="selectionBar" class="" style="transform: translateX(0%) scaleX(0);"></div>
        <slot></slot>
      </div>
    </div>

    <paper-icon-button id="right" icon="paper-tabs:chevron-right" class="not-visible" aria-hidden="true" role="button" aria-disabled="true" aria-label="" disabled="" tabindex="-1" style="pointer-events: none;"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon" alt=""><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template></paper-icon-button>
</template>
      </paper-tabs>
      <!--?lit$939691256$--> <paper-icon-button icon="icons:more-horiz" title="Show more" role="button" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-icon-button">:host {
  display: inline-block;
        position: relative;
        padding: 8px;
        outline: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        cursor: pointer;
        z-index: 0;
        line-height: 1;

        width: 40px;
        height: 40px;

        
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -webkit-tap-highlight-color: transparent;

        
        box-sizing: border-box !important;

        ;
}

:host #ink {
  color: var(--paper-icon-button-ink-color, var(--primary-text-color));
        opacity: 0.6;
}

:host([disabled]) {
  color: var(--paper-icon-button-disabled-text, var(--disabled-text-color));
        pointer-events: none;
        cursor: auto;

        ;
}

:host([hidden]) {
  display: none !important;
}

:host(:hover) {
  ;
}

iron-icon {
  --iron-icon-width: 100%;
        --iron-icon-height: 100%;
}</style><iron-icon id="icon"><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M6 10c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm12 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-6 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></template>
  </paper-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./titanic_survival_prediction_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; camera; gyroscope; magnetometer; microphone; serial; usb; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals allow-popups-to-escape-sandbox" src="./titanic_survival_prediction_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar" style="min-height: inherit;"><template shadowrootmode="open"><!----> <!--?lit$939691256$--> <div class="connect-status">
        <md-icon status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$--><svg viewBox="0 0 24 24"><!--?lit$939691256$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
        <div aria-atomic="true" aria-live="polite"><!--?lit$939691256$-->Connected to Python 3 Google Compute Engine backend</div>
      </div>
      <md-icon-button class="visible-on-closed" title="Connected" aria-label="Connected" disabled="" role="presentation" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Connected" disabled="">
        <!--?lit$939691256$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$939691256$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$939691256$--><span class="icon"><slot></slot></span>
        <!--?lit$939691256$-->
        <!--?lit$939691256$--><span class="touch"></span>
        <!--?lit$939691256$-->
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="icon-okay" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$939691256$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <md-icon-button title="Close" aria-label="Close" role="presentation" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$939691256$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$939691256$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$939691256$--><span class="icon"><slot></slot></span>
        <!--?lit$939691256$-->
        <!--?lit$939691256$--><span class="touch"></span>
        <!--?lit$939691256$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$939691256$--><div command="locate-in-drive" class="goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Locate in Drive<!--?lit$939691256$--></div></div><div command="open-in-playground" class="goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Open in playground mode<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class="goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->New notebook<!--?lit$939691256$--></div></div><div command="open" class="goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Open notebook<!--?lit$939691256$--></div></div><div command="import-notebook" class="goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Upload notebook<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class="goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Rename<!--?lit$939691256$--></div></div><div command="move-notebook" class="goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Move<!--?lit$939691256$--></div></div><div command="trash" class="goog-menuitem " role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Move to the bin<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class="goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Save a copy in Drive<!--?lit$939691256$--></div></div><div command="copy-to-gist" class="goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Save a copy as a GitHub Gist<!--?lit$939691256$--></div></div><div command="copy-to-github" class="goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Save a copy in GitHub<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class="goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Save<!--?lit$939691256$--></div></div><div command="save-and-checkpoint" class="goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Save and pin revision<!--?lit$939691256$--></div></div><div command="show-history" class="goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Revision history<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$939691256$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class="goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Print<!--?lit$939691256$--></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$939691256$--><div command="download-ipynb" class="goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Download .ipynb<!--?lit$939691256$--></div></div><div command="download-python" class="goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Download .py<!--?lit$939691256$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$939691256$--><div command="undo" class="goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Undo<!--?lit$939691256$--></div></div><div command="redo" class="goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Redo<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class="goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Select all cells<!--?lit$939691256$--></div></div><div command="cut" class="goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Cut cell or selection<!--?lit$939691256$--></div></div><div command="copy" class="goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Copy cell or selection<!--?lit$939691256$--></div></div><div command="paste" class="goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Paste<!--?lit$939691256$--></div></div><div command="delete-cell-or-selection" class="goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Delete selected cells<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class="goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Find and replace<!--?lit$939691256$--></div></div><div command="find-next" class="goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Find next<!--?lit$939691256$--></div></div><div command="find-previous" class="goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Find previous<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class="goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Notebook settings<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class="goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Clear all outputs<!--?lit$939691256$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$939691256$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><iron-icon><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></div><!--?lit$939691256$-->Table of contents<!--?lit$939691256$--></div></div><div command="show-fileinfo" class="goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Notebook info<!--?lit$939691256$--></div></div><div command="show-executedcode" class="goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Executed code history<!--?lit$939691256$--></div></div><div command="toggle-comments-visibility" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><iron-icon><template shadowrootmode="open"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></g></svg><style scope="iron-icon">:host {
  display: var(--layout-inline_-_display);
        -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
        position: relative;

        vertical-align: middle;

        fill: var(--iron-icon-fill-color, currentcolor);
        stroke: var(--iron-icon-stroke-color, none);

        width: var(--iron-icon-width, 24px);
        height: var(--iron-icon-height, 24px);
        ;
}

:host([hidden]) {
  display: none;
}</style>
    
</template></iron-icon></div><!--?lit$939691256$-->Comments sidebar<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1b" style="user-select: none;"></div><div command="collapse-sections" class="goog-menuitem " role="menuitem" id=":1c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Collapse sections<!--?lit$939691256$--></div></div><div command="expand-sections" class="goog-menuitem " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Expand sections<!--?lit$939691256$--></div></div><div command="save-section-layout" class="goog-menuitem " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Save collapsed section layout<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1f" style="user-select: none;"></div><div command="hide-code" class="goog-menuitem " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Show/hide code<!--?lit$939691256$--></div></div><div command="toggle-output" class="goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Show/hide output<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1i" style="user-select: none;"></div><div command="focus-next-tab" class="goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Focus next tab<!--?lit$939691256$--></div></div><div command="focus-previous-tab" class="goog-menuitem " role="menuitem" id=":1k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Focus previous tab<!--?lit$939691256$--></div></div><div command="move-tab-to-next" class="goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Move tab to next pane<!--?lit$939691256$--></div></div><div command="move-tab-to-prev" class="goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Move tab to previous pane<!--?lit$939691256$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$939691256$--><div command="insert-cell-below" class="goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Code cell<!--?lit$939691256$--></div></div><div command="add-text" class="goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Text cell<!--?lit$939691256$--></div></div><div command="add-section-header" class="goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Section header cell<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1r" style="user-select: none;"></div><div command="open-scratch-code-cell" class="goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Scratch code cell<!--?lit$939691256$--></div></div><div command="snippets" class="goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Code snippets<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1u" style="user-select: none;"></div><div command="add-form-field" class="goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Add a form field<!--?lit$939691256$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$939691256$--><div command="runall" class="goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Run all<!--?lit$939691256$--></div></div><div command="runbefore" class="goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Run before<!--?lit$939691256$--></div></div><div command="runfocused" class="goog-menuitem " role="menuitem" id=":1z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Run the focused cell<!--?lit$939691256$--></div></div><div command="runselected" class="goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Run selection<!--?lit$939691256$--></div></div><div command="runafter" class="goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Run after<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":22" style="user-select: none;"></div><div command="interrupt" class="goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Interrupt execution<!--?lit$939691256$--></div></div><div command="restart" class="goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Restart session<!--?lit$939691256$--></div></div><div command="restart-and-run-all" class="goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Restart session and run all<!--?lit$939691256$--></div></div><div command="powerwash-current-vm" class="goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Disconnect and delete runtime<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="change-runtime-type" class="goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Change runtime type<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":29" style="user-select: none;"></div><div command="manage-sessions" class="goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Manage sessions<!--?lit$939691256$--></div></div><div command="open-resource-viewer" class="goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->View resources<!--?lit$939691256$--></div></div><div command="view-runtime-logs" class="goog-menuitem " role="menuitem" id=":2c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->View runtime logs<!--?lit$939691256$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$939691256$--><div command="show-command-palette" class="goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Command palette<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2f" style="user-select: none;"></div><div command="preferences" class="goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Settings<!--?lit$939691256$--></div></div><div command="shortcuts" class="goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Keyboard shortcuts<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="open-differ" class="goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Diff notebooks<!--?lit$939691256$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$939691256$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$939691256$--><div command="faq" class="goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Frequently asked questions<!--?lit$939691256$--></div></div><div command="view-relnotes" class="goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->View release notes<!--?lit$939691256$--></div></div><div command="snippets" class="goog-menuitem " role="menuitem" id=":2n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Search code snippets<!--?lit$939691256$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2o" style="user-select: none;"></div><div command="report-bug" class="goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Report a bug<!--?lit$939691256$--></div></div><div command="report-abuse" class="goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Report Drive abuse<!--?lit$939691256$--></div></div><div command="send-feedback" class="goog-menuitem " role="menuitem" id=":2r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->Send feedback<!--?lit$939691256$--></div></div><div command="view-in-english" class="goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$939691256$-->View in English<!--?lit$939691256$--></div></div></div><div class="doc-comments-area" style="display: none;"><!----><div class="doc-comments-buttons">
        <paper-button command="add-comment" role="button" animated="" elevation="0" aria-disabled="false" tabindex="0"><template shadowrootmode="open"><style scope="paper-button">:host, html {
  --paper-material_-_display:  block; --paper-material_-_position:  relative;;
        --paper-material-elevation-1_-_box-shadow:  var(--shadow-elevation-2dp_-_box-shadow);;
        --paper-material-elevation-2_-_box-shadow:  var(--shadow-elevation-4dp_-_box-shadow);;
        --paper-material-elevation-3_-_box-shadow:  var(--shadow-elevation-6dp_-_box-shadow);;
        --paper-material-elevation-4_-_box-shadow:  var(--shadow-elevation-8dp_-_box-shadow);;
        --paper-material-elevation-5_-_box-shadow:  var(--shadow-elevation-16dp_-_box-shadow);;
}

:host(.paper-material), .paper-material {
  display: var(--paper-material_-_display); position: var(--paper-material_-_position);
}

:host(.paper-material[elevation="1"]), .paper-material[elevation="1"] {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host(.paper-material[elevation="2"]), .paper-material[elevation="2"] {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host(.paper-material[elevation="3"]), .paper-material[elevation="3"] {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host(.paper-material[elevation="4"]), .paper-material[elevation="4"] {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host(.paper-material[elevation="5"]), .paper-material[elevation="5"] {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host {
  display: var(--layout-inline_-_display);
      -ms-flex-align: var(--layout-center-center_-_-ms-flex-align); -webkit-align-items: var(--layout-center-center_-_-webkit-align-items); align-items: var(--layout-center-center_-_align-items); -ms-flex-pack: var(--layout-center-center_-_-ms-flex-pack); -webkit-justify-content: var(--layout-center-center_-_-webkit-justify-content); justify-content: var(--layout-center-center_-_justify-content);
      position: relative;
      box-sizing: border-box;
      min-width: 5.14em;
      margin: 0 0.29em;
      background: transparent;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
      -webkit-tap-highlight-color: transparent;
      font: inherit;
      text-transform: uppercase;
      outline-width: 0;
      border-radius: 3px;
      -moz-user-select: none;
      -ms-user-select: none;
      -webkit-user-select: none;
      user-select: none;
      cursor: pointer;
      z-index: 0;
      padding: 0.7em 0.57em;

      font-family: var(--paper-font-common-base_-_font-family); -webkit-font-smoothing: var(--paper-font-common-base_-_-webkit-font-smoothing);
      ;
}

:host([elevation="1"]) {
  box-shadow: var(--paper-material-elevation-1_-_box-shadow);
}

:host([elevation="2"]) {
  box-shadow: var(--paper-material-elevation-2_-_box-shadow);
}

:host([elevation="3"]) {
  box-shadow: var(--paper-material-elevation-3_-_box-shadow);
}

:host([elevation="4"]) {
  box-shadow: var(--paper-material-elevation-4_-_box-shadow);
}

:host([elevation="5"]) {
  box-shadow: var(--paper-material-elevation-5_-_box-shadow);
}

:host([hidden]) {
  display: none !important;
}

:host([raised].keyboard-focus) {
  font-weight: bold;
      ;
}

:host(:not([raised]).keyboard-focus) {
  font-weight: bold;
      ;
}

:host([disabled]) {
  background: none;
      color: #a8a8a8;
      cursor: auto;
      pointer-events: none;

      ;
}

:host([disabled][raised]) {
  background: #eaeaea;
}

:host([animated]) {
  transition: var(--shadow-transition_-_transition);
}

paper-ripple {
  color: var(--paper-button-ink-color);
}</style><slot></slot></template>
          <md-icon filled="" class="layout align-middle" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$939691256$-->Add a comment
        </paper-button>
      </div></div><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy5eb495b9718564b9494d5eb929c80d6b1c2fedff0.806441206" name="apiproxy5eb495b9718564b9494d5eb929c80d6b1c2fedff0.806441206" src="./titanic_survival_prediction_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s ease 0s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-piewde1ktrrs" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./titanic_survival_prediction_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./titanic_survival_prediction_files/saved_resource.html"></iframe></div><iframe id="apiproxyb66848ecd7c3e55eb861f491bca2131c05cb76220.2498077754" name="apiproxyb66848ecd7c3e55eb861f491bca2131c05cb76220.2498077754" src="./titanic_survival_prediction_files/proxy(1).html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><iframe src="./titanic_survival_prediction_files/bscframe.html" style="display: none;"></iframe></body></html>