import type { ComponentType } from 'react';
import { useMemo, useState } from 'react';
import Landing from './views/Landing';
import LeadLeakCalculator from './views/LeadLeakCalculator';
import InstagramDMFlow from './views/InstagramDMFlow';
import FreeLeadAuditForm from './views/FreeLeadAuditForm';
import PilotSignup from './views/PilotSignup';
import { businessMeta, frontendViews, type RouteKey } from './businessMeta';
import './styles.css';

const routes: Record<RouteKey, ComponentType> = {
  landing: Landing,
  'lead-leak-calculator': LeadLeakCalculator,
  'instagram-dm-flow': InstagramDMFlow,
  'free-lead-audit-form': FreeLeadAuditForm,
  'pilot-signup': PilotSignup,
};

export default function App() {
  const [route, setRoute] = useState<RouteKey>('landing');
  const ActiveView = useMemo(() => routes[route], [route]);
  const activeView = frontendViews.find((view) => view.route === route) ?? frontendViews[0];

  return (
    <div className="app-shell">
      <nav className="top-nav" aria-label="Med Spa Lead Recovery prototype sections">
        <div className="brand-block">
          <strong>{businessMeta.name}</strong>
          <span>{activeView.buyerSignal}</span>
        </div>
        <div className="nav-actions" role="list">
          {frontendViews.map((view) => (
            <button
              key={view.route}
              type="button"
              onClick={() => setRoute(view.route)}
              className={route === view.route ? 'active' : ''}
              aria-current={route === view.route ? 'page' : undefined}
            >
              {view.navLabel}
            </button>
          ))}
        </div>
      </nav>
      <ActiveView />
    </div>
  );
}
